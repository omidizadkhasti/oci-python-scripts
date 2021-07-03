import json
import os
import sys
import configparser
import base64
import oci
import logging


def readConfigFile(environment):
    config = configparser.ConfigParser()
    config.read('securityList.properties')
    return dict(config.items(environment))


def addIngressRuleToSL(sgOCID, portNumber, protocol, sourceCIDR):
    try:
        virtual_network_client = oci.core.VirtualNetworkClient(config, signer=signer)
        resp = virtual_network_client.get_security_list(commConfig["securitylist_ocid"]).data
        ingress_rules = resp.ingress_security_rules

        ingressSecRule = oci.core.models.IngressSecurityRule(
            source_type='CIDR_BLOCK',
            is_stateless=False,
            protocol=protocol,
            source=sourceCIDR,
            tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(
                    max=portNumber,
                    min=portNumber
                )
                )
            )

        ingress_rules.append(ingressSecRule)

        update_nsg_response = virtual_network_client.update_security_list(
                commConfig["securitylist_ocid"],
                oci.core.models.UpdateSecurityListDetails(
                    display_name="test_securitylist",
                    ingress_security_rules=ingress_rules
                )
            ).data    
    except Exception as e:
        print("\nError creating ingress rule - " + str(e))
        raise SystemExit

def addEgressRuleToSL(sgOCID, portNumber, protocol, destinationCIDR):
    try:
        virtual_network_client = oci.core.VirtualNetworkClient(config, signer=signer)
        resp = virtual_network_client.get_security_list(commConfig["securitylist_ocid"]).data
        egress_rules = resp.egress_security_rules

        egressSecRule = oci.core.models.EgressSecurityRule(
            destination_type='CIDR_BLOCK',
            is_stateless=False,
            protocol=protocol,
            destination=destinationCIDR,
            tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(
                    max=portNumber,
                    min=portNumber
                )
                )
            )

        egress_rules.append(egressSecRule)

        update_nsg_response = virtual_network_client.update_security_list(
                commConfig["securitylist_ocid"],
                oci.core.models.UpdateSecurityListDetails(
                    display_name="test_securitylist",
                    egress_security_rules=egress_rules
                )
            ).data    
    except Exception as e:
        print("\nError creating egress rule - " + str(e))
        raise SystemExit

def create_signer(config_file, config_profile, is_instance_principals):

    # if instance principals authentications
    if is_instance_principals==True:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception as ex:
            logging.getLogger().info("Error obtaining instance principals certificate, aborting" + str(ex))
            raise SystemExit
    # -----------------------------
    # config file authentication
    # -----------------------------
    else:
        config = oci.config.from_file(
            (config_file if config_file else oci.config.DEFAULT_LOCATION),
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        return config, signer


commConfig = readConfigFile("DEFAULT")

config, signer = create_signer(commConfig["config_file"], commConfig["config_profile"], commConfig["is_instance_principals"])

addIngressRuleToSL(commConfig["securitylist_ocid"], 7001, '6', '10.0.0.0/16')
addEgressRuleToSL(commConfig["securitylist_ocid"], 7001, '6', '10.0.0.0/16')

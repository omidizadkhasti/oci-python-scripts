import json
import os
import sys
import configparser
import base64
import oci
import logging


def readConfigFile(environment):
    config = configparser.ConfigParser()
    config.read('autoscaling.properties')
    return dict(config.items(environment))


def createInstanceConfiguration(compartmentId, imageId, shape, availibilityDomain, backupVolumeId, sshKey, displayName):
    try:

        core_client = oci.core.ComputeManagementClient(config, signer=signer)

        create_instance_configuration_response = core_client.create_instance_configuration(
            create_instance_configuration=oci.core.models.CreateInstanceConfigurationDetails(
                source="NONE",
                compartment_id=compartmentId,
                instance_details=oci.core.models.ComputeInstanceDetails(
                    instance_type="compute",
                    block_volumes=[
                        oci.core.models.InstanceConfigurationBlockVolumeDetails(
#                            attach_details=oci.core.models.InstanceConfigurationIscsiAttachVolumeDetails(
#                                display_name="autoscaling_bv_attach",
#                                type="iscsi"),
                            attach_details=oci.core.models.InstanceConfigurationParavirtualizedAttachVolumeDetails(
                                display_name="autoscaling_bv_attach",
                                type="paravirtualized"
                            ),
                            create_details=oci.core.models.InstanceConfigurationCreateVolumeDetails(
                                availability_domain=availibilityDomain,
                                compartment_id=compartmentId,
                                display_name="autoscaling_bv_1",
                                source_details=oci.core.models.InstanceConfigurationVolumeSourceFromVolumeDetails(
                                    type="volumeBackup",
                                    id=backupVolumeId)),
                            )],
                    launch_details=oci.core.models.InstanceConfigurationLaunchInstanceDetails(
                        availability_domain=availibilityDomain,
                        compartment_id=compartmentId,
                        display_name=displayName,
                        metadata={
                            'ssh_authorized_keys': sshKey},
                        shape=shape,
                        shape_config=oci.core.models.InstanceConfigurationLaunchInstanceShapeConfigDetails(
                            ocpus=1,
                            memory_in_gbs=16),
#                        shape_config=oci.core.models.InstanceConfigurationLaunchInstanceShapeConfigDetails(
#                            ocpus=3244.6516,
#                            memory_in_gbs=719.0478,
#                            baseline_ocpu_utilization="BASELINE_1_1"),
                        source_details=oci.core.models.InstanceConfigurationInstanceSourceViaImageDetails(
                            source_type="image",
                            image_id=imageId)
                    )
                ),
#                        fault_domain="EXAMPLE-faultDomain-Value",
#                        launch_mode="EMULATED",
                display_name=displayName
            )
        )
        return create_instance_configuration_response.data


    except Exception as e:
        print("\nError creating ingress rule - " + str(e))
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

compartmentId = commConfig["compartment_id"]
imageId = commConfig["image_id"]
shape = commConfig["shape"]
availibilityDomain = commConfig["availibility-domain"]
backupVolumeId = commConfig["backup-volume-id"]
sshKey = commConfig["ssh-key"]
displayName = commConfig["display-name"]


print(createInstanceConfiguration(compartmentId, imageId, shape, availibilityDomain, backupVolumeId, sshKey, displayName))


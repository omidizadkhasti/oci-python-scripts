
import oci

config = oci.config.from_file('~/.oci/config','<Config Profile>')

core_client = oci.core.VirtualNetworkClient(config)

update_vcn_response = core_client.update_subnet(
    subnet_id="<OCI VCN OCID>",
    update_subnet_details=oci.core.models.UpdateSubnetDetails(
        display_name="<New Display Name>"))

# Get the data from response
print(update_subnet_response.data)

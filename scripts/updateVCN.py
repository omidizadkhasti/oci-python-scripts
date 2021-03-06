import oci

config = oci.config.from_file('~/.oci/config','<Config Profile>')

core_client = oci.core.VirtualNetworkClient(config)

update_vcn_response = core_client.update_vcn(
    vcn_id="<OCI VCN OCID>",
    update_vcn_details=oci.core.models.UpdateVcnDetails(
        display_name="<New Display Name>"))

# Get the data from response
print(update_vcn_response.data)

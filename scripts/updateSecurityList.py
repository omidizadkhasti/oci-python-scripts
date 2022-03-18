mport oci

config = oci.config.from_file('/etc/oci/config','eu-frankfurt-1')

core_client = oci.core.VirtualNetworkClient(config)

update_security_list_response = core_client.update_security_list(
    security_list_id="",
    update_security_list_details=oci.core.models.UpdateSecurityListDetails(
        display_name="db-nonprod-subnet"))

# Get the data from response
print(update_security_list_response.data)

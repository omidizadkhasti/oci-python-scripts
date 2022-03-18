mport oci

config = oci.config.from_file('/etc/oci/config','eu-frankfurt-1')

core_client = oci.core.VirtualNetworkClient(config)

update_vcn_response = core_client.update_ssecurity_list(
    seclist_id="",
    update_security_list_details=oci.core.models.UpdateSecurityListtDetails(
        display_name="db-nonprod-subnet"))

# Get the data from response
print(update_security_list_response.data)

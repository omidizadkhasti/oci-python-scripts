import oci

config = oci.config.from_file('~/.oci/config','<Config Profile>')

core_client = oci.integration.IntegrationInstanceClient(config)

update_integration_instance_response = integration_client.update_integration_instance(
    integration_instance_id="",
    update_integration_instance_details=oci.integration.models.UpdateIntegrationInstanceDetails(
        display_name="")

# Get the data from response
print(update_integration_instance_response.data)

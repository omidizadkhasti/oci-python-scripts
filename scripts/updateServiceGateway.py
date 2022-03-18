import oci

config = oci.config.from_file('/etc/oci/config','eu-frankfurt-1')

core_client = oci.core.VirtualNetworkClient(config)

update_service_gateway_response = core_client.update_service_gateway(
    service_gateway_id="",
    update_service_gateway_details=oci.core.models.UpdateServiceGatewayDetails(
        display_name="ResMed-SG"))

# Get the data from response
print(update_service_gateway_response.data)

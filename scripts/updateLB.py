import oci

config = oci.config.from_file('/etc/oci/config','eu-frankfurt-1')

load_balancer_client = oci.load_balancer.LoadBalancerClient(config)

update_load_balancer_response = load_balancer_client.update_load_balancer(
    update_load_balancer_details=oci.load_balancer.models.UpdateLoadBalancerDetails(
        display_name=""),
    load_balancer_id="")

print(update_load_balancer_response.headers)

# oci-python-scripts
This repository includes python scripts to manage OCI resources using the OCI python SDK. 

- Autoscaling script: This script use for attach custom block volume (backup volume) to instances in autoscaling group.
- SecurityList script: This script use OCI python SDK and add new Security List rule to existing subnet.

Each script has a properties file that contains parameter for that script. some of parameters are common between all scripts (same as OCI configuration) and some of the are specific for each script that you can find more information about specific parameters in readme file for that script. 

### Common properties
If you want to use the OCI config file, use following parameters in DEFAULT section of property file:  
```
config_file=<path of oci config file in filesystem>
is_instance_principals=false
config_profile=<profile name in oci config file>
```

if you want to use instance principal, use following parameters in DEFAULT section of property file (valuse of other two parameters are not important):  
```
is_instance_principals=true
```
if you have multiple OCI config profile in your machine, specified the profile name in config_profile parameter.

for example if you have following configuration in OCI config file (under /home/opc/.oci/oci_config) and you want to use 'Test_Tenancy' configuration in your script, you should update proprty file as below.

OCI Config file

```
[DEFAULT]
user=ocid1.user.oc1.#####
fingerprint=####
key_file=<Key File Path>
tenancy=ocid1.tenancy.oc1.####
region=ap-melbourne-1
pass_phrase=<Kety File Passphrase>
[Test_Tenancy]
user=ocid1.user.oc1.#####
fingerprint=####
key_file=<Key File Path>
tenancy=ocid1.tenancy.oc1.####
region=ap-sydney-1
pass_phrase=<Kety File Passphrase>
```

Property file

```
config_file=/home/opc/.oci/oci_config
is_instance_principals=false
config_profile=Test_Tenancy
```

# Create pytyhon evirtual environment
```
python3 -m venv oci-script
#Activate environment
source oci-scripts/bin/activate
#Deactivate environment
deactivate
python3 -m pip install oci


```

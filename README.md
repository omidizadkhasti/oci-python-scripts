# oci-python-scripts
This repository includes python scripts to manage OCI resources using OCI python SD.  
Each script has a properties file that contains parameter for that script.  

### Common properties
If you want ti use OCI config file, use following parameters in DEFAULT section of property file:  
```
config_file=<path of oci config file in filesystem>
is_instance_principals=false
config_profile=<profile name in oci config file>
```

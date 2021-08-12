# oci-python-scripts
This repository includes python scripts to manage OCI resources using the OCI python SDK. 

- Autoscaling script: 
- SecurityList script: 

Each script has a properties file that contains parameter for that script. some of parameters are common between all scripts (same as OCI configuration) and some of the are specific for each script that you can find more information about specific parameters in readme file for that script. 

### Common properties
If you want to use the OCI config file, use following parameters in DEFAULT section of property file:  
```
config_file=<path of oci config file in filesystem>
is_instance_principals=false
config_profile=<profile name in oci config file>
```

if you want to use instance principal, use following parameters in DEFAULT section of property file:  
```
is_instance_principals=true
```

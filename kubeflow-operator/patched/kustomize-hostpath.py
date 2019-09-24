import yaml

y = yaml.safe_load(open("kustomize/katib-db/base/katib-db-deployment.yaml"))
y["spec"]["template"]["spec"]["containers"][0]["securityContext"]={}
y["spec"]["template"]["spec"]["containers"][0]["securityContext"]["privileged"]=True
y["spec"]["template"]["spec"]["securityContext"]={}
y["spec"]["template"]["spec"]["securityContext"]["seLinuxOptions"]={}
y["spec"]["template"]["spec"]["securityContext"]["seLinuxOptions"]["level"]="s0:c13,c12"
yaml.dump(y, open("kustomize/katib-db/base/katib-db-deployment.yaml",'w'), default_flow_style=False)
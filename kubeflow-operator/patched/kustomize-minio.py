import yaml

y = yaml.safe_load(open("kustomize/minio/base/deployment.yaml"))
del y["spec"]["template"]["spec"]["containers"][0]["volumeMounts"][0]["subPath"]
yaml.dump(y, open("kustomize/minio/base/deployment.yaml",'w'), default_flow_style=False)
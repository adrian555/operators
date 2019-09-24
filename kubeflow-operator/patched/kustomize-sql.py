import yaml

y = yaml.safe_load(open("kustomize/katib-db/base/kustomization.yaml"))
for x in y["images"]:
  if x["name"] == "mysql":
    x["newName"] = "mysql"
    x["newTag"] = "5.6"
yaml.dump(y, open("kustomize/katib-db/base/kustomization.yaml",'w'), default_flow_style=False)

y = yaml.safe_load(open("kustomize/metadata/base/kustomization.yaml"))
if y.get("images", ""):
  for x in y["images"]:
    if x["name"] == "mysql":
      x["newName"] = "mysql"
      x["newTag"] = "5.6"
else:
  y["images"] = [{"name": "mysql", "newTag": "5.6"}]
yaml.dump(y, open("kustomize/metadata/base/kustomization.yaml",'w'), default_flow_style=False)
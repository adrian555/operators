# Copyright 2019 IBM Corporation 
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
import yaml
import os

y = yaml.safe_load(open("app.yaml"))
for x in y["spec"]["applications"]:
  if x["name"] == "argo":
    x["kustomizeConfig"]["overlays"].append('pns')
yaml.dump(y, open("app.yaml",'w'), default_flow_style=False)

y = yaml.safe_load(open("kustomize/argo/kustomization.yaml"))
if "patches" not in y:
  y["patches"]=[]
y["patches"].append("overlays/pns/config-map.yaml")
y["patches"].append("overlays/pns/params.yaml")
yaml.dump(y, open("kustomize/argo/kustomization.yaml",'w'), default_flow_style=False)

image, tag = os.environ.get("WORKFLOW_CONTROLLER_IMAGE", "tomcli/workflow-controller:containerd").split(':')
y = yaml.safe_load(open("kustomize/argo/base/kustomization.yaml"))
for x in y["images"]:
  if x["name"] == "argoproj/workflow-controller":
    x["newName"] = image
    x["newTag"] = tag
yaml.dump(y, open("kustomize/argo/base/kustomization.yaml",'w'), default_flow_style=False)

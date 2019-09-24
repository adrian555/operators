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

y = yaml.safe_load(open("/opt/ansible/kfctl_k8s_istio.yaml"))
if os.getenv("KUBEFLOW_RELEASE", "v0.6.2") == "v0.6.1":
  del y["spec"]["componentParams"]["istio-crds"]
  del y["spec"]["componentParams"]["istio-install"]
  del y["spec"]["components"]["istio-crds"]
  del y["spec"]["components"]["istio-install"]
else:
  y["spec"]["applications"]=[x for x in y["spec"]["applications"] if x["name"] not in ["istio-crds", "istio-install"]]
yaml.dump(y, open("/opt/ansible/kfctl_k8s_istio.yaml",'w'), default_flow_style=False)
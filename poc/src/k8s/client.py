import os
import requests
import k8s.parser


class Client:

#--------------------------------------------------------------------
  
  def __init__(self):
    # Authentication
    self.cert_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    self.token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"

    # Namespace
    ns_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
    with open(ns_path) as f:
      ns = f.read()

    # Kube API url
    kube_host = os.environ['KUBERNETES_SERVICE_HOST']
    self.url = "https://" + kube_host + "/api/v1/namespaces/" + ns + "/pods"

#--------------------------------------------------------------------

  def get_pods(self):
    try:
      # TODO: Find out how often token changes
      with open(self.token_path) as f:
        token = f.read()

      hdrs = {'Authorization': 'Bearer ' + token}
      r = requests.get(self.url, verify=self.cert_path, headers=hdrs)
    except Exception as err:
      return (False, err)

    if r.status_code == 200:
      data = k8s.parser.parse_pods(r.json())
      return (True, data)
    else:
      err = "Could not get \"{}\". {} ({}).".format(url, r.reason, r.status_code)
      return (False, err)


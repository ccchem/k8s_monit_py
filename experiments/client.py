import requests
import k8s.parser


class Client:

  def get_pods(self):
    url = "http://localhost:8000/pods.json"

    try:
      r = requests.get(url)
    except Exception as err:
      return (False, err)

    if r.status_code == 200:
      data = k8s.parser.parse_pods(r.json())
      return (True, data)
    else:
      err = "Could not get \"{}\". {} ({}).".format(url, r.reason, r.status_code)
      return (False, err)



# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

all_projects_url = "https://infinitusai.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("ashwath.sh@infinitus.ai", "ATATT3xFfGF0BUBsolCEdgRgkDSfR_MVDxDK68svXWTeaEh5tjKWEvVZow6hP0bxsaJnz6jeFzSiwzvJjgH1TY3ZItcFLKB_wcj9snTmn0Idvpgvm58W3vqYZEQGoRTiqUUc7aGkJJ9alT0mYuJ2c0RT5EyketZH8-Y9gU3astxQHSEttkw5VSk=74230877")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   all_projects_url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
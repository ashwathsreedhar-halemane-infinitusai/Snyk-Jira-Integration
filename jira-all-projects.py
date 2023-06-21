# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

all_projects_url = "https://infinitusai.atlassian.net/rest/api/3/project"

jira_api_token = os.environ.get("JIRA_API_TOKEN")

auth = HTTPBasicAuth("ashwath.sh@infinitus.ai", jira_api_token)

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

print(response.status_code)

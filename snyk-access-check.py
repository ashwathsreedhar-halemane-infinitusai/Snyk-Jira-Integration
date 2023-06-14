# demo app to check access to Snyk API

import requests
import json
import os

# get the Snyk API token from the environment
snyk_api_token = "15003490-726b-48e5-bb22-22999bda0c0a"

# curl -H "Authorization: token 15003490-726b-48e5-bb22-22999bda0c0a" "https://snyk.io/api/v1/orgs"
# call get orgs API to get the org details

snyk_api_url = "https://snyk.io/api/v1/orgs"

snyk_token = os.environ.get("SNYK_TOKEN")

headers = {
    "Authorization": "token " + snyk_api_token
}

response = requests.request("GET" ,snyk_api_url, headers=headers)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# get details of one org by name

# snyk_one_org_url = "https://snyk.io/api/v1/org/infinitus-ai"


import requests
import json
import os

# get the Snyk API token from the environment
snyk_token = os.environ.get("SNYK_TOKEN")
org_id= os.environ.get("synk_org_id_infinitus") # Infinitus org
project_id= os.environ.get("snyk_absinthe_code_analysis_project_id") # Absinthe code analysis 


snyk_url="https://snyk.io/api/v1/org/"+org_id+"/project/"+project_id

headers = {
    "Authorization": "token " + snyk_token
}

response = requests.request("GET" ,snyk_api_url, headers=headers)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
import requests
import json
import os

# get the Snyk API token from the environment
snyk_token = os.environ.get("SNYK_API_TOKEN")
# org_id= os.environ.get("synk_org_id_infinitus") # Infinitus org
org_id = "0ab5aa02-0901-47b0-bf3e-f515c14981c5"
# project_id= os.environ.get("snyk_absinthe_code_analysis_project_id") # Absinthe code analysis 
project_id = "5dccaa30-d108-4db1-81e1-e361561a48fe"
snyk_api_url="https://snyk.io/api/v1/org/"+org_id+"/project/"+project_id

headers = {
    "Authorization": "token " + str(snyk_token)
}

response = requests.request("GET" ,snyk_api_url, headers=headers)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
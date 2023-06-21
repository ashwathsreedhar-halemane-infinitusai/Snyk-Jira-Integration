import requests
import json
import os

# get the Snyk API token from the environment
snyk_token = os.environ.get("SNYK_API_TOKEN")
org_id= os.environ.get("synk_org_id_infinitus") # Infinitus org
project_id= os.environ.get("snyk_absinthe_code_analysis_project_id") # Absinthe code analysis 
snyk_api_url="https://snyk.io/api/v1/org/"+org_id+"/issues" + "?project_id=" + project_id + "&version=2021-08-20~experimental"

# url = f"https://api.snyk.io/v3/orgs/{SNYK_ORG}/projects?version=2021-06-04~beta"

print("Snyk URL: " +snyk_api_url) 

headers = {
    "Authorization": "token " + str(snyk_token),
    "Content-Type": "application/json" 
}
snyk_body = json.dumps({
  "includeDescription": True,
  "includeIntroducedThrough": True
})
response = requests.request("POST" ,snyk_api_url, headers=headers, data=snyk_body)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
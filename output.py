import json    
import requests
import sys
import os

def jira_request(method="GET", data=None):
    jira_url = "https://infinitusai.atlassian.net/rest/api/3/"
    headers = {
        'Content-Type': 'application/json',
    }

    jira_auth = os.getenv("JIRA_AUTH")
    auth = (jira_auth, "")

    if(method == "GET"):
        response = requests.request(method, jira_url, headers=headers, auth=auth, data=data)
    elif(method == "POST"):
        response = requests.request(method, jira_url, headers=headers, auth=auth, json=data)

    response.raise_for_status()
    return response.json()

def list_all_issues():
    SNYK_TOKEN=os.getenv("SNYK_API_TOKEN")
    SNYK_ORG=os.getenv("synk_org_id_infinitus")

    url = f"https://snyk.io/api/v1/org/{SNYK_ORG}/projects"

    payload={}
    headers = {
    'Authorization': f'token {SNYK_TOKEN}',
    }

    url = f"https://api.snyk.io/v3/orgs/{SNYK_ORG}/projects?version=2021-06-04~beta"
    def paginate_call(url):
        response_json = requests.request("GET", url, headers=headers, data=payload).json()
        data = response_json['data']
        while 'next' in response_json['links']:
            url = f"https://api.snyk.io/v3{response_json['links']['next']}"
            response_json = requests.request("GET", url, headers=headers, data=payload).json()
            data += response_json['data']
        return data

    output = {}
    for project in paginate_call(url):
        if project["attributes"]['name'].split(':')[0] not in output:
            output[project["attributes"]['name'].split(':')[0]] = []
        # Snyk Code
        if 'sast' in project['attributes']['type'].lower():
            url = f"https://api.snyk.io/v3/orgs/{SNYK_ORG}/issues?version=2021-08-20~experimental&project_id={project['id']}"
            print(url)
            for issue in paginate_call(url):
                url = f"https://api.snyk.io/v3/orgs/{SNYK_ORG}/issues/detail/code/{issue['id']}?version=2021-08-20~experimental&project_id={project['id']}"
                # print(url)
                issue = requests.request("GET", url, headers=headers, data=payload).json()['data']
                ignore = {}
                if issue['attributes']['ignored']:
                    url = f"https://snyk.io/api/v1/org/{SNYK_ORG}/project/{project['id']}/ignore/{issue['id']}"
                    ignore = requests.request("GET", url, headers=headers, data=payload).json()[0]["*"]
                output[project["attributes"]['name'].split(':')[0]].append({
                    "type": project['attributes']["type"],
                    "project name": project["attributes"]["name"],
                    "project origin": project["attributes"]["origin"],
                    "project reference": project["attributes"]["targetReference"],
                    "project id": project["id"],
                    "project link": f"https://app.snyk.io/org/{SNYK_ORG}/project/{project['id']}",
                    "ignored": issue["attributes"]["ignored"],
                    "ignore reason": ignore["reason"] if issue["attributes"]["ignored"] else "",
                    "file path": issue["attributes"]["primaryFilePath"],
                    "title": issue["attributes"]["title"],
                    "severity": issue["attributes"]["severity"],
                    "remediation": "",
                    "issue description": issue["attributes"]
                })
    

    with open('output.json', 'w+') as f:
        output = json.dump(output, f)

def process_all_issues():
    with open('output.json', 'r') as f:
        output = json.load(f)

    for project in output:
        n_vulnerabilities = len(output[project])
        if(n_vulnerabilities == 0):
            print(f"We found no issues in the project: {project}")
            sys.exit(0)
        else:    
            print(f"We found {len(output[project])} issues in the project: {project}")

            for issue in output[project]:
                # Create a Jira issue.
                severity_priority_map = {"critical": "highest", "high":"high", "medium":"medium", "low":"low"}
                severity_in_jira = issue['severity']
                jira_issue_data = {
                    "project": "VM",
                    "issuetype": "Bug",
                    "summary": issue['title'],
                    "description": issue['issue description'],
                    "assignee": "",
                    "severity": severity_priority_map[severity_in_jira]
                }
            
                # check_if_issue_exists()
                # jira_request(jira_url, "GET", data=None)
                
                # payload=json.dumps(jira_issue_data)

                # headers = {
                # 'Content-Type': 'application/json'
                # }

                # response = requests.request("POST", url, headers=headers, data=payload)
        
                # if issue['ignored']:
                #     print(f"\t\tThis issue is ignored for the reason: {issue['ignore reason']}")
            print("\n")

process_all_issues()

if __name__ == "__main__":
    # list_all_issues()
    # process_all_issues()
    jira_request()
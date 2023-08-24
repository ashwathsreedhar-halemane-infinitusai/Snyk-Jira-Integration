import json    
import requests

def list_all_issues():
    with open('output.json', 'r') as f:
        output = json.load(f)

    for project in output:
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
            # print(jira_issue_data)
            
            url = "https://infinitusai.atlassian.net/rest/api/3/issue"
            payload=json.dumps(jira_issue_data)

            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            # print(f"\t {issue['severity']}    \t {issue['title']} ({issue['type']}): {issue['file path']}")
            # break
            
            # create jira ticket using these data

            if issue['ignored']:
               print(f"\t\tThis issue is ignored for the reason: {issue['ignore reason']}")
        print("\n")

list_all_issues()
import json



# first_issue=None
# for project in output:
#     for issue in output[project]:
#         first_issue=issue
#         print(first_issue)
#         break
#         print(f"\t {issue['severity']}    \t {issue['title']} ({issue['type']}): {issue['file path']}")
#         # create jira ticket using these data
#     # first_issue=one_issue
    

def list_all_issues():
    with open('output.json', 'r') as f:
        output = json.load(f)

    for project in output:
        print(f"We found {len(output[project])} issues in the project: {project}")
        first_issue = None
        for issue in output[project]:
            # Create a Jira issue.
            severity_priority_map = {"critical": "highest", "high":"high", "medium":"medium", "low":"low"}
            first_issue = issue
            severity_in_jira = issue['severity']
            jira_issue_data = {
                "issuetype": "Bug",
                "summary": issue['type'],
                "description": issue['issue description'],
                "assignee": "",
                "project": "VM",
                "severity": severity_priority_map[severity_in_jira]
            }
            print(jira_issue_data)
            break
            print(f"\t {issue['severity']}    \t {issue['title']} ({issue['type']}): {issue['file path']}")
            # create jira ticket using these data

            if issue['ignored']:
               print(f"\t\tThis issue is ignored for the reason: {issue['ignore reason']}")
        print("\n")

list_all_issues()
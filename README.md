# Snyk-Jira-Integration

Try to use this: https://docs.snyk.io/snyk-api-info/other-tools/tool-jira-tickets-for-new-vulns 

To create Jira tickets automatically from a Snyk scan, you can use the Snyk API and the Jira API to integrate the two systems. Here's a general approach to achieve this:

1. Set up API access: Ensure that you have API access to both Snyk and Jira. You'll need API tokens or credentials to authenticate your requests.

2. Retrieve scan results from Snyk: Use the Snyk API to fetch the results of the scan. This can typically be done by making a GET request to the Snyk API endpoint that provides scan details for a specific project or repository.

3. Parse scan results: Extract the relevant information from the Snyk scan results, such as vulnerabilities, affected packages, severity levels, and any additional details you want to include in the Jira ticket.

4. Create Jira tickets: Use the Jira API to programmatically create tickets. Make a POST request to the Jira API endpoint that creates issues or tickets, passing the necessary information as parameters or in the request body. Ensure that you include details such as the vulnerability title, description, severity level, affected package, and any other relevant information.

5. Link tickets to the Snyk scan: In the Jira ticket, include a link or reference back to the Snyk scan. This helps establish the relationship between the vulnerability detected by Snyk and the corresponding Jira ticket.

6. Assign tickets and set priorities: If required, you can assign the tickets to specific team members and set priority levels based on the severity of the vulnerabilities. This can be done by setting the appropriate fields in the Jira API request.

7. Automate the process: To create tickets automatically on an ongoing basis, you can set up a script or program that periodically triggers the above steps. For example, you could schedule a cron job or use a task scheduler to run a script that performs the integration between Snyk and Jira.

Keep in mind that the specific implementation details may vary depending on your Snyk and Jira configurations, as well as the programming language or tools you are using. It's recommended to refer to the documentation of the Snyk API and the Jira API for detailed instructions on how to interact with these systems programmatically.

# Run:

python3 list-all-issues.py 

# Output:

Output.json

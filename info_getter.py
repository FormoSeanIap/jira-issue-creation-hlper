# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os 
from dotenv import load_dotenv

load_dotenv()

# ref: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-group-issue-fields
# url = f'{os.getenv("JIRA_URL")}/rest/api/3/field'
# url = f'{os.getenv("JIRA_URL")}/rest/api/3/field/customfield_10014/contexts'
url = f'{os.getenv("JIRA_URL")}/rest/api/3/project/10000'
api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")
asignee_id = os.getenv("SEAN_ID")

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
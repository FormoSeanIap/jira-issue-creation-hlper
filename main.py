import json
import yaml
import os
import logging
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

load_dotenv()

# ref: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-group-issues
url = f'{os.getenv("JIRA_URL")}/rest/api/3/issue/bulk'
api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")
asignee_id = os.getenv("SEAN_ID")

logger.info(f'Jira URL: {url} \n API Token: {api_token} \n Email: {email}')

with open('configs.yml', 'r') as file:
  configs = yaml.safe_load(file)


auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "issueUpdates": [
    {
      "fields": {
        "summary": "Main order flow broken",
        "issuetype": {
          "id": configs['ISSUE_TYPE']['Task']
        },
        "priority": {
          "id": configs['PRIORITY']['High']
        },
        "project": {
          "id": "10000"
        },
        "duedate": "2019-05-11",
        "assignee": {
          "id": asignee_id
        },
        "customfield_10014": "STUDY2023-1075", #epic link
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order entry fails when selecting supplier.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
      },
      "update": {}
    },
    {
      "fields": {
        "summary": "Main order flow broken",
        "issuetype": {
          "id": configs['ISSUE_TYPE']['Task']
        },
        "priority": {
          "id": configs['PRIORITY']['High']
        },
        "project": {
          "id": "10000"
        },
        "duedate": "2019-05-11",
        "assignee": {
          "id": asignee_id
        },
        "customfield_10014": "STUDY2023-1075", #epic link
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order entry fails when selecting supplier.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
      },
      "update": {}
    },
  ]
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

logger.info(f'Response: \n {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))}')
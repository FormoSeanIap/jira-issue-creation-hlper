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

url = f'{os.getenv("JIRA_URL")}/rest/api/3/issue'
api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")
asignee_id = os.getenv("SEAN_ID")

logger.info(f'Jira URL: {url} \n API Token: {api_token} \n Email: {email}')

configs = yaml.safe_load(open("configs.yml"))

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "assignee": {
      "id": asignee_id
    },
    # "components": [
    #   {
    #     "id": "10000"
    #   }
    # ],
    # "customfield_10011": "JLPT N2",
    # "customfield_10000": "09/Jun/19",
    # "customfield_20000": "06/Jul/19 3:25 PM",
    # "customfield_30000": [
    #   "10000",
    #   "10002"
    # ],
    # "customfield_40000": {
    #   "content": [
    #     {
    #       "content": [
    #         {
    #           "text": "Occurs on all orders",
    #           "type": "text"
    #         }
    #       ],
    #       "type": "paragraph"
    #     }
    #   ],
    #   "type": "doc",
    #   "version": 1
    # },
    # "customfield_50000": {
    #   "content": [
    #     {
    #       "content": [
    #         {
    #           "text": "Could impact day-to-day work.",
    #           "type": "text"
    #         }
    #       ],
    #       "type": "paragraph"
    #     }
    #   ],
    #   "type": "doc",
    #   "version": 1
    # },
    # "customfield_60000": "jira-software-users",
    # "customfield_70000": [
    #   "jira-administrators",
    #   "jira-software-users"
    # ],
    # "customfield_80000": {
    #   "value": "red"
    # },
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
    "duedate": "2019-05-11",
    # "environment": {
    #   "content": [
    #     {
    #       "content": [
    #         {
    #           "text": "UAT",
    #           "type": "text"
    #         }
    #       ],
    #       "type": "paragraph"
    #     }
    #   ],
    #   "type": "doc",
    #   "version": 1
    # },
    # "fixVersions": [
    #   {
    #     "id": "10001"
    #   }
    # ],
    "issuetype": {
      "id": configs['ISSUE_TYPE']['TASK']
    },
    # "labels": [
    #   "bugfix",
    #   "blitz_test"
    # ],
    # "parent": {
    #   "key": "PROJ-123"
    # },
    # "priority": {
    #   "id": "20000"
    # },
    "project": {
      "id": "10000"
    },
    # "reporter": {
    #   "id": "5b10a2844c20165700ede21g"
    # },
    # "security": {
    #   "id": "10000"
    # },
    "summary": "Main order flow broken",
    # "timetracking": {
    #   "originalEstimate": "10",
    #   "remainingEstimate": "5"
    # },
    # "versions": [
    #   {
    #     "id": "10000"
    #   }
    # ]
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

logger.info(f'Response: \n {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))}')

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
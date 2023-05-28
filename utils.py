import os
import logging
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='s%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

load_dotenv()


def get_jira_configs():
  # ref: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-group-issues
  url = f'{os.getenv("JIRA_URL")}/rest/api/3/issue/bulk'
  api_token = os.getenv("API_TOKEN")
  email = os.getenv("EMAIL")

  logger.info(f'Jira URL: {url} \n API Token: {api_token} \n Email: {email}')

  auth = HTTPBasicAuth(email, api_token)

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  return url, auth, headers

def split_list(list, limit):
    n = len(list)
    if n <= limit:
        return [list]
    else:
        return [list[:n//2], list[n//2:]]
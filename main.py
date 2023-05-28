import json
import sys
import logging
import requests
from input_converter import convert_markdown_to_dicts
from utils import get_jira_configs, split_list

logging.basicConfig(level=logging.INFO, format='s%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def main(input_file, url, auth, headers):

  dicts = convert_markdown_to_dicts(input_file)
  
  dict_parts = split_list(dicts, 50) # Jira API only allows 50 issues per request

  for part in dict_parts:
    payload = json.dumps({'issueUpdates': part})    
    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
    )
    logger.info(f'Response: \n {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))}')

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print("Usage: python main.py <input_file>")
      sys.exit(1)

  input_file = sys.argv[1]
  url, auth, headers = get_jira_configs()
  main(input_file, url, auth, headers)
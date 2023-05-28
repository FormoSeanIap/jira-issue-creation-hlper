import re
import os
import datetime
import yaml
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='s%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

load_dotenv()

asignee_id = os.getenv("SEAN_ID")

def convert_markdown_to_dicts(markdown_file_path):
    with open(markdown_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()

    with open('configs.yml', 'r') as file:
        configs = yaml.safe_load(file)


    dicts = []
    current_epic = ""
    for line in lines:
        if line.strip().replace('`', '') in configs['EPIC_IDS'].keys():
            current_epic = line.strip().replace('`', '') # remove backticks. e.g. '`CKAD`' -> 'CKAD'
            logger.info(f'found epic {current_epic}')
        else:
            match = re.match(r"^(【.*】)(.*)$", line)
            if match:
                summary = match.group(1) + match.group(2).strip()
                due_date = get_due_date(match.group(1))
                dict = {
                    "fields": {
                        "summary": summary,
                        "issuetype": {
                            "id": configs['ISSUE_TYPES']['Task']
                        },
                        "priority": {
                            "id": configs['PRIORITIES']['Medium']
                        },
                        "project": {
                            "id": configs['PROJECTS']['STUDY_2023']['id']
                        },
                        "duedate": due_date,
                        "assignee": {
                            "id": asignee_id
                        },
                        "customfield_10014": configs['EPIC_IDS'][current_epic], #epic link
                    }
                }
                dicts.append(dict)

    return dicts

def get_due_date(time_str):
    if "第" in time_str:
        week_num = int(re.search(r"第(\d+)週", time_str).group(1))
        month = int(re.search(r"(\d+)月", time_str).group(1))
        year = datetime.datetime.now().year
        first_day_of_month = datetime.datetime(year, month, 1)
        first_sunday_of_month = first_day_of_month + datetime.timedelta(days=(6 - first_day_of_month.weekday()))
        due_date = first_sunday_of_month + datetime.timedelta(weeks=week_num-1)
    else:
        month = int(re.search(r"(\d+)月", time_str).group(1))
        year = datetime.datetime.now().year
        last_day_of_month = datetime.datetime(year, month+1, 1) - datetime.timedelta(days=1)
        due_date = last_day_of_month
    return due_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    dicts = convert_markdown_to_dicts("input-example.md")
    logger.info(dicts)
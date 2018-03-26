import requests, json
from datetime import datetime
from config import *

'''
提取所有项目id
'''

post_url = 'http://10.98.0.2/datasys/pro/project/masterview/'


def get_all_project_id(project_type):
    project_list = []
    for i in range(30):
        form_data = {'status': project_type,
                     'category': 0,
                     'offset': i}
        content = requests.post(post_url, data=form_data, cookies=MY_COOKIE, headers=HEADERS).content.decode('utf-8')
        j = json.loads(content)
        details = j['data']['detail']
        if not details == []:
            for detail in details:
                project_list.append(detail['id'])
        else:
            print('end')
            break
    print(project_type, project_list)
    return project_list

# print(get_all_project_id(DOING_PROJECT))

import requests, json
from datetime import datetime
from config import *


'''
给定项目id，获取数据id
'''

now = str(datetime.now().date())


post_url = 'http://10.98.0.2/datasys/data/res/search/'


def get_project_detail(project_id):
    project = []
    for i in range(30):
        form_data = {"offset": i,
                     "limit": " 15",
                     "project": project_id,
                     "show_schedule": " 1", }
        content = requests.post(post_url, data=form_data, cookies=MY_COOKIE).content.decode('utf-8')
        j = json.loads(content)
        # print(j)
        details = j['data']['detail']
        d = {}
        if details == []:
            print('End')
            break
        else:
            print('正在获取第{}页'.format(i))
            for detail in details:
                try:
                    d['收录时间'] = now.replace('-', '/')
                    d['项目id'] = detail['project']
                    d['id'] = detail['id']
                    d['数据id'] = detail['raw']
                    d['版本'] = detail['version']
                    d['数据量'] = int(detail['pic_num'])
                    if detail['status'] == '3':
                        d['数据状态'] = '已完成'
                    elif detail['status'] == '2':
                        d['数据状态'] = '标注中'
                    else:
                        print('else')
                        d['数据状态'] = detail['status']
                    d['已标注'] = d['数据量'] - int(detail['data_dist']['nodone_1'])
                    d['已质检'] = int(detail['data_dist']['done_3'])
                    d['已验收'] = int(detail['data_dist']['done_99'])
                except:
                    continue
                project.append(d)
                d = {}
    return project

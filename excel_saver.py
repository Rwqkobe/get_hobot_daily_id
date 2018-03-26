from Data_id_getter import *
import xlwt

'''
把当日爬取的数据存储到excel中
'''


def save_as_excel(path, project_id_list):
    workbook = xlwt.Workbook(encoding='utf-8')
    for project_id in project_id_list:
        print('开始获取{}....'.format(project_id))
        project = get_project_detail(project_id)
        worksheet = workbook.add_sheet(project_id)
        j = 0
        try:
            for k, v in project[0].items():
                worksheet.write(0, j, k)
                j += 1

            for i in range(len(project)):
                j = 0
                for k, v in project[i].items():
                    if k == '收录时间':
                        worksheet.write(i + 1, j, v)
                    else:
                        worksheet.write(i + 1, j, v)
                    j += 1
        except:
            print(project_id, 'is None')
    workbook.save(path + now + '.xls')

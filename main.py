from datetime import datetime
import os
from excel_saver import *
from Project_id_getter import get_all_project_id

now = str(datetime.now().date())
PROJECT_ID_LIST = get_all_project_id(DOING_PROJECT)

root_path = 'D:\daily_data\\'  # + now + '\\'

save_as_excel(root_path, PROJECT_ID_LIST)

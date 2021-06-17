import os
import shutil
import pytest


def go_allure(is_clear=False):
    pro_path = os.path.dirname(__file__)
    xml_path = pro_path + "/output/report/xml/"
    html_path = pro_path + "/output/report/html/"
    command = "allure generate " + xml_path + " -o " + html_path + " --clean"
    os.popen(command)
    if is_clear:
        shutil.rmtree(xml_path)
        os.mkdir(xml_path)
        log_path = pro_path + "/output/log/"
        shutil.rmtree(log_path)
        os.mkdir(log_path)


def run(file_name):
    pro_dir = os.path.dirname(__file__)
    xml_path = pro_dir + "/output/report/xml/"
    pytest.main(
        ['-vs', file_name, '--alluredir', xml_path])  # 正式 "--reruns","2"
    go_allure()

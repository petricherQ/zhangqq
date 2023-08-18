import os
import pytest
import datetime


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == "__main__":
    today = datetime.datetime.today().date()
    path = os.path.dirname(__file__)
    report_path = "/root/.jenkins/workspace/IE_IMS/outputs/allure_results"
    pytest.main(["-m ims", "--alluredir={}".format(report_path), "--clean-alluredir"])


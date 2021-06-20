import pytest
# from pathlib import Path
# import os
import time
from utils import return_path


# Configure logging
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_setup(item):
#     config = item.config
#     logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
#     filename = Path('./pytest-logs', item._request.node.name + ".log")
#     logging_plugin.set_log_path(str(filename))
#     yield


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(return_path(log_name))

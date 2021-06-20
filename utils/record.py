import allure
import os
from .load_yaml import return_path


def record_text(title, body):
    allure.attach(body, title, allure.attachment_type.TEXT)


def record_jpg(title, image_name):
    with open(os.path.join(return_path("utils/images"), image_name), "rb") as f:
        allure.attach(f.read(), title, allure.attachment_type.JPG)

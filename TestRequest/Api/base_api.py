import logging

import allure
import requests


class BaseApi(object):
    CORPID = "ww266c99753fd0859b"
    SCORPSECRET = "OnAriV8rZcUbcUlM2i0BS-6mg6iBG0AwkisJp8e7hR0"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"
    PATH = ''

    def __init__(self):
        self.token = self.get_token()
        self.params = {"access_token": self.token}

    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params={"corpid": self.CORPID, "corpsecret": self.SCORPSECRET})
        return r.json().get("access_token")

    @allure.step("发送post请求")
    def post(self, variables):
        logging.info("发送post请求")
        logging.info(f"variables : {variables}")
        logging.info(f"url : {self.BASE_URL + self.PATH}")
        return requests.post(self.BASE_URL + self.PATH, json=variables, params=self.params)

    @allure.step("发送get请求")
    def get(self, params=None):
        if params is None:
            params = {}
        self.params.update(params)
        logging.info("发送get请求")
        logging.info(f"variables : {params}")
        logging.info(f"url : {self.BASE_URL + self.PATH}")
        return requests.get(self.BASE_URL + self.PATH, params=self.params)

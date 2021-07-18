import requests

access_token = "1oOQDzhT9AHrf1pdH6jKRmBfG1C-Oov29WQTyEvOoDMAkEKe4nIUSgpfvh6ua6pxl7j-QnZMaQnj4m7_PDWx0GJ855fHs2Oc8_GMBEum5Xo1-qem91OyFw4HWD5jHD1yhG_sqrguaeKdypVVv8McP5JtVM4znTKA2xNULP5sJmEbatzDcfyGn19KbUEzN6X7mJwp8uyYdwU5WXj2PfxnSg"


def test_request():
    corpid = "ww266c99753fd0859b"
    scorpsecret = "OnAriV8rZcUbcUlM2i0BS-6mg6iBG0AwkisJp8e7hR0"

    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r = requests.get(url, params={"corpid": corpid, "corpsecret": scorpsecret})
    print(r)
    print(r.json().get("access_token"))


def test_2():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={access_token}"
    print(requests.get(url).json())


if __name__ == '__main__':
    test_2()

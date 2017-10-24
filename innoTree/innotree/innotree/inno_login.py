import requests
import re
import time
import os.path
from PIL import Image
import http.cookiejar as cookielib
import time


header = {
    "agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "X-Requested-With": "X-Requested-With",
    "Host": "Host",
    "Referer": "https://www.innotree.cn/inno/database/totalDatabase"
}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')

try:
    session.cookies.load(ignore_discard=True)
except:
    print("Can not load Cookie")


login_url = "https://www.innotree.cn/ajax/uc/login"

def login(password,account):
    
import requests
import os
from .auth_v3_util import addAuthParams

def correct_writing(
    text,
    grade,
    title,
    modelContent,
    isNeedSynonyms,
    correctVersion,
    isNeedEssayReport,
    appKey="263b55112bed5896",
    appSecret="88EGsWtCx4vcdOKfkZV4F8PQTwIUqHBp"
):
    appKey = appKey or os.getenv("YOUDAO_APP_KEY", "你的appKey")
    appSecret = appSecret or os.getenv("YOUDAO_APP_SECRET", "你的appSecret")
    url = "https://openapi.youdao.com/v2/correct_writing_text"
    data = {
        "q": text,
        "grade": grade,
        "to": title,
        "modelContent": modelContent,
        "isNeedSynonyms": isNeedSynonyms,
        "correctVersion": correctVersion,
        "isNeedEssayReport": isNeedEssayReport
    }
    addAuthParams(appKey, appSecret, data)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    print("请求参数：", data)
    print("key:", appKey)
    print("secret:", appSecret)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    print("响应：", resp.json())
    return resp.json() 
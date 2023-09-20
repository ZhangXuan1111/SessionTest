#!/user/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import random
import calendar

import requests
import time
import hmac
from hashlib import sha256
import uuid

from textSession.initData import GlobalData


def getRandomTimestamp(month, day):
    # 给定一个日期，随机一个当天的时间戳 (单位/秒)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    startDate = datetime.datetime(2023, month, day, hour, minute, second)
    startTimestamp = int(random.uniform(1672502400, startDate.timestamp()))
    endTimestamp = startTimestamp + 400
    return startTimestamp, endTimestamp


def getTimestamp():
    # 获取当前时间戳 (header中的参数)
    now = time.time()
    now_timestamp = round(now)
    return now_timestamp


def getSignature(key, signatureContent):
    # 计算签名(header中的参数)
    key = key.encode('utf-8')
    message = signatureContent.encode('utf-8')
    sig = hmac.new(key, message, digestmod=sha256).hexdigest()
    return sig


def singleRequest(startTime, endTime, DialogueID, content):
    # 发单次请求
    timestamp = str(getTimestamp())
    Messages = [{} for _ in range(len(content))]
    for i in range(len(Messages)):
        Messages[i]["MessageID"] = str(DialogueID) + "-" + str(i)
        Messages[i]["MessageTime"] = str(startTime)
        Messages[i]["IsFirstMessage"] = False
        Messages[i]["IsLatestMessage"] = False
        Messages[i]["Content"] = content[i]
        if i % 2 == 0:
            Messages[i]["From"] = initData.From[0]
        else:
            Messages[i]["From"] = initData.From[1]
        if i == 0:
            Messages[i]["IsFirstMessage"] = True
        elif i == len(Messages) - 1:
            Messages[i]["IsLatestMessage"] = True
    body = initData.body
    body["Payload"]["DialogueID"] = str(DialogueID)
    body["Payload"]["DialogueStartTime"] = str(startTime)
    body["Payload"]["DialogueEndTime"] = str(endTime)
    body["Payload"]["Messages"] = Messages

    signingContent = json.dumps(body) + timestamp
    signature = getSignature(initData.appSecret, signingContent)
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Timestamp": timestamp,
        "Signature": signature
    }
    response = requests.post(url=initData.url, data=json.dumps(body), headers=headers)
    print(response.text)


def multiRequest():
    # 循环请求
    for m in range(1, 2):
        monthRange = calendar.monthrange(2023, m)[1]
        sessions_per_day = 33000
        for d in range(1, monthRange):
            for times in range(sessions_per_day):
                # 达到每天3.3w条会话的量级
                DialogueID = uuid.uuid4()
                result = getRandomTimestamp(m, d)
                startTimestamp = result[0]
                endTimestamp = result[1]
                if times < int(sessions_per_day * 0.35):
                    # 会话消息为1-10条
                    len_content = random.randint(0, 10)
                    content = initData.content_10[:len_content]
                    singleRequest(startTimestamp * 1000, endTimestamp * 1000, DialogueID, content)
                elif times > int(sessions_per_day * 0.5):
                    # 会话消息为 10-30条
                    len_content = random.randint(10, 30)
                    content = initData.content_30[:len_content]
                    singleRequest(startTimestamp * 1000, endTimestamp * 1000, DialogueID, content)

                else:
                    # 会话消息为 30-50条
                    len_content = random.randint(30, 50)
                    content = initData.content_50[:len_content]
                    singleRequest(startTimestamp * 1000, endTimestamp * 1000, DialogueID, content)


if __name__ == '__main__':
    initData = GlobalData()
    multiRequest()

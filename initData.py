#!/user/bin/env python3
# -*- coding: utf-8 -*-

class GlobalData:
    def __init__(self):
        self.StaffID = "mayday01"
        self.StaffName = 'mayday01'
        self.AppKey = '1687279621886766153'
        self.appSecret = '61c3e1f8abe32e2756415f1aa6690827'
        self.UserID = "700000364226-cloud"
        self.From = [
            {
                "id": self.StaffID,
                "type": "STAFF",
                "name": self.StaffName
            },
            {
                "id": "b2a1r0",
                "type": "CUSTOMER",
                "name": "test"
            },
        ]
        self.Users = [
            {
                "id": self.StaffID,
                "type": "STAFF",
                "name": self.StaffName
            },
            {
                "id": "b2a1r0",
                "type": "CUSTOMER",
                "name": "小张33"
            }
        ]
        self.url = 'https://pre.api-yunxiaowei.cloud.tencent.com/tqi/conversation-analysis/message/text-dialogue' \
                   '-quality'
        self.content_10 = ["你好", '111', '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢"]
        self.content_30 = ["你好", '111', '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好",
                           '111', '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好", '111',
                           '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢"]
        self.content_50 = ["你好", '111', '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好",
                           '111', '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好", '111',
                           '2222', '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好", '111', '2222',
                           '3333', '44444', '55555', '6666', '7777', '8888', "ok, 谢谢", "你好", '111', '2222', '3333',
                           '44444', '55555', '6666', '7777', '8888', "ok, 谢谢"]
        self.body = {
            "RequestSource": "ceshi",
            "UserID": self.UserID,
            "Metadata": {
                "AppKey": self.AppKey
            },
            "Payload": {
                "Users": self.Users,
                "SatisfactionResult": 4,
                "ChannelMark": "",
            }
        }

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/24 2:25 下午
# @Author  : chencheng
# @File    : test_001.py
# @Remark  : OAuth后客户端与后端同步信息 - /v1/sync


import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import os
# import util.reporyresult as cr
import modulefinder


@allure.feature('OAuth后客户端与后端同步信息 - /v1/sync')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-001' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.token = gl.get_value('Authorization')
        print(self.token)

        # 测试API地址
        self.url = '%ssync' % (self.ip)
        print(self.url)

        self.payloadData = {
            "followings": [{
            "id": "1496221756470001664",
            "name": "Layla",
            "username": "Layla95359365"
            }],
            "deleteExisting": False
            }

        self.payloadHeader = {
            'Content-Type': 'application/json',
            # 'Cookie': self.token
            'Authorization': self.token
        }

        # 打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request('POST', url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        # print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['code'] == 0




if __name__ == '__main__':
        pytest.main(['test_001.py'])



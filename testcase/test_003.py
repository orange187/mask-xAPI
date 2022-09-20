# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/31 2:55 下午
# @Author  : chencheng
# @File    : test_003.py
# @Remark  : 获取指定用户的混合时间线 - v1/user/timeline


import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import modulefinder


@allure.feature('获取指定用户的混合时间线 - v1/user/timeline')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-003' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.twitterId = gl.get_value('twitterId')
        self.token = gl.get_value('Authorization')
        #print(self.token)

        # 测试API地址
        self.url = '%suser/timeline' % (self.ip)
        print(self.url)

        self.payloadData = {
                "twitterId": self.twitterId
            }

        self.payloadHeader = {
            'Content-Type': 'application/json',
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
    pytest.main(['test_003.py'])



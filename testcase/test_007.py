# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 4:31 下午
# @Author  : chencheng
# @File    : test_007.py
# @Remark  : 获取指定用户的混合时间线 - v1/user/follow Twitter


import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import modulefinder


@allure.feature('获取指定用户的混合时间线 - v1/user/follow Twitter')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-007' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.accountId = gl.get_value('account_id')
        self.token = gl.get_value('Authorization')
        #print(self.token)

        # 测试API地址
        self.url = '%sdiscover/suggestUsers' % (self.ip)
        print(self.url)

        self.payloadData = {
            }

        self.payloadHeader = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        # 打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request('get', url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        # print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['code'] == 0




if __name__ == '__main__':
    pytest.main(['test_007.py'])


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 12:11 下午
# @Author  : chencheng
# @File    : test_009.py
# @Remark  : 关注指定用户或实体 - v1/user/follow


import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import modulefinder


@allure.feature('关注指定用户或实体 - v1/user/follow')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-009' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.token = gl.get_value('Authorization')

        # 测试API地址
        self.url = '%suser/follow?toObjectId=177604511&type=twitter&toObjectValue=yisiliu' % (self.ip)
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

        r = requests.request('put', url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        # print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['code'] == 0




if __name__ == '__main__':
    pytest.main(['test_009.py'])

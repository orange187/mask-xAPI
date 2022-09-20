# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/31 3:32 下午
# @Author  : chencheng
# @File    : test_005.py
# @Remark  : 绑定新钱包地址到当前用户v1/wallet


import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import modulefinder


@allure.feature('绑定新钱包地址到当前用户v1/wallet')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-005' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.accountId = gl.get_value('account_id')
        self.token = gl.get_value('Authorization')
        self.address = gl.get_value('address')
        #print(self.token)

        # 测试API地址
        self.url = '%swallet/' % (self.ip)
        print(self.url)

        self.payloadData = {
                # "accountId": self.accountId,
                "wallets": [{
                    "address": self.address,
                    "blockchain": "ethereum"
                }]
            }

        self.payloadHeader = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        # 打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request('PUT', url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        # print(r.json())
        ul.log.logger.info(r)


        # 断言
        assert r.json()['code'] <= 206




if __name__ == '__main__':
    pytest.main(['test_005.py'])





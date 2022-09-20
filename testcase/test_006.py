# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/31 3:21 下午
# @Author  : chencheng
# @File    : test_006.py
# @Remark  : 获取当前用的的指定钱包地址 - v1/wallet

import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import modulefinder


@allure.feature('获取当前用的的指定钱包地址 - v1/wallet')
class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize()
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-006' % (self.lab)
        self.ip = gl.get_value('ApiIp')
        self.accountId = gl.get_value('account_id')
        self.token = gl.get_value('Authorization')
        self.address = gl.get_value('address')
        #print(self.token)

        # 测试API地址
        self.url = '%swallet/?address=0x934b510d4c9103e6a87aef13b816fb080286d649' % (self.ip)
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

        print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['code'] == 0
        if r.json()['data'][0]['address'] == self.address:
            assert r.json()['data'][0]['address'] == self.address
            print('从第一位查找出')
        elif r.json()['data'][1]['address'] == self.address:
            assert r.json()['data'][1]['address'] == self.address
            print('从第二位查找出')
        else:
            print("未查找出改钱包地址")




if __name__ == '__main__':
    pytest.main(['test_006.py'])


#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

import requests


class ApiSDK:
    def __init__(self,base_url, api_id, api_key):
        """
        初始化
        :param base_url: 基础URL，通常以"api/api/"
        :param api_id: 授权的apiId
        :param api_key: 授权的apiKey
        """
        self.BASE_URL = base_url
        self.API_ID = api_id
        self.API_KEY = api_key

    def queryData(self, id, begin=0, length=10, params=None, params_check=None):
        """
        查询数据
        :param id: API接口ID
        :param begin: 起始编号
        :param length: 数据长度
        :param params: 参数（JSON格式）
        :param params_check: 参数生效配置（JSON格式）
        :return: 返回值的text格式
        """

        if params is None:
            params = {}
        if params_check is None:
            params_check = {}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self.BASE_URL + 'queryData'
        data = {
            'parms': json.dumps(params),
            'parmsCheck': json.dumps(params_check),
            'id': id,
            'begin': begin,
            'length': length,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY
        }
        res = requests.post(url, data=data, headers=headers)
        return res.text

    def executeData(self, id, params=None):
        """
        更新数据
        :param id: API接口ID
        :param params: 参数（JSON格式）
        :return:
        """

        if params is None:
            params = {}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self.BASE_URL + 'executeData'
        data = {
            'parms': json.dumps(params),
            'id': id,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY
        }
        res = requests.post(url, data=data, headers=headers)
        return res.text

    def uploadFile(self, id, file_path,v_parms):
        """
        上传文件
        :param id: API接口ID
        :param file_path: 文件存放路径
        :return:
        """

        url = self.BASE_URL + 'addFiles'
        files = [
            ('form1', open(file_path, 'rb'))
        ]
        params = {
            'id': id,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY,
	    'parms':v_parms
        }
        res = requests.post(url, params=params, files=files)
        return res.text

    def downloadFile(self, id, file_id):
        """
        下载文件
        :param id:  API接口ID
        :param file_id: 文件ID
        :return: 文件流
        """
        url = self.BASE_URL + 'getFileById'

        params = {
            'id': id,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY,
            'fileId': file_id
        }
        res = requests.post(url, params=params)
        return res.text

    def deleteFiles(self, id, file_id_list):
        """
        批量删除文件
        :param id: API接口ID
        :param file_id_list: 文件ID数组
        :return:
        """
        if file_id_list is None:
            file_id_list = []

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self.BASE_URL + 'deleteFiles'
        data = {
            'fileIds': json.dumps(file_id_list),
            'id': id,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY
        }
        res = requests.post(url, data=data, headers=headers)
        return res.text

    def queryFileByParm(self, id, begin,length,beginTime,endTime,file_id_list):
        """
        根据文件参数，获取文件列表
        :param id: API接口ID
        :param file_id_list: 文件ID数组
        :return:
        """
        if file_id_list is None:
            file_id_list = []

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self.BASE_URL + 'deleteFiles'
        data = {
            'fileIds': json.dumps(file_id_list),
            'id': id,
            'apiId': self.API_ID,
            'apiKey': self.API_KEY,
	    'begin':begin,
            'length':length,
            'benginTime':beginTime,
            'endTime':endTime
        }
        res = requests.post(url, data=data, headers=headers)
        return res.text

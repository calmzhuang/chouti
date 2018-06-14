#!/usr/bin/env python

# encoding: utf-8

'''

@author: calmzhuang

@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.

@contact: calmzhuang@163.com

@software: garner

@file: modeltool.py

@time: 2018/6/14 14:40

@desc:

'''

from  app01 import models

#创建model数据查询类
class ModelSelect():

    #创建热点查询方法
    @staticmethod
    def hot_select(num):
        size = 5
        start_num = (num-1) * size
        end_num = (num) * size
        datalist = models.AllHot.objects.all().order_by('-storage_time')[start_num: end_num]
        return datalist
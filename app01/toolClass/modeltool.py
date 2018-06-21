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

from app01 import models
from django.db.models import F, Q

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

    #获取当前用户点赞文章
    @staticmethod
    def user_praise(user):
        allhot_id = user.user_praise.values('id')
        return allhot_id

    #查询是否已经点赞该热点
    @staticmethod
    def praise(hotId, username):
        have_praise = models.AllHot.objects.get(id=hotId).praise_user.filter(username=username)
        return have_praise

    # 增加该用户的点赞记录
    @staticmethod
    def praise_add(hotId, username):
        allhot = models.AllHot.objects.get(id=hotId)
        user = models.UserInfo.objects.get(username=username)
        allhot.praise_user.add(user)
        models.AllHot.objects.filter(id=hotId).update(praises=F('praises')+1)

    #删除该用户的点赞记录
    @staticmethod
    def praise_delete(hotId, username):
        allhot = models.AllHot.objects.get(id=hotId)
        user = models.UserInfo.objects.get(username=username)
        allhot.praise_user.remove(user)
        models.AllHot.objects.filter(id=hotId).update(praises=F('praises')-1)
#!/usr/bin/env python

# encoding: utf-8

'''

@author: calmzhuang

@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.

@contact: calmzhuang@163.com

@software: garner

@file: show_list.py

@time: 2018/5/31 10:39

@desc:

'''
from django import template

register = template.Library()

@register.filter()
def list(cla, dat):
    strs = "<tr>"
    for item in cla:
        strs += "<th>" + str(item) + "</th>"
    for item in dat:
        strs += "</tr><tr>"
        strs += "<td>" + str(item.get('id')) + "</td>"
        strs += "<td>" + str(item.get('name')) + "</td>"
        if item.get('email'):
            strs += "<td>" + str(item.get('email')) + "</td>"
        if item.get('classes__name'):
            strs += "<td>" + str(item.get('classes__name')) + "</td>"
        strs += "<td><a href=\"javascript:void(0)\">编辑</a>|<a href=\"javascript:void(0)\">删除</a></td>"
    strs +="</tr>"
    return strs

'''
@register.simple_tag()
def list(cla, dat):
    strs = "<tr>"
    for item in cla:
        strs += "<th>" + str(item) + "</th>"
    strs += "</tr><tr>"
    for item in dat:
        strs += "<td>" + str(item.id) + "</td>"
        strs += "<td>" + str(item.name) + "</td>"
        strs += "<td><a href=\"javascript:void(0)\">编辑</a>|<a href=\"javascript:void(0)\">删除</a></td>"
    strs +="</tr>"
    return strs
'''
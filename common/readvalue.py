#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm
from utils.logger import log


class ElementValue(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if not data:
          raise ArithmeticError("{}中根本不存在关键字：{}".format(self.file_name, item))
        return data

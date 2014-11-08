# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import os.path as path

import yaml

from ..utils import to_snake_case


class AttrDict(dict):

    def __init__(self, *args, **kwgs):
        super(AttrDict, self).__init__(*args, **kwgs)
        self.__dict__ = self
        for key, value in self.iteritems():
            if isinstance(value, dict) and not isinstance(value, AttrDict):
                self[key] = AttrDict(value)


class GUI(object):

    def __init__(self, container_name):
        file_path = path.join(path.dirname(__file__), 'components',
                              '%s.yml' % to_snake_case(container_name))

        components = yaml.load(open(file_path))
        components = AttrDict(components)

        for key in components:
            if components[key].get('parent'):
                components[key]['parent'] = components[components[key]['parent']]

        self.__dict__.update(components)

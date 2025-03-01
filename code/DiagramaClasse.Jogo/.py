#!/usr/bin/python
# -*- coding: utf-8 -*-

from Interface3 import Interface3
from Interface5 import Interface5


class (Interface3, Interface5):
    def __init__(self):
        self.name = None
        self.surf = None
        self.rect = None
        self.Attribute1 = None
        self.Part1 = None

    def move(self, ):
        pass

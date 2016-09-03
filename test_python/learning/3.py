#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'LH Liu'

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

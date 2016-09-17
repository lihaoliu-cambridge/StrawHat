# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('E:\\PythonProject\\Work\\work_3\\dake_recommendation\\test\\recmd_results.csv', sep='\t', encoding='utf-8', dtype=np.unicode_)
b = a.loc[:, ['video_account_id', 'video_account_nickname', 'watch_num_avg', 'score_watch_num_avg', 'engagement',
              'score_engagement', 'category_max_weight', 'score_category_max_weight', 'total_score']]

col_name = ['id', 'st']
c = pd.read_csv('E:\\PythonProject\\Work\\work_3\\dake_recommendation\\test\\test_1.txt', names=col_name, encoding='utf-8', dtype=np.unicode_)
d = pd.DataFrame(c['id'][c['st'] == '应约'].value_counts())
d['video_account_id'], d.index = d.index, range(d.shape[0])

print b, d
print type(b['video_account_id'][0])
print type(d['video_account_id'][0])
e = pd.merge(b, d, how='left', on='video_account_id')
print e


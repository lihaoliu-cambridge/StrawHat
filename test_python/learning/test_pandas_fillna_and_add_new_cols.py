import pandas as pd
import os

col_name = ['id', 'name', 'age', 'money']
items = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test_1.txt'), encoding='utf-8', names=col_name, sep=' ')

print items

items.fillna({'name': 'allen', 'age': 18}, inplace=True)
items['score'] = items['age'] + items['money']*0.5
print items
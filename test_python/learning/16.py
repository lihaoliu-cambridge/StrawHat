import datetime

t = {'year': '2013', 'month': '9', 'day': '30', 'hour': '16', 'minute': '45', 'second': '2'}
print datetime.datetime(**{k: int(v) for k, v in t.items()}).strftime('%Y-%m-%d %H:%M:%S')

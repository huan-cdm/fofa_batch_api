#!/usr/bin/env python3
import os
import time
from config import batchfofasleeptime

#读取文件行数
num_value = os.popen('bash /root/batch_fofa_api/fofa_lib.sh target_num').read()
print("去重前文件行数："+num_value)
time.sleep(2)
os.popen('bash /root/batch_fofa_api/fofa_lib.sh uniqfofa_batch')
num_value1 = os.popen('bash /root/batch_fofa_api/fofa_lib.sh target_num').read()
print("去重后文件行数："+num_value1)

fofa_file = open('/root/batch_fofa_api/target.txt',encoding='utf-8')
try:
    for line in fofa_file.readlines():
        ip_domain = os.popen('python3 /root/batch_fofa_api/fofa_lib.py'+' '+line).read()
        print(ip_domain)
        time.sleep(batchfofasleeptime)
except:
    pass

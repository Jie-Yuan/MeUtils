#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : crontabe_demo
# @Time         : 2021/1/24 12:08 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : https://www.cnblogs.com/mysql-dba/p/13565057.html
# https://github.com/guige/python-crontab/blob/master/crontab.py


from meutils.pipe import *

# 基本信息
with CronTab(user='yuanjie') as cron:
    cron | xlist  # cron.crons
    cron.commands | xlist
    cron.comments | xlist

# 增加一个crontab任务
comment = 'comment'  # crontab id
with CronTab(user='yuanjie') as cron:
    # cron.crons
    job = cron.new(command='echo hello_world', comment=comment, pre_comment=True)
    job.minute.every(1)

# 删除一个crontab任务
with CronTab(user='yuanjie') as cron:
    jobs = cron.find_comment('job')
    # cron.find_command('echo hello_world')
    # cron.find_time('* * * * *')
    for job in jobs:
        cron.remove(job)

# 修改任务
with CronTab(user='yuanjie') as cron:
    jobs = cron.find_comment('job')
    for job in jobs:
        job.set_command("python bakcup.py --port=3306")
        # job.set_comment
        # job.setall # 修改调度时间

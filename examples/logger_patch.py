#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : logger_patch
# @Time         : 2021/1/19 8:53 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from meutils.pipe import logger, logger_patch, timer, time

logger.info("x")

logger = logger_patch(__file__)
logger.info("xx")

with timer() as t:
    time.sleep(3)

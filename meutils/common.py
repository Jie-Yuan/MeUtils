#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : common
# @Time         : 2020/11/12 11:42 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import os
import gc
import re
import sys
import time

import joblib
import datetime
import pickle
import operator
import inspect
import requests
import resource
import socket
import warnings
import fire
import subprocess

import numpy as np
import pandas as pd

from typing import *
from PIL import Image
from pathlib import Path
# from loguru import logger
from meutils.log_utils import logger, logger_patch
from meutils.crontab import CronTab

from tqdm.auto import tqdm
from contextlib import contextmanager
from functools import reduce, lru_cache
from collections import Counter, OrderedDict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

try:
    import simplejson as json
except ImportError:
    import json

warnings.filterwarnings("ignore")
tqdm.pandas()

# args
get_args = lambda func: inspect.getfullargspec(func).args


# run time
@contextmanager
def timer(task="timer"):
    """https://www.kaggle.com/lopuhin/mercari-golf-0-3875-cv-in-75-loc-1900-s
        with timer() as t:
            time.sleep(3)
    """

    logger.info(f"{task} started")
    s = time.time()
    yield
    e = time.time()
    logger.info(f"{task} done in {e - s:.3f} s")


# limit memory
def limit_memory(memory=16):
    """
    :param memory: 默认限制内存为 16G
    :return:
    """
    rsrc = resource.RLIMIT_AS
    # res_mem=os.environ["RESOURCE_MEM"]
    memlimit = memory * 1024 ** 3
    resource.setrlimit(rsrc, (memlimit, memlimit))
    # soft, hard = resource.getrlimit(rsrc)
    logger.info("memory limit as: %s G" % memory)


def magic_cmd(cmd='ls'):
    status, output = subprocess.getstatusoutput(cmd)
    logger.info(f"CMD: {cmd}")
    logger.info(f"CMD Output: {status}")
    return status, output.split('\n')


def download(url, rename=None):
    cmd = f"wget {url}"
    if rename:
        cmd += f" -O {rename}"

    os.system(cmd)


if __name__ == '__main__':
    with timer() as t:
        time.sleep(3)

    status, output = magic_cmd('ls')
    print(status, output)

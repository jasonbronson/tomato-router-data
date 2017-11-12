#!/usr/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

username = os.environ.get("username")
password = os.environ.get("password")
httpid = os.environ.get("httpid")
ip = os.environ.get("ip")
redishost = os.environ.get("redishost")
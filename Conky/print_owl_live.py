#!/usr/bin/python3

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

from os.path import exists
import os

COLOR1 = '${color0}'
COLOR2 = '${color1}'
COLOR_GREEN = '${color2}' #green
COLOR_RED = '${color3}' #red

if exists("OWLLIVE"):
  print('%s%s' % (COLOR_GREEN, "Live"));
else:
  print('%s%s' % (COLOR_RED, "Offline"));

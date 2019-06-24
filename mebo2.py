'''
Created on 24.06.2019

@author: User
'''

import subprocess
import shlex
import re
import os
import time
import platform
import json
import sys
import base64
import random
import datetime
import traceback
import thread
import copy
import argparse
import uuid
import urllib2
import tempfile
import getpass
import glob

parser = argparse.ArgumentParser(description='Mebo Python 27')
parser.add_argument('--robotid', dest='robot_id', type=int, default=0)
parser.add_argument('--cameraid', dest='camera_id', type=int, default=0)
parser.add_argument('--debug', dest='debug', type=bool, default=False)

commandArgs = parser.parse_args()

print "| "
print "| "
print "| MEBO PYTHON 2.7"
print "| BETA VERSION - MEBO CLIENT"
print "| "
print "| "

print "> Following args got loaded: " + commandArgs
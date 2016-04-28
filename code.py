#-*-encoding: utf-8 -*-
# ipython notebook --ip 0.0.0.0 --port 9999
#import mathplotlib.
#%matplotlib inline 이걸 써줘야 아이파이썬에서 가능
#import networkx as nx

import numpy as np
import re
import os.path
import csv
from scipy.stats import rankdata
import scipy.stats
import time

#이제는 기초계산 모듈들을 가지고 온다. 
def templets():
	start_time = time.time()
	temp_start_time = time.time()
	print "=============	Reading raw data start 	=============="
	print "=============	Reading raw data end 	=============="
	print("Reading raw data takes %s seconds" % (time.time() - temp_start_time))
	temp_start_time = time.time()



#네트워크 관련 자료부터 시작한다. 




#-*-encoding: utf-8 -*-
# ipython notebook --ip 0.0.0.0 --port 9999
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


def temp():
	data_in = "../2.processed_data/all_id_year_title.txt"
	f_in = open(data_in, "r")
	lines = f_in.readlines()

	year_last = 0
	year_first = 9999
	for line in lines:
		parse = line.split("|")
		year = int(parse[1])
		if (year > year_last):
			year_last = year
		if (year < year_first):
			year_first = year

	print year_last
	print year_first

#네트워크 관련 자료부터 시작한다. 

def cite_year_divider(in_path, out_path):
	#연도별로 인용 링크를 나누어준다.
	f_in_1 = open(in_path + "all_cite.txt","r")
	f_in_2 = open( in_path + "all_id_year.txt", "r")

	t_year = f_in_2.readlines()
	t_cite = f_in_1.readlines()

	f_in_1.close()
	f_in_2.close()
	item_id = {}

	for i in t_year:
		t = i.split(",")
		t1 = int(t[0])
		t2 = int(t[1])
		if (t2 != -1):
			item_id[t1] = t2


	f_error = open("cite_year_divider_error.txt","w")
	for i in range(1936, 2014):
		print i
		f_out = open("./divided_by_year_data2/" +str(i) + "_cite.csv","w")
		f_out.write("Source,Target\n")
		for j in t_cite:
			tt = j.split(",")
			id1 = int(tt[0])
			id2 = int(tt[1])
			try:
				if (item_id[id1] <= i and item_id[id2] <=i):
					f_out.write(str(id1) + ","+ str(id2) + "\n")
			except:
				f_error.write(str(id1) + "," +str(id2)+"\n")
		f_out.close()
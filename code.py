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

def data_descriptor(in_path, out_path):

	#입력받는 부분
	f_in_1 = open(in_path + "all_cite.txt","r")
	f_in_2 = open(in_path + "all_id_year_title.txt", "r")

	f_out_source = open(out_path + "source_count.txt", "w")
	f_out_target = open(out_path + "target_count.txt", "w")

	id_year_title = f_in_2.readlines()
	cite = f_in_1.readlines()
	f_in_1.close()
	f_in_2.close()

	print "all item size:\t" + str(len(id_year_title))


	#계산하는 부분 
	item = {}
	all_item = {}
	for i in id_year_title:
		parse = i.split("|")
		item_id = parse[0]
		year = int(parse[1])
		if (year not in item):
			item[item_id] = year

	source_count = {}
	target_count = {}

	print "all relation size:\t" + str(len(cite))
	for i in cite:
		parse = i.split(",")
		source = parse[0].strip()
		target = parse[1].strip()
		if (source not in source_count):
			source_count[source] = 0
		if (target not in target_count):
			target_count[target] = 0

		source_count[source] = source_count[source] + 1
		target_count[target] = target_count[target] + 1

	print "all_source:\t" + str(len(source_count))
	print "all_target:\t" + str(len(target_count))

	#출력하는 부분

	for i in source_count:
		f_out_source.write(str(source_count[i]) + "\n")
		if i < 10000:
			continue
	for i in target_count:
		if i < 10000:
			continue
		f_out_target.write(str(target_count[i]) + "\n")

def plt_hist(x, title):
	import numpy as np
	import matplotlib
	import matplotlib.pyplot as plt

	matplotlib.use('Agg')

	plt.hist(x, 5)

	plt.xlabel('cited_count')
	plt.ylabel('number_of_data')
	plt.title('Hist_of_'+ title)
	plt.axis([0, 200,10000,1050000])

	plt.grid(True)
	plt.show()

def data_descriptor_2(in_path, out_path):
	import matplotlib.pyplot as plt

	#입력받는 부분 
	f_in_source = open(in_path + "source_count.txt", "r")
	f_in_target = open(in_path + "target_count.txt", "r")

	source = map(int, f_in_source.readlines())
	target = map(int, f_in_target.readlines())
	target.remove(938038)

	print "max source:\t" +str(max(source))
	print "ave source:\t" +str(float(sum(source))/float(len(source)))
	print "size source:\t" +str(len(source))
	print "max target:\t" +str(max(target))
	print "ave target:\t" +str(float(sum(target))/float(len(source)))
	print "size target:\t" +str(len(source))


	plt_hist(source, "Source")



def cite_data_refining(in_path, out_path):
	f_in_1 = open(in_path + "all_cite.txt","r")
	f_in_2 = open( in_path + "all_id_year_title.txt", "r")

	id_year_title = f_in_2.readlines()
	cite = f_in_1.readlines()

	f_in_1.close()
	f_in_2.close()
	item = {}

	for i in id_year_title:
		parse = i.split("|")
		item_id = parse[0].strip()
		year = int(parse[1])
		if (year not in item):
			item[item_id] = year

	f_out_cited_count_in_the_title_list = open("../2.processed_data/cited_count_in_the_title_list.txt","w")
	f_out_cited_count_out_the_title_list = open("../2.processed_data/cited_count_out_the_title_list.txt","w")

		for j in cite:
			parse = j.split(",")
			source = parse[0].strip()
			target = parse[1].strip()
			
		if (target not in item):
			f_out_cited_count_out_the_title_list.write(j)
		else:
			f_out_cited_count_out_the_title_list.write(j)

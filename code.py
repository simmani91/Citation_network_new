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

def cite_year_divider(in_path, out_path):
	#연도별로 인용 링크를 나누어준다.
	#363초 걸림 
	start_time = time.time()
	temp_start_time = time.time()
	print "=============	cite_year_divider start		=============="
	print "=============		from 1951 to 2015		=============="
	f_in_1 = open(in_path + "all_cite.txt","r")
	f_in_2 = open(in_path + "all_id_year_title.txt", "r")

	t_year = f_in_2.readlines()
	t_cite = f_in_1.readlines()

	f_in_1.close()
	f_in_2.close()
	item_id = {}

	for i in t_year:
		t = i.split("|")
		item = t[0].strip()
		year = int(t[1])
		item_id[item] = year

	f_error = open("cite_year_divider_error.txt","w")
	for i in range(1951, 2016):
		print i
		f_out = open(out_path +str(i) + "_cite.csv","w")
		f_out.write("Source,Target\n")
		for j in t_cite:
			tt = j.split(",")
			source = tt[0].strip()
			target = tt[1].strip()
			if (source in item_id and target in item_id):
				if (item_id[source] <= i and item_id[target] <=i):
					f_out.write(str(source) + ","+ str(target) + "\n")
			else:
				print "error"
				f_error.write(str(target) + "," +str(target)+"\n")
		f_out.close()

	print "=============	cite_year_divider end	=============="
	print("takes %s seconds" % (time.time() - temp_start_time))
	temp_start_time = time.time()

def make_net_initialize(in_path):
	#연도별 중심성을 저장하는 Dump를 초기화해주는 코드라 한다. 
	global Dump
	f_in = open(in_path + "2015_cite.csv", "r")
	lines = f_in.readlines()
	
	for line in lines:
		data = line.split(",")
		Dump[data[0].strip()] = {}
		Dump[data[1].strip()] = {}

def make_net(centrality_name, in_path, out_path):
	#네트워크를 만들고 Centurality를 계산하고 저장할 것이다.
	import networkx as nx
	global Dump
	Dump = {}
	make_net_initialize(in_path)
	start_time = time.time()
	temp_start_time = time.time()

	print "=============		make_net start:" + centrality_name + "		=============="
	print "=============		from 1951 to 2015		=============="

	for year in range(1951, 2016):
		print year
		f_in = open(in_path + str(year) + "_cite.csv","r")
		lines = f_in.readlines()
		f_in.close()
		edge_list = []

		for line in lines:
			data = line.split(",")
			data_tuple = (data[0].strip(), data[1].strip())
			edge_list.append(data_tuple)

		Net = nx.DiGraph(edge_list)
		Cen_in = {}
		if (centrality_name == "in_degree"):
			Cen_in = nx.in_degree_centrality(Net)
		elif (centrality_name == "degree"):
			Cen_in = nx.degree_centrality(Net)
		elif (centrality_name == "eigenvector"):
			Cen_in = nx.eigenvector_centrality_numpy(Net)
		elif (centrality_name == "katz"):
			Cen_in = nx.katz_centrality(Net)
		elif (centrality_name == "pagerank"):
			Cen_in = nx.pagerank(Net)
		elif (centrality_name == "communicability"):
			Net = nx.Graph(edge_list)
			Cen_in = nx.communicability_centrality(Net)
		elif (centrality_name == "load"):
			Cen_in = nx.load_centrality(Net)
		
		for j in Cen_in:
			key = j
			val = Cen_in[j]
			Dump[key][year] = val

	#저장하는 코드 
	f_out = open(out_path + centrality_name +"_centrality.csv", "w")
	for key in Dump:
		line = str(key)
		for year in range(1951, 2016):
			data = Dump[key].get(year, 0)
			line = line + ","+ str(data)
		line = line + "\n"
		f_out.write(line)
	f_out.close()

	print "=============		make_net end			=============="
	print(centrality_name + "takes %s seconds" % (time.time() - temp_start_time))
	temp_start_time = time.time()


def make_cited_count_sheet(in_path, out_path):
	start_time = time.time()
	temp_start_time = time.time()

	print "=============		make_cited_count_sheet		=============="
	print "=============		from 1951 to 2015		=============="

	global Dump
	Dump = {}

	make_net_initialize(in_path)

	for year in range(1951, 2016):
		print year
		f_in = open( in_path + str(year) + "_cite.csv", "r")
		lines = f_in.readlines()
		edge_list = []
		for line in lines:
			data = line.split(",")
			key = data[1].strip()
			Dump[key][year] = Dump[key].get(year,0) + 1

	f_out = open(out_path + "cited_count.csv", "w")
	for key in Dump:
		line = str(key)
		for year in range(1951, 2016):
			data = Dump[key].get(year, 0)
			line = line + ","+ str(data)
		line = line + "\n"
		f_out.write(line)
	print "=============		make_cited_count_sheet		=============="
	print(centrality_name + "takes %s seconds" % (time.time() - temp_start_time))
	temp_start_time = time.time()

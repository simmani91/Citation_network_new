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

class Item:
	def __init__(self):
		self.item_id = ''
		self.title = 'NULL'
		self.year = -1
		self.publisher = 'NULL'
		self.author = []
		self.cite = []
		self.abstract = ""

def save_customized_data(item,out_path):
	#새로운 processed 데이터를 만들때 이곳에서 작업하면 된다. 
	global f_out_id_year_title		
	global f_out_cited			
	global f_out_publisher		
	global f_out_author 			
	global f_out_id_year_abstract	

def save_processed_data(item,out_path):
	#열심히 저장하는 공간
	global f_out_id_year_title		
	global f_out_cited			
	global f_out_publisher		
	global f_out_author 			
	global f_out_id_year_abstract	
	global check

	if item.year <1900:
		if item.year in check :
			check[item.year] = check[item.year] + 1
		else:
			check[item.year] = 1
		"""
		print item.year
		print item.item_id
		print item.title
		
		print item.publisher
		print item.author
		print item.cite
		print item.abstract
		"""

	if item.year == 11:
		print item.item_id
		print item.title		
	f_out_id_year_title.write(item.item_id.strip()+"|"+str(item.year)+"|"+item.title.strip()+"\n")
	f_out_publisher.write(item.item_id.strip()+"|"+str(item.year)+"|"+item.publisher.strip()+"\n")
	f_out_id_year_abstract.write(item.item_id.strip()+"|"+str(item.year)+"|"+item.abstract.strip() + "\n")

	if (len(item.author) > 0):
		f_out_author.write(item.item_id.strip()+"|"+str(item.year)+"|")
		for author in item.author[:-1]:
			f_out_author.write( author.strip()+ ",")
		f_out_author.write(item.author[-1].strip()+"\n")

	if (len(item.cite) > 0):
		for c in item.cite:
			f_out_cited.write(item.item_id.strip()+","+c.strip()+"\n")

def processed_data(in_path, out_path):
	start_time = time.time()
	temp_start_time = time.time()

	#파일을 입력받는다. 2016년 4월 최신버전 기준 2GB정도 된다.
	print "=============	Reading raw data start 	=============="

	f_in = open(in_path,"r")
	lines = f_in.readlines()
	f_in.close()

	print "=============	Reading raw data end 	=============="
	print("Reading raw data takes %s seconds" % (time.time() - temp_start_time))
	temp_start_time = time.time()

	#한줄씩 보며 데이터를 읽어들이고 저장한다. 
	print "=============	Parsing raw data start 	=============="
	#출력할 경로를 지정하여준다. 
	global f_out_id_year_title
	global f_out_cited
	global f_out_publisher
	global f_out_author
	global f_out_id_year_abstract
	global check
	check = {}
	f_out_id_year_title = open(out_path +"all_id_year_title.txt","w")
	f_out_cited = open(out_path +"all_cite.txt","w")
	f_out_publisher = open(out_path +"all_publisher.txt","w")
	f_out_author = open(out_path +"all_author.txt","w")
	f_out_id_year_abstract =	open(out_path +"all_id_year_abstract.txt","w")


	item = Item()
	print len(lines)
	i = 0
	for line in lines:
		i = i +1
		if (i%1000000 == 0 ):
			print str(i) + " / " + str(len(lines)) + " (" + str(int((float(i)/float(len(lines)))*100)) + " %)"

		if len(line) > 1:
			flag = line[1]
			if (flag == "*"):
				item.title = line[2:].strip()
			elif(flag == "@"):
				item.author = line[2:].split(",")
			elif(flag == "t"):
				item.year = int(line[2:].strip())
			elif(flag == "c"):
				item.publisher = line[2:]
			elif(flag == "i"):
				item.item_id = line[6:].strip()
			elif(flag == "%"):
				item.cite.append(line[2:])
			elif(flag == "!"):
				item.abstract = line[2:]
				save_processed_data(item,out_path)
				save_customized_data(item,out_path)
				item = Item()
	print "=============	Parsing raw data end 	=============="
	print("Parsing raw data takes %s seconds" % (time.time() - temp_start_time))
	for i in check:
		print str(i) + ": "+ str(check[i])

	temp_start_time = time.time()



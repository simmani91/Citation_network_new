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
				item.title = line[2:].strip().replace("\t"," ")
			elif(flag == "@"):
				item.author = line[2:].split(",")
			elif(flag == "t"):
				item.year = int(line[2:].strip())
			elif(flag == "c"):
				item.publisher = line[2:].strip().replace("\t"," ")
			elif(flag == "i"):
				item.item_id = line[6:].strip()
			elif(flag == "%"):
				item.cite.append(line[2:])
			elif(flag == "!"):
				item.abstract = line[2:].replace("\t"," ")
				#임시로 막아놓음
				save_processed_data(item,out_path)
				#save_customized_data(item,out_path)

				item = Item()
	print "=============	Parsing raw data end 	=============="
	print("Parsing raw data takes %s seconds" % (time.time() - temp_start_time))

	"""
	f_out = open("error_title.txt", "w")
	for i in check:
		f_out.write(str(i.replace("\t"," ")) + "\n")
	"""
	temp_start_time = time.time()


def check_year_error():
	#연도가 이상한 데이터를 추출한것을 하나하나 검사하여 쓸 수 있는데이터(연도 추측가능)는 연도를 추가하고 
	#쓸수 없는 데이터는 no relation에 적어놓는다. 
	data_in_id_year = "../2.processed_data/all_id_year_title.txt"
	data_in_cite = "../2.processed_data/all_cite.txt"
	all_id_year =  {}
	all_cite = {}


	f_in_id_year = open(data_in_id_year, "r")
	f_in_cite = open(data_in_cite, "r")
	f_in_error = open("error_title.txt", "r")

	lines = f_in_id_year.readlines()
	f_in_id_year.close()

	for line in lines:
		parse = line.split("|")
		item_id = parse[0]
		year = int(parse[1])

		all_id_year[item_id] = year


	lines = f_in_cite.readlines()
	f_in_cite.close()

	for line in lines:
		parse = line.split(",")
		item_id_A = parse[0].strip()
		item_id_B = parse[1].strip()

		if (item_id_A not in all_cite):
			all_cite[item_id_A] = []	
		all_cite[item_id_A].append(item_id_B)
		
	print "all_cite: " + str(len(all_cite))
	print "all_id: " + str(len(all_id_year))
	ans = {}
	lines = f_in_error.readlines()
	print "all_id: " + str(len(all_id_year))

	f_out_no_relation = open("No_relation.txt","w")
	for line in lines:
		item_year = 0 
		if (line.strip() not in all_cite):
			print "No relations: " + str(line.strip())
			f_out_no_relation.write(line.strip() + "\n")
			continue

		for item_id in all_cite[line.strip()]:
			try:
				cited_item_year = all_id_year[item_id]
			except:
				print line.strip() + " " + item_id
			if item_year < cited_item_year:
				item_year = cited_item_year
		ans[line.strip()]= item_year + 1

	print "ans: " + str(len(ans))
	f_out = open("error_title_correct.txt", "w")
	for item in ans:
		if ans[item] > 1900:
			f_out.write(str(item) + "," + str(ans[item])+ "\n")
		else: 
			f_out_no_relation.write(str(item.strip())+ "\n")

def refining_data():
	#연도 이상한거 acm.txt에서 삭제하는 도구
	f_in_no_relation = open("No_relation.txt","r")
	f_in_correct = open("error_title_correct.txt","r")
	f_in_acm = open("../1.raw_data/acm.txt", "r")
	f_out_acm = open("../1.raw_data/acm3.txt","w")

	no_relation = {}
	correct = {}

	lines = f_in_no_relation.readlines()
	for line in lines:
		no_relation[line.strip()] = 1

	lines = f_in_correct.readlines()
	for line in lines:
		parse = line.split(",")
		correct[parse[0]] = int(parse[1])

	flag = 0
	lines = f_in_acm.readlines()
	data = ["","","","","",[],""]
	symbal = {'*':0,'@':1,'t':2,'c':3,'i':4,'%':5,'!':6 }
	for line in lines:
		if len(line)>1:
			if (line[1] not in symbal):
				continue
			address = symbal[line[1]]
			if (address == 0):
				if (data[address] != ""):
					if flag == 0:
						#flag == 1이면 no relation이므로 출력하지 않을 것
						for i in data:
							if (type(i) == str):
								if (i != ""):
									f_out_acm.write(i)
							elif(len(data[5]) >0):
								for j in data[5]:
									f_out_acm.write(j)
						f_out_acm.write("\n")
					data = ["","","","","",[],""]
					flag = 0
				data[address] = line
			elif address == 2:
				if (int(line[2:]) < 1900):
					flag = 1
				data[address] = line

			elif (address == 5):
				#다른 데이터와 달리 리스트를 사용하므로 예외처리
				data[address].append(line)
			elif(address ==4):
				#아이템 아이디가 버리는건지, 쓸만한건지, 상관없는건지 확인하기 위해 예외처리 
				item_id = line[6:].strip()
				if (item_id in no_relation):
					#flag =1로 설정, 출력하지 말라는 뜻 
					flag = 1
				elif (item_id in correct):
					#조정된 연도가 있으면 그걸로 초기화 
					data[2] = "#t" + str(correct[item_id])+"\n"
					flag = 0
				#상관없음 패스
				data[address] = line
			else:
				#0,1,2,3의 경우 일반 제목, 저자, 퍼블리셔, 연도 이므로 그냥 저장 
				data[address] = line

			if (line == lines[len(lines)-1]):
				#마지막 데이터 출력
				for i in data:
					if (type(i) == str):
						if (i != ""):
							f_out_acm.write(i)
					elif(len(data[5]) >0):
						for j in data[5]:
							f_out_acm.write(j)
				data = ["","","","","",[],""]
				f_out_acm.write("\n")
		

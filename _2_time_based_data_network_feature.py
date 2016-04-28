#-*-encoding: utf-8 -*-
# ipython notebook --ip 0.0.0.0 --port 9999
#import mathplotlib.
#%matplotlib inline 이걸 써줘야 아이파이썬에서 가능
def cite_year_divider(in_path, out_path):
	#sample code
		#import _2_time_based_data_network_feature
		#cite_year_divider_in_path = "../2.processed_data/"
		#cite_year_divider_out_path = "../3.time_based_data/1.cite_relation_devide/"
		#_2_time_based_data_network_feature.cite_year_divider(cite_year_divider_in_path, cite_year_divider_out_path)


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
	#sample code
		#import _2_time_based_data_network_feature
		#make_net_in_path = "../3.time_based_data/1.cite_relation_devide/"
		#make_net_out_path = "../3.time_based_data/2.centrality_data/"
		#_2_time_based_data.make_net( "in_degree", make_net_in_path, make_net_out_path)

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


def centrality_maker(year,in_path, out_path):
	#아직 안돌림 나중에 계산 다 되면 돌려야 함
	#load centrality, communicatability계산되면 돌릴 것
	#해당 연도까지의 max, slope, sum 값을 모아서 저장한다.

	#sample code
		#import _2_time_based_data_network_feature
		#centrality_maker_in_path = "../3.time_based_data/2.centrality_data/"
		#centrality_maker_out_path = "../3.time_based_data/3.centrality_feature_data/"
		#_2_time_based_data.make_cited_count_sheet(centrality_maker_in_path,centrality_maker_out_path)
	start_time = time.time()

	year = year - 1936 + 1
	#id 공간 때문에 + 1
	file_name = ["in_degree_centrality", 
					"degree_centrality", 	
					"load_centrality", 
					"communicability_centrality", 
					"pagerank_centrality"]

	for name in file_name:
		list_id = []
		list_max = []
		list_sum = []
		list_slope = []

		f = open("./4.centrality_data/"+name+".csv", "r")
		lines = csv.reader(f)
		for line in lines:
			val = map(float, line)

			val_slope = val[1]
			for v in val[2:year]:
				val_slope = max(val_slope,v-val_slope)

			val_id = int(val[0])
			val_max = max(val[1:year])
			val_sum = sum(val[1:year])
			
			list_id.append(val_id)
			list_max.append(0-val_max)
			list_sum.append(0-val_sum)
			list_slope.append(0-val_slope)


		rank_max = rankdata(list_max)
		rank_sum = rankdata(list_sum)
		rank_slope = rankdata(list_slope)
		#print str(len(rank_max)) +" " + str(len(rank_sum)) +" " + str(len(rank_slope))
		f_out_1 = open(out_path+name+"_max.csv","w")
		f_out_2 = open(out_path+name+"_sum.csv","w")
		f_out_3 = open(out_path+name+"_slope.csv", "w")
		cnt = 0
		for i in rank_max:
			f_out_1.write(str(list_id[cnt]) +","+ str(i) + "\n")
			cnt = cnt + 1
		cnt =0
		for i in rank_sum:
			f_out_2.write(str(list_id[cnt]) +","+ str(i) + "\n")
			cnt = cnt + 1
		cnt =0

		for i in rank_slope:
			f_out_3.write(str(list_id[cnt]) +","+ str(i) + "\n")	
			cnt = cnt + 1
		cnt =0

	print("centrality_maker takes %s seconds" % (time.time() - start_time))
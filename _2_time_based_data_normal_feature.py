#-*-encoding: utf-8 -*-
# ipython notebook --ip 0.0.0.0 --port 9999
#import mathplotlib.
#%matplotlib inline 이걸 써줘야 아이파이썬에서 가능
def make_cited_count_sheet(in_path, out_path):
	#sample code
		#import _2_time_based_data_normal_feature
		#make_cited_count_in_path = "../3.time_based_data/1.cite_relation_devide/"
		#make_cited_count_out_path = "../3.time_based_data/2.centrality_data/"
		#_2_time_based_data_normal_feature.make_cited_count_sheet(make_cited_count_in_path,make_cited_count_out_path)
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
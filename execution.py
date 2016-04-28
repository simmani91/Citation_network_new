#-*-encoding: utf-8 -*-

import code
import _1_processed_data
import _2_time_based_data_network_feature

#processed_data_input_file_path = "../1.raw_data/acm.txt"
#processed_data_output_file_path = "../2.processed_data/"
#_1_processed_data.processed_data(processed_data_input_file_path,processed_data_output_file_path)

#에러를 잡아는데 사용한 코드, 나중에 _1_raw_to_processed_parser로 옯겼다. 
#_1_processed_data.check_year_error()
#_1_processed_data.refining_data()

#cite_year_divider_in_path = "../2.processed_data/"
#cite_year_divider_out_path = "../3.time_based_data/1.cite_relation_devide/"
#_2_time_based_data_network_feature.cite_year_divider(cite_year_divider_in_path, cite_year_divider_out_path)

#중심성을 만들어 계산한다. 
#make_net_in_path = "../3.time_based_data/1.cite_relation_devide/"
#make_net_out_path = "../3.time_based_data/2.centrality_data/"

#_2_time_based_data_network_feature.make_net( "in_degree", make_net_in_path, make_net_out_path)
#_2_time_based_data_network_feature.make_net( "degree", make_net_in_path, make_net_out_path)
#실패 수렴불가 1956년부터 _2_time_based_data_network_feature.make_net( "eigenvector", make_net_in_path, make_net_out_path)
#실패 수렴불가 1956년부터 _2_time_based_data_network_feature.make_net( "katz", make_net_in_path, make_net_out_path)
#_2_time_based_data_network_feature.make_net( "pagerank", make_net_in_path, make_net_out_path)
#_2_time_based_data_network_feature.make_net( "communicability", make_net_in_path, make_net_out_path)
#_2_time_based_data_network_feature.make_net( "load", make_net_in_path, make_net_out_path)

#make_cited_count_in_path = "../3.time_based_data/1.cite_relation_devide/"
#make_cited_count_out_path = "../3.time_based_data/2.centrality_data/"
#_2_time_based_data_normal_feature.make_cited_count_sheet(make_cited_count_in_path,make_cited_count_out_path)
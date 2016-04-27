#-*-encoding: utf-8 -*-

import code
import _1_raw_to_processed_parser


#processed_data_input_file_path = "../1.raw_data/acm.txt"
#processed_data_output_file_path = "../2.processed_data/"
#_1_raw_to_processed_parser.processed_data(processed_data_input_file_path,processed_data_output_file_path)

#에러를 잡아는데 사용한 코드, 나중에 _1_raw_to_processed_parser로 옯겼다. 
#_1_raw_to_processed_parser.check_year_error()
#_1_raw_to_processed_parser.refining_data()

#data_descriptor_in_path = "../2.processed_data/"
#data_descriptor_out_path = "../1.raw_data/0.data_description/"
#code.data_descriptor(data_descriptor_in_path, data_descriptor_out_path)
#code.cite_data_refining(data_descriptor_in_path, data_descriptor_in_path)

#cite_year_divider_in_path = "../2.processed_data/"
#cite_year_divider_out_path = "../3.time_based_data/1.cite_relation_devide/"
#code.cite_year_divider(cite_year_divider_in_path, cite_year_divider_out_path)

#중심성을 만들어 계산한다. 
make_net_in_path = "../3.time_based_data/1.cite_relation_devide/"
make_net_out_path = "../3.time_based_data/2.centrality_data/"

#code.make_net( "in_degree", make_net_in_path, make_net_out_path)
#code.make_net( "degree", make_net_in_path, make_net_out_path)
#실패 수렴불가 1956년부터 code.make_net( "eigenvector", make_net_in_path, make_net_out_path)
#실패 수렴불가 1956년부터 code.make_net( "katz", make_net_in_path, make_net_out_path)
#code.make_net( "pagerank", make_net_in_path, make_net_out_path)
#code.make_net( "communicability", make_net_in_path, make_net_out_path)
#code.make_net( "load", make_net_in_path, make_net_out_path)

make_cited_count_in_path = "../3.time_based_data/1.cite_relation_devide/"
make_cited_count_out_path = "../3.time_based_data/2.centrality_data/"

code.make_cited_count_sheet(make_cited_count_in_path,make_cited_count_out_path)
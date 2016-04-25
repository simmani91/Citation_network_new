#-*-encoding: utf-8 -*-

import code
import _1_raw_to_processed_parser


#processed_data_input_file_path = "../1.raw_data/acm.txt"
#processed_data_output_file_path = "../2.processed_data/"
#_1_raw_to_processed_parser.processed_data(processed_data_input_file_path,processed_data_output_file_path)

#에러를 잡아는데 사용한 코드, 나중에 _1_raw_to_processed_parser로 옯겼다. 
#_1_raw_to_processed_parser.check_year_error()
#_1_raw_to_processed_parser.refining_data()


cite_year_divider_in_path = "../2.processed_data/"
cite_year_divider_out_path = "../3.time_based_data/1.cite_relation_devide"
code.cite_year_divider(cite_year_divider_in_path, cite_year_divider_out_path)

data_descriptor_in_path = "../2.processed_data/"
data_descriptor_out_path = "../1.raw_data/0.data_description/"
#code.data_descriptor(data_descriptor_in_path, data_descriptor_out_path)
#code.data_descriptor_2(data_descriptor_out_path, data_descriptor_out_path)
cite_data_refining(data_descriptor_out_path, data_descriptor_out_path)
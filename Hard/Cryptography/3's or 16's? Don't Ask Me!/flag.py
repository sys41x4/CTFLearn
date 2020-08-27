######## By Arijit Bhowmick #########
#####################################
# My twitter id = anon_r00ter 
# twitter link = https://twitter.com/anon_r00ter
# Github Profile = https://github.com/root-ji218at
#


import binascii
import os

open_reference_file = open("3's or 16's.txt", "rb")
open_cache_file = open("flag.txt", "wb")
read_byte_code = open_reference_file.read()
write_byte_code = open_cache_file.write(read_byte_code)
open_reference_file.close()
open_cache_file.close()

progress = 1

while progress==1:
	try:
		open_file = open("flag.txt", "r")
		read_hex_code = (open_file.read()).replace("\n", " ")
		open_file.close()
		
		

		read_string_list = read_hex_code.split(" ")
		str_num_count = len(read_string_list)

		for string_test in read_string_list:
			true_hex = 0
			no_hex = 0
			try:
				
				hex_decoded = binascii.unhexlify(string_test)
				true_hex += 1
				flag_file = open("flag.txt", "wb")
				flag_file.write(hex_decoded)
				flag_file.close()
			except:
				no_hex += 1
				continue
		if str_num_count == no_hex:
			print("The Flag File is saved as \"flag.txt\"\n\nThe flag is -->", read_hex_code)
			progress=0
			break
	except:
		continue



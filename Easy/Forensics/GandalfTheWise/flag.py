# Arijit Bhowmick

import codecs
import base64

enc_str = open("enc_strings", "rb")

enc_str_read = enc_str.readlines()

enc_str.close()

#print(byte_code_read)
for enc_string in enc_str_read:

	print((enc_string.decode()).replace("\n", ""), "is converted to hex as --->\n")
	print((codecs.encode((base64.b64decode(enc_string)), "hex")).decode())
	print("-"*60)


import base64

enc_flag = open("flag.txt", "r")
enc_flag_read = enc_flag.readlines()
enc_flag.close()

decode_flag = base64.b64decode((enc_flag_read[0]).encode())

a=1

while True:
	try:
		decode_flag = base64.b64decode(decode_flag)
	except:
		break

print("flag --> ",(decode_flag).decode())
	

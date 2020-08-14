# Arijit Bhowmick


data_file = open("data.dat", 'r')

tested_words = data_file.readlines()

data_file.close()

flag_seg = 0

for t_words in tested_words:
	if ((t_words.count("0"))%3) == 0 or ((t_words.count("1"))%2) == 0 :
		flag_seg += 1
	else:
		continue
print("flag -->",flag_seg)

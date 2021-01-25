from PIL import Image


def printTab(tab):
    for ligne in tab:
      for ele in ligne:
        print(ele, end="\t")
      print()


def char2bin(char):
	"""
	Transforme un charactère en sa representation binaire encodé en utf-8
	:param char type str
	:return type str representation binaire du charactère
	"""
	"""
	a_encoder = bin(ord(char))[2:]
	longeur = len(a_encoder)
	print(a_encoder)
	if longeur < 8 :
		tmp = '0' + '0' * (7 - longeur) + a_encoder
		return tmp[:4] + " " + tmp[4:]
	elif longeur < 12 :
		tmp = '110' + '0' * (5-len(a_encoder[6:])) + a_encoder[:5-len(a_encoder[5:])] + '10' + a_encoder[4-len(a_encoder[6:]):]
		return tmp[:4] + " " + tmp[4:8] + "  " + tmp[8:12] + " " + tmp[12:]
	elif longeur < 16 :
		tmp = '1112' + '0' * (4-len(a_encoder[6:])) + a_encoder[:5-len(a_encoder[5:])] + '12' + a_encoder[4-len(a_encoder[6:]):]
		return tmp[:4] + " " + tmp[4:8] + "  " + tmp[8:12] + " " + tmp[12:16] + " " + tmp[16:20] + " " + tmp[20:]
	"""
	return "".join(f"{i:08b}" for i in (char.encode("utf-8")))


def bin2char(binary):
	"""
	Transforme une representation binaire encodé en utf-8 en charactère 
	:param binary type str
	:return type str charactère
	"""
	octet = len(binary) // 8
	if octet == 1:
		tmp = binary
	elif octet == 2:
		tmp = binary[3:8] + binary[10:]
	elif octet == 3:
		tmp = binary[4:8] + binary[10:16] + binary[18:24]
	elif octet == 4:
		tmp = binary[5:8] + binary[10:16] + binary[18:24] + binary[26:32]
	return chr(int(tmp, 2))


def text2bin(text):
	return " ".join(char2bin(text[i]) for i in range(len(text)))


def bin2text(binary):
	tmp = binary.split(" ")
	return "".join(bin2char(str(val)) for val in tmp)


def pre_bin(binary):
	tmp = []
	binary = str(binary)
	counter = len(binary) // 8
	while counter != 0:
		if binary[:1] == '0':
			tmp.append(binary[:8])
			binary = binary[8:]
			counter -= 1
		elif binary[:3] == '110':
			tmp.append(binary[:16])
			binary = binary[16:]
			counter -= 2
		elif binary[:4] == '1110':
			tmp.append(binary[:24])
			binary = binary[24:]
			counter -= 3
		elif binary[:5] == '11110':
			tmp.append(binary[:32])
			binary = binary[32:]
			counter -= 4
		else:
			counter -= 1
			binary = binary[8:]
	return " ".join(val for val in tmp if val != '00000000')



def checkimg():
	aray = []
	counter = 0
	imgH = Image.open("/home/runner/NSI-1-Urbain/Cours/H.png")
	imgHm = Image.open("/home/runner/NSI-1-Urbain/Cours/H_modifiee.png")
	colonne,ligne = imgH.size
	for i in range(ligne):
		tmp = []
		for j in range(colonne):
			pixelH = imgH.getpixel((j,i)) # récupération du pixel
			pixelHm = imgHm.getpixel((j,i))
			if pixelH[1] == pixelHm[1] and pixelH[0]==pixelHm[0] and pixelH[2]==pixelHm[2]:
				tmp.append(0)
			else:
				tmp.append(1)
				counter += 1
		aray.append(tmp)
	return aray


def main():
	tmp = ""
	dif_aray = checkimg()
	for i in dif_aray:
		for y in i:
			tmp = tmp + str(y)
		
	print(bin2text(pre_bin(tmp)))


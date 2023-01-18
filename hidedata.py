# ord it will convert characters to unicode(ASCII)
#08b it will convert integers to unicode(ASCII)
from PIL import Image

def genData(data):

		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd


def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")
	    
def modPix(pix, data):

	# datalist show us what is the msg we need to hide
	datalist = genData(data)
	# length of msg
	lendata = len(datalist)
	# in an image, you are iterating induvidual pixels iter() function in python
	imdata = iter(pix)

	for i in range(lendata):
		
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]
		
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				# pix[j] -= 1

		
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	print("what is w", w)
	(x,y) = (0,0)
	for pixel in modPix(newimg.getdata(), data):
		newimg.putpixel((x,y), pixel)
		if(x == w-1):
			x =0 
			y += 1
		else:
			x += 1

def encode():
	myimg = input("Enter the image name(with extension png:): ")
	image = Image.open(myimg, "r")
	msg_hide = input("enter the msg to hide/encode: ")
	if(len(msg_hide) == 0):
		raise ValueError("msg_hide is empty")
	newImage = image.copy()
	encode_enc(newImage, msg_hide)
	message_hide_image = input("Enter the new image path with extension: ")
	newImage.save(message_hide_image, str(message_hide_image.split(".")[1].upper()))
	main()
def decode():
	myimg = input("Enter the image name with extension: ")
	image = Image.open(myimg, "r")
	msg_hide = " "
	imageData = iter(image.getdata())
	print("in decode what is image Data")
	print(imageData)
	while True:
		pixels = [value for value in imageData.__next__()[:3] +
								imageData.__next__()[:3] +
								imageData.__next__()[:3]]
		binstring = ""
		for i in pixels[:8]:
			if(i%2 == 0):
				binstring += '0'
			else: 
				binstring += '1'
	
		msg_hide += chr(int(binstring,2))
		#print("what is data we decoded")
		#print(msg_hide)

		if (pixels[-1] % 2 != 0):
			pixels[-1] -= 1

# Main Function
# Driver Code
if __name__ == '__main__' :
	# Calling main function
	main()
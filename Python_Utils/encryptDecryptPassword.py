import base64

def encryptPassword(inpPlainPassword):
	try:
		inpPassword = inpPlainPassword.encode("UTF-8")
		encryptedPassword = base64.b64encode(inpPassword)

		#return encryptedPassword.decode('ascii')
		print(encryptedPassword.decode('ascii'))
  
	except Exception as e:
		print(e)

def decryptPassword(inpEncryptedPassword):
	try:
		decryptedPassword = base64.b64decode(inpEncryptedPassword)
		print(decryptedPassword.decode(('ascii')))

  		#return decryptedPassword.decode(('ascii'))

	except Exception as e:
		print(e)
  
def main():
    encryptPassword("Welcome")
    decryptPassword("V2VsY29tZQ==")


if __name__ == "__main__":
	main()
def salutation(name):
	if name == "Phil":
		print('Hello, Phil')
	else:
		print('Hello. {0} is unknown.'.format(name))


name  = input('Enter your name:s')
salutation(name)

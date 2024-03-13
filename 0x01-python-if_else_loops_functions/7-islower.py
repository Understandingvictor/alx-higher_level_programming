def islower(c):
	for i in range(97, 123):
		character = chr(i)
		if character == c:
			return True
	return False

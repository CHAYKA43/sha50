class sha50:
	def __init__(self, text):
		self.text = text
	def sum(self):
		bytess = bytearray(self.text.encode())
		if len(bytess) < 2000:
			goyda = 2000 - len(bytess)
			for i in range(goyda):
				rbyte = bytearray([((((i + 254) * len(bytess)) + 1) + len(self.text)) % 256])
				bytess = bytess + rbyte
		elif len(bytess) > 2000:
			max_start = len(bytess) - 2000
			start = (max_start + 1 * len(bytess)) % len(bytess)
			bytess = bytess[start:start + 2000]
		for i in range(len(bytess)):
			bytess[i] = ((bytess[i] + len(bytess) - 1) + len(self.text)) % 256
		for i in range(len(bytess)):
			bytess[i] = (bytess[i] + bytess[i-1] + len(self.text)) % 256
		bytehex = bytess.hex()
		goydabyte = []
		for i in range(0, len(bytehex), 5):
			goydabyte.append(bytehex[i])
		bytehex = ''.join(goydabyte)
		bytehex = bytearray(bytehex.encode())
		for i in range(len(bytehex)):
			bytehex[i] = ((bytehex[i] + len(bytehex) - 1) + len(self.text)) % 256
		for i in range(len(bytehex)):
			bytehex[i] = (bytehex[i] + bytehex[i-1] + len(self.text)) % 256
		bytehex = bytehex.hex()
		max_start = len(bytehex) - 50
		start = (max_start + 1 * len(bytehex)) % len(bytehex)
		bytehex = bytehex[start:start + 50]
		return bytehex
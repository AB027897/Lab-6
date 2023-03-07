# William Osborne
def decode(pwenc):
	out = ""
	for c in pwenc:
		out += chr((ord(c) % 0x30 - 3) % 10 + 0x30)
	return out

# William Osborne
def decode(pwenc):
	out = ""
	for c in pwenc:
		out += str((int(c) - 3) % 10)
	return out

def smallestCube():
	for a in range(1,11):
		for b in range(1,11):
			for c in range(1, 11):
				for d in range(1,11):
					if a**3 == (b**3) + (c**3) + (d**3):
						return a, b, c, d
						

a,b,c,d = smallestCube()
print(a,b,c,d)
		
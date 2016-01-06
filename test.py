
for i in range(10):
	count=False
	for j in range(2,i):
		if i%j==0:
			break
		else:
			count=True
	if count:
		print i


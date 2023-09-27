r = [252, 198]
q = [1]
s = [1, 0]
t = [0, 1]
i = 0
while r[i]%r[i+1] != 0:
	#r[i] = r[i + 1] * r[i]//r[i + 1] + r[i]%r[i + 1]
	r.append(r[i]%r[i + 1])
	q.append(r[i]//r[i + 1])
	i += 1
else:
	q.append(r[i]//r[i + 1])
	
for j in range(2, i + 2):
	s.append(s[j -2] - q[j -1]*s[j - 1])
	t.append(t[j - 2] - q[j - 1]*t[j - 1])
print(i)
print("r : ",r)
print("q : ",q)
print("s : ",s)
print("t : ",t)	
print()
for k in range(i):
	print(k, r[k], r[k + 1], q[k + 1], r[k + 2], s[k], t[k])

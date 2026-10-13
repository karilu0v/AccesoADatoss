multiplos=[]
for i in range(7, 101, 7):
    multiplos.append(i)
print(multiplos)
print(multiplos[3])
print(multiplos[-5:])
print(multiplos[2:6])
print(multiplos[::2])

for i, v in enumerate(multiplos):
	print(i,v)
print()
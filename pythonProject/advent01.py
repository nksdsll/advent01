def bubblesort(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] < x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


f = open("advent01.kande")
list = []
elf1 = 0
results = []
for line in f.readlines():
    line = line.rstrip()
    list.append(line)
    if line == "":
        results.append(int(elf1))
        elf1 = 0
    if line != "":
        elf1 += (int(line))

if elf1 > 0:
    results.append(int(elf1))

bubblesort(results)
f.close()
print(results[0])

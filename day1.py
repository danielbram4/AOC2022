elf = []
file = open("calories.txt", "r")
lines = file.readlines()
sum = 0
for line in lines:
    if line != "\n":
        sum = sum + int(line)
    else:
        elf.append(sum)
        sum = 0

elf.sort(reverse=True)
for e in elf:
    if(int(e) != 0):
        print(e)

#print("The elf carrying the most calories is", elf[0])
total = 0
max = elf[:3]
for m in max:
    total = m + total
print("The total is ",total)

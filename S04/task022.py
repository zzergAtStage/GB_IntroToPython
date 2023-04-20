mol = [int(x) for x in input("Input range of list (2 number): ").split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input("Input set 1: ").split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input("Input set 2: ").split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
#the main row in this program
lok = set_1 & set_2 #

kool = list(lok)
kool.sort()

for i in kool:
    print(i, end=' ')

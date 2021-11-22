#Compression:72.07%
#Speed:38.85%
import os
import sys
fd = sys.stdin
csv = fd.read()
input = csv.split("\n")
tmp = input[0].split(", ")
tmp1 = tmp[0].split("# ")
tmp[0] = tmp1[1]
del input[0]
data = [[["test" for x in range(int(tmp[2]))]
        for c in range(int(tmp[1]))]for y in range(int(tmp[0]))]
i = 0
count1 = int(tmp[0])*int(tmp[1])*int(tmp[2])
count2 = int(tmp[3])*int(tmp[4])*int(tmp[5])
count = int(count1/count2)
for z in range(int(tmp[2])):
    for y in range(int(tmp[1])):
        for x in range(int(tmp[0])):
            tmp4 = input[i].split(", ")
            tmp2 = tmp4[len(tmp4)-1].split("\n")
            tmp4[len(tmp4)-1] = tmp2[0]
            data[x][y][z] = tmp4[len(tmp4)-1]
            i = i+1
a = 0  # x
b = 0  # y
c = 0  # z
for i in range(count):
    test2 = ""
    flag2 = 0
    numbers = (str(a), str(b), str(c))
    output = []
    p = 0
    test1 = ""
    flag1 = 0
#        print("a={0}".format(a))
#        print("b={0}".format(b))
#        print("c={0}".format(c))
    test1 = data[a][b][c]
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if(data[a+x][b+y][c+z] != test1):
                    flag1 = 1
#        print(flag1)
    if(flag1 == 1):
        flag2 == 1
        for z in range(2):
            block = data[a][b][c+z]
            if(data[a+0][b+1][c+z]==block)&(data[a+1][b+0][c+z]==block)&(data[a+1][b+1][c+z]==block):
                sys.stdout.write("{0}, {1}, {2}, 2, 2, 1, {3}\n".format(str(a), str((b)), str((c+z)), data[a][b][c+z]))
            else:
                for y in range(2):
                    if(data[a][b+y][c+z]==data[a+1][b+y][c+z]):
                        sys.stdout.write("{0}, {1}, {2}, 2, 1, 1, {3}\n".format(str(a), str((b+y)), str((c+z)), data[a][b+y][c+z]))
                    else:
                        for x in range(2):
                            number = (a+x)+(b+y)*int(tmp[0])+(c+z)*int(tmp[0])*int(tmp[1])
                            sys.stdout.write(input[number]+"\n")
    else:
        out = "{0}, {1}, {2}, {3}, {4}, {5}, {6}\n".format(
            str(a), str(b), str(c), "2", "2", "2", test1)
        sys.stdout.write(out+"\n")
#        print("b_flag={0}".format(b_flag))
    a = int(numbers[0])+int(tmp[3])
    b = int(numbers[1])
    c = int(numbers[2])
    if(a == int(tmp[0])):
        a = 0
        b = int(numbers[1])+2
    if(b == int(tmp[1])):
        b = 0
        c = int(numbers[2])+2

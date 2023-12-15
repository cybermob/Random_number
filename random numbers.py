import random
ip1 = int(input())
lis = []
x = list(range(1,ip1+1))

while len(lis)<ip1:
    ss = input()

    p = random.choice(x)
    print("Number is:",p)
    x.remove(p)
    lis += [p]
    print("")
    # print(len(x))
    print("new:",sorted(lis),len(lis))
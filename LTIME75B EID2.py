# cook your dish here
t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    c = a[0:3]
    d = a[3:]
    f = 0
    for j in range(3):
        for k in range(j + 1, 3):
            if c[j] > c[k]:
                p = c[j]
                c[j] = c[k]
                c[k] = p
                p = d[j]
                d[j] = d[k]
                d[k] = p
    for j in range(2):
        if c[j] == c[j + 1]:
            if d[j] != d[j + 1]:
                print("NOT FAIR")
                f = 1
                break
        elif c[j] > c[j + 1]:
            if d[j] <= d[j + 1]:
                print("NOT FAIR")
                f = 1
                break
        else:
            if d[j] >= d[j + 1]:
                print("NOT FAIR")
                f = 1
                break
    if f == 0:
        print("FAIR")

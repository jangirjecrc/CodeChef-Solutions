# cook your dish here
t = int(input())
for i in range(t):
    abc = list(map(int, input().split()))
    s = abc[0] + 2 * abc[1] + 3 * abc[2]
    if s % 2 != 0:
        print("NO")
    else:
        p = 0
        s = int(s / 2)
        if abc[0] == abc[1] and abc[1] == abc[2]:
            print("YES")
        elif abc[0] % 2 == 0 and abc[1] % 2 == 0 and abc[2] % 2 == 0:
            print("YES")
        else:
            d = int(s / 3)
            if d >= abc[2]:
                p = abc[2] * 3
            else:
                p = d * 3
            s = s - p
            if s == 0:
                print("YES")
            else:
                d = int(s / 2)
                if d >= abc[1]:
                    p = abc[1] * 2
                else:
                    p = d * 2
                s = s - p
                if s <= abc[0]:
                    print("YES")
                else:
                    print("NO")








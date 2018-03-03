s = input()
list1 = []
cnt = 0

if(len(s) == 1):
    t = (1, eval(s))
    print(t)
else:
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            cnt += 1
            if(i == len(s)-2):
                if (s[i].isdigit()):
                    t = (cnt+1, eval(s[i]))
                else:
                    t = (cnt+1, s[i])
                list1.append(t)
        else:
            if (s[i].isdigit()):
                t = (cnt+1, eval(s[i]))
            else:
                t = (cnt+1, s[i])
            cnt = 0
            list1.append(t)
            if(i == len(s)-2):
                if (s[i+1].isdigit()):
                    t = (cnt+1, eval(s[i+1]))
                else:
                    t = (cnt+1, s[i+1])
                list1.append(t)
    for j in list1:
        print(j, end = " ")
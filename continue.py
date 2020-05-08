print("this is with continue")
## continue
for i in range(1,10):
    if (i % 2 == 0):
        print("even")
    else:
        continue
    print(i)


## blank
print("this is leaving blank")
for i in range(1,10):
    if (i % 2 == 0):
        print("even")
    else:
        pass 

    print(i)


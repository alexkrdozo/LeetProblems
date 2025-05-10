nums = [1, 1, 0, 1, 1, 1]
count = 0 
listaCount = []
for index, i in enumerate(nums):
    if i == 1:
        count += 1
        if index == (len(nums) - 1):
            listaCount.append(count)
            #print(listaCount)
        else:
            continue
    elif i != 1:
        listaCount.append(count)
        count = 0
        #print(listaCount)
        

print(max(listaCount))
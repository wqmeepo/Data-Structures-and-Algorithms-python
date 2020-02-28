def bubble(origin):
    n = len(origin)
    for i in range(n):
        for j in range(i,n):
            if origin[i] > origin[j]:
                origin[i],origin[j] = origin[j], origin[i]
    return origin


origin = [5,2,1,7,30,60,78,8,0]
bubble(origin)
print(origin)
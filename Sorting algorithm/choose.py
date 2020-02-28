def choose(origin):
    n = len(origin)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if origin[j] < origin[min_index]:
                min_index = j
        if min_index != i:
            origin[i],origin[min_index] = origin[min_index], origin[i]
        print(origin)
    return origin


origin = [5,2,1,7,30,60,78,8,0,9]
choose(origin)
print(origin)

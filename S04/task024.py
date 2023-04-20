def counterBearen():
    x = 12
    for i in range(1,x,2):
        yield i

arr = list()
for i in counterBearen():
    arr.append(i)

arr_count = list()
for i in range(len(arr)-1):
    arr_count.append(arr[i-1]+arr[i]+arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(arr_count)
print(max(arr_count))
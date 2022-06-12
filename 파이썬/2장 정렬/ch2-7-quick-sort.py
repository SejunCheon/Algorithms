a = [3,5,8,1,2,9,4,7,6]


def quick_sort(arr):
    if len(arr) < 1:
        return arr    
    pivot = len(arr) // 2 # 배열의 중간값
    print('피벗 : ', arr[pivot])
    small, medium, big = [],[],[]
    for i in range(0, len(arr)):
        if arr[i] < arr[pivot]:
            small.append(arr[i])
            print('small : ',small)
        elif arr[i] > arr[pivot]: 
            big.append(arr[i])
            print('big : ',big)
        else:
            medium.append(arr[i])
            print('medium : ',medium)
    return quick_sort(small) + medium + quick_sort(big)


print(quick_sort(a))

#----------- 메모리 사용이 적은 최적화

def quick_sort(arr, start, end):
    part = partition(arr, start, end)
    if start < part-1:
        quick_sort(arr, start, part-1)
    if end > part:
        quick_sort(arr, part, end)
    print(arr)
    return arr


def partition(arr, start, end):
    pivot = arr[(start + end) // 2]

    while start <= end:
        while arr[start] < pivot:
            start+=1
        while arr[end] > pivot:
            end-=1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    return start

print(quick_sort(a, 0, len(a)-1))
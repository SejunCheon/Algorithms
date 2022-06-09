# 정렬할 배열
a = [5,3,4,7,2,8,6,9,1]

def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                print(arr)
    return arr

print(insertion_sort(a))
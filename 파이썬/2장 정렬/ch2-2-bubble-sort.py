# 정렬할 배열
a = [5, 9, 3, 1, 2, 8, 4, 7, 6]

b = [9, 8, 75, 3, 2, 122]



def bubble_sort(arr):
    for i in range(len(arr) -1, 0, -1) :
        for j in range(i):
            if(arr[j] > arr[j + 1]) :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

print(bubble_sort(a))
    
    
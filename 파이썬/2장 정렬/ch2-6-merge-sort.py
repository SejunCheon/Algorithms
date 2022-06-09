a = [6, 4, 3, 7, 5, 1, 2]

def merge_sort(arr):
    if len(arr) < 2: # 배열이 2보다 작으면 재귀함수를 통해 배열나누기를 반복한다
        return arr
    mid = len(arr) // 2 # 배열의 중간지점
    l_arr = merge_sort(arr[:mid]) # 왼쪽
    r_arr = merge_sort(arr[mid:]) # 오른쪽
    
    merge_arr = [] # 재조합할 빈 배열
    
    l = r = 0 # 배열길이 비교를 위한 초기화 index
    
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
            merge_arr.append(l_arr[l])
            l += 1
        else:
            merge_arr.append(r_arr[r])
            r += 1
    
    merge_arr += l_arr[l:]
    merge_arr += r_arr[r:]
    return merge_arr    

# print(merge_sort(a))
            
# def merge_sort2(arr, start, end):
    

    
    
    
    
        
    



    
    





















# if len(arr) < 2: # 배열이 2보다 작으면 재귀함수를 통해 배열나누기를 반복한다
    #     return arr
    # mid = len(arr) // 2 # 배열의 중간지점
    # l_arr = merge_sort(arr[:mid]) # 왼쪽
    # r_arr = merge_sort(arr[mid:]) # 오른쪽
    
    # merge_arr = [] # 재조합할 빈 배열
    
    # l = r = 0 # 배열길이 비교를 위한 초기화 index
    
    # while l < len(l_arr) and r < len(r_arr):
    #     if l_arr[l] < r_arr[r]:
    #         merge_arr.append(l_arr[l])
    #         l += 1
    #     else:
    #         merge_arr.append(r_arr[r])
    #         r += 1
    
    # merge_arr += l_arr[l]
    # merge_arr += r_arr[r]
    # return merge_arr
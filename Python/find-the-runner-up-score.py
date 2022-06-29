if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    cleaned_arr = list(set(arr))
    
    maximum = max(cleaned_arr)
    cleaned_arr.remove(maximum)
    
    new_maximum = max(cleaned_arr)
    print(new_maximum)

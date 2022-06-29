if __name__ == '__main__':
    
    data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([score, name])
        
    data.sort()
    min_value = data[0][0]
    to_delete = [0]
    
    for i in range(1, len(data)):
        if data[i][0] == min_value: to_delete.append(i)
        
    to_delete.sort(reverse=True)
    for index in to_delete:
        data.pop(index)
        
    min_value = data[0][0]
    results = [student[1] for student in data if student[0] == min_value]
    
    results.sort()
    print('\n'.join(results))

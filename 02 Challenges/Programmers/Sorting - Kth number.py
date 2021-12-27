# source: https://neerc.ifmo.ru/subregions/northern.html

def solution(array, commands):
 
    answer = []
    for command in commands:
        start = command[0] - 1
        end = command[1]
        pos = command[2] - 1
        
        arr = array[start:end]
        arr.sort()
        value = arr[pos]
        answer.append(value)

    return answer

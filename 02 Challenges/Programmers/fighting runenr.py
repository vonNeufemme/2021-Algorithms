import time

# solution 1
def solution(participant, completion):
    
    start = time.time()
    
    answer = ""
    SIZE = len(participant)

    parts = participant.copy()
    comp = completion.copy()

    # compare the two lists
    for i in range(SIZE):
        if (participant[i] not in comp):
            answer = participant[i]
            return answer
        else:
            print(participant[i])
            parts.remove(participant[i])
            comp.remove(participant[i]) 

    answer = parts[0]
    end = time.time()
    print(end - start)

    # find the one missing and return
    return  answer
  
  
  
  
  # solution 2
  def solution(participant, completion):

    answer = ""
    SIZE = len(participant)

    participant.sort()
    completion.sort()
    
    # compare the two lists
    for i in range(SIZE):
        if (participant[i] not in completion):
            answer = participant[i]
    
    return participant[i]

# solution 1 (success 12 / fail 4 out of 16 tests)
def solution(scoville, K):
    answer = 0
    breakpoint = 0
    scoville.sort()

    while (scoville[0] < K):
        first = scoville.pop(0)
        second = scoville.pop(0)
        mixed = first + second * 2
        scoville.append(mixed)
        scoville.sort()
        answer += 1        

    return answer
  
  
  # solution 2

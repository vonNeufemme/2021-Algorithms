# solution 1
import numpy as np

def solution(citations):
    answer = 0
    total_cit = []

    for i in range(len(citations)):
        pubs = i+1
        cits = len([c for c in citations if (c >= pubs)])
        if (cits >= pubs):
            answer = cits

    return answer


# solution 2
def solution(citations):
    
    total = len(citations)
    citations.sort()
    answer = 0

    for i in range(total):
        h = total - i
        if (citations[i] >= h):
            answer = h
            break

    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/136798
import math

def getMyDivisor(n):

    divisorsCnt = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsCnt = divisorsCnt + 1
            if ( (i**2) != n) : 
                divisorsCnt = divisorsCnt + 1
    return divisorsCnt

def solution(number, limit, power):
    prise = 0
    people_list = []
    
    for i in range(1, number+1):
        if getMyDivisor(i) > limit:
            people_list.append(power)
        else:
            people_list.append(getMyDivisor(i))
        
    for i in people_list:
        prise += i
    
    return prise



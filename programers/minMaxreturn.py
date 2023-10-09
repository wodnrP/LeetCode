def solution(s):
    num = s.split(' ')
    num = sorted(list(map(int, num)))
    return str(num[0])+' '+str(num[-1])
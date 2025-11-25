if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first = float('-inf')
    second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x < first and x > second:
            second = x
    print (second)
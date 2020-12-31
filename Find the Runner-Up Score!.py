n = int(input())

na = map(int, input().split())    
print(sorted(list(set(na)))[-2])

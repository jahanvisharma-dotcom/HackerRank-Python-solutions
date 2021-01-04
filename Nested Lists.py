a={} 
for _ in range(int(raw_input())): 
    N=raw_input() 
    G=float(raw_input()) 
    a[N]=G 
v=a.values()
s=sorted(list(set(v)))[1] 
se=[] 
for key,value in a.items():  
    if value==s: 
        se.append(key) 
se.sort() 
for name in se: 
    print name 

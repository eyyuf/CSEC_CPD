n = int(input())

p = 0

for _ in range(n):
   
    a, b, c = map(int, input().split())
  
    if a + b + c >= 2:
      
        p += 1

print(p)

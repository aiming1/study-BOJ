N = int(input())//2
eq = input()
result = -1e12
for bit in range(1<<N):
  if bit&(bit<<1):
    continue
  eq1 = [*eq]
  for i in reversed(range(N)):
    if bit&(1<<i):
      eq1.insert(i*2+3,")")
      eq1.insert(i*2,"(")
  result = max(result,eval("".join(eq1)))
print(result)
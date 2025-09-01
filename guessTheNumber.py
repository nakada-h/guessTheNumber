import random
n,m=0,0
while n==m:
  print("input different two numbers")
  n=int(input())
  m=int(input())
n,m=min(n,m),max(n,m)
while True:
  num=random.randint(n,m)
  inputNum=int(input("guess the number"))
  if num==inputNum:
    print("success")
    break
  else:
    print(f"wrong. correct number is {num}")


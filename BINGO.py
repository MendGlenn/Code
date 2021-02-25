# BINGO SINGLE PLAYER(*)
import random
 
#RANDOM GRID GENERATION
A = random.sample(range(1, 26), 25)
def Grid():
  r = 0
  for i in range(0,5):
    for j in range(0,5):
      print(A[r], end=" ")
      if int(A[r])<10:
        print(end=" ")
      r = r + 1
    print()

def Win():
  d=0
  if((A[0]==0) and (A[5]==0) and (A[10]==0) and (A[15]==0) and (A[20]==0)):
    d=d+1
  if((A[1]==0) and (A[6]==0) and (A[11]==0) and (A[16]==0) and (A[21]==0)):
    d=d+1
  if((A[2]==0) and (A[7]==0) and (A[12]==0) and (A[17]==0) and (A[22]==0)):
    d=d+1
  if((A[3]==0) and (A[8]==0) and (A[13]==0) and (A[18]==0) and (A[23]==0)):
    d=d+1
  if((A[0]==0) and (A[9]==0) and (A[14]==0) and (A[19]==0) and (A[24]==0)):
    d=d+1
  if((A[0]==0) and (A[1]==0) and (A[2]==0) and (A[3]==0) and (A[4]==0)):
    d=d+1
  if((A[5]==0) and (A[6]==0) and (A[7]==0) and (A[8]==0) and (A[9]==0)):
    d=d+1
  if((A[10]==0) and (A[11]==0) and (A[12]==0) and (A[13]==0) and (A[14]==0)):
    d=d+1
  if((A[15]==0) and (A[16]==0) and (A[17]==0) and (A[18]==0) and (A[19]==0)):
    d=d+1
  if((A[20]==0) and (A[21]==0) and (A[22]==0) and (A[23]==0) and (A[24]==0)):
    d=d+1
  if((A[0]==0) and (A[6]==0) and (A[12]==0) and (A[18]==0) and (A[24]==0)):
    d=d+1
  if((A[4]==0) and (A[8]==0) and (A[12]==0) and (A[16]==0) and (A[20]==0)):
    d=d+1
  return d

# GAME STARTS
Grid()
w=0
while(w<5):
  e=1
  while(e==1):
    a=int(input("Select any number:"))
    b = int(A.index(a))
    pass
    if (a<26):
      e=0
    elif (b == "0"):
      print("Number is already selected") 
    else:  
      e=1       
  A[b] = 0
  w=Win()
  Grid()
print("U Won")
w=0
import random
def compare(c1,c2):
	if c1[1]>c2[1]:
		return c1
	elif c1[1]<c2[1]:
		return c2
	elif c1[1]==c2[1]:
		if c1[0]>c2[0]:
			return c1
		elif c1[0]<c2[0]:
			return c2
		elif c1[0]==c2[0]:
			return "Draw"
def convert(x):
    if x[0]==0:
        x[0]=chr(9830)
    elif x[0]==1:
        x[0]=chr(9827)
    elif x[0]==2:
        x[0]=chr(9829)
    elif x[0]==3:
        x[0]=chr(9824)
    if 11 in x:
        x[1]="J"
    elif 12 in x:
        x[1]="Q"
    elif 13 in x:
        x[1]="K"
    elif 14 in x:
        x[1]="A"
    elif x=="Draw":
        return "Draw"
    return x
#chr(9830)=Diamond,chr(9827)=Club,chr(9829)=Heart,chr(9824)=Spade
#[chr(9830),chr(9827),chr(9829),chr(9824)]
full_stack = [i for i in range(2,15)]
card1 = [random.randint(0,3),full_stack[random.randint(0,12)]]
card2 = [random.randint(0,3),full_stack[random.randint(0,12)]]
#Show card1,2 array
print("Card1: ",card1,"Card2: ",card2)
#Show return value of compare()
print("Compare two card:",compare(card1,card2))
result=compare(card1,card2)
print(convert(card1),convert(card2))
print(convert(result),"Win")
#print("Player 1 : ",convert(card1))
#print("Player 2 : ",convert(card2))
#print(convert(compare(card1,card2)),"Win.")

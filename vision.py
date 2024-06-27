prev="r000k00r/00000000/00000000/00000000/00000000/00000000/00000000/00000000"
curx="x0000xx0/00000000/00000000/00000000/00000000/00000000/00000000/00000000"

novih_praznih_mest = []
pieces = []
cur = ""
p=0
x=0
counter = 1   

for i in range(71):
    if prev[i].isalpha() == True and prev[i]!="/":
        p+=1
    if curx[i] == "x" and curx[i]!="/":
        x+=1
    if prev[i]!="0" and curx[i]=="0":
        pieces.append(prev[i])
    if prev[i]=="0" and curx[i]=="x":
        novih_praznih_mest.append(i)

    

if len(novih_praznih_mest)==1 and len(pieces) == 1 and p == x:
    for i in range(71):
        if prev[i] != "0" and curx[i] != "0":
            cur += prev[i]
        elif prev[i] != "0" and curx[i] == "0":
            cur+="0"
        elif prev[i] == "0" and curx[i] != "0":
            cur += pieces[0]
        elif prev[i] == "0" and curx[i] == "0":
            cur += prev[i]
        elif prev[i] == "/":
            cur+="/"


elif len(novih_praznih_mest)==2:

    for i in range(71):
        if prev[i] != "0" and curx[i] != "0":
            cur += prev[i]
        elif prev[i] != "0" and curx[i] == "0":
            cur+="0"
        elif prev[i] == "0" and curx[i] != "0" and curx[0]=="0":
            
            cur += pieces[counter]
            counter-=1
        
        elif prev[i] == "0" and curx[i] != "0":
            
            cur += pieces[counter]
            counter-=1


        elif prev[i] == "0" and curx[i] == "0":
            cur += prev[i]
        elif prev[i] == "/":
            cur+="/"

elif len(novih_praznih_mest) == 1 and len(pieces)==0 and p!=x:

    pass

print(cur)



games = []
player1 = []
player2 = []
file = open("rounds.txt", "r")
lines = file.readlines()

i = 0
for line in lines:
    games.append(line)

for p in games:
    x = p.split(" ")
    player1.append(x[0])
    player2.append(x[1])

player3 = []
for sub in player2:
    player3.append(sub.replace("\n", ""))
player2.clear()
player2 = player3


score = 0
for p1, p2 in zip(player1,player2):
    if(p2 == 'X'):
        if(p1 == 'A'):
            score += 3
        elif(p1 == 'B'):
            score += 1
        elif(p1 == 'C'):
            score += 2
    elif(p2 == 'Y'):
        if(p1 == 'A'):
            score += 4
        elif(p1 == 'B'):
            score += 5
        elif(p1 == 'C'):
            score += 6
    elif(p2 == 'Z'):
        if(p1 == 'A'):
            score+= 8
        elif(p1 == 'B'):
            score+=9
        elif(p1 == 'C'):
            score+=7
print(score)
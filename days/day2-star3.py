#!/usr/bin/env/python3

relative_path = './inputs/input-day2-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    print
    totalscore = 0
    roundscore = 0
    youscore = {"X":1,"Y":2,"Z":3}
    calcscore1 = {"A":"1","B":"2","C":"3"}
    calcscore2 = {"X":"1","Y":"2","Z":"3"}
    for i in range(0,len(lines_list)):
        playscore = 0
        roundscore = 0
        opponent = lines_list[i].rstrip().split(" ")[0]
        you = lines_list[i].rstrip().split(" ")[1]
        roundscore = youscore[you]
        print("Opp: ",opponent)
        print("You: ",you)
        print("ScoreOpp: ",calcscore1[opponent],"ScoreYou: ",calcscore2[you])
        playscore1 = int(calcscore1[opponent])
        playscore2 = int(calcscore2[you])
        # draw
        if(playscore1 == playscore2):
            playscore = 3
        # Rock defeats scissors    
        elif(playscore1 == 3 and playscore2 == 1):
            playscore = 6
        # Scissors defeats paper
        elif(playscore1 == 2 and playscore2 == 3):
            playscore = 6
        # Paper defeats rock
        elif(playscore1 == 1 and playscore2 == 2):
            playscore = 6   
        print("# Playscore: ",(playscore))
        print("# Roundscore: ",(int(roundscore)+playscore))
        totalscore += (int(roundscore)+playscore)
    print(totalscore)
#!/usr/bin/env/python3

relative_path = './inputs/input-day2-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    print
    totalscore = 0
    for i in range(0,len(lines_list)):
        playscore = 0
        opponent = lines_list[i].rstrip().split(" ")[0]
        you = lines_list[i].rstrip().split(" ")[1]
        print("Opp: ",opponent)
        print("You: ",you)
        if(you == "X" and opponent == "A"):
            playscore = 3
        elif(you == "X" and opponent == "B"):
            playscore = 1
        elif(you == "X" and opponent == "C"):
            playscore = 2
        elif(you == "Y" and opponent == "A"):
            playscore = 4
        elif(you == "Y" and opponent == "B"):
            playscore = 5
        elif(you == "Y" and opponent == "C"):
            playscore = 6
        elif(you == "Z" and opponent == "A"):
            playscore = 8
        elif(you == "Z" and opponent == "B"):
            playscore = 9
        elif(you == "Z" and opponent == "C"):
            playscore = 7
        print("# Roundscore: ",(playscore))
        totalscore += (playscore)
    print(totalscore)
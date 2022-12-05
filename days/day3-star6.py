#!/usr/bin/env/python3

relative_path = './inputs/input-day3-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    totalScore = 0
    for i in range(0,len(lines_list)): 
        if i%3 == 0:
            print(i)
            print("line1",lines_list[i])
            print("line2",lines_list[i+1])
            print("line3",lines_list[i+2])
            part1 = (lines_list[i])
            part2 = (lines_list[i+1])
            part3 = (lines_list[i+2])
            a=list(set(part1)&set(part2)&set(part3))
            print("Common letter is:")
            print("list:",a)
            for char in a:
                print("Found:",char)
                score = 0
                if(char.islower()):
                    score = (ord(char)-96)
                if(char.isupper()):
                    score = (ord(char)-38)
                print("Character",char,"heeft score",score)
                totalScore += score
    print("# Totaal:",totalScore)
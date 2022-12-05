#!/usr/bin/env/python3

relative_path = './inputs/input-day3-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    totalScore = 0
    for i in range(0,len(lines_list)):
        print(lines_list[i])
        print(lines_list[i][0:(len(lines_list[i])//2)])
        print(lines_list[i][(len(lines_list[i])//2):len(lines_list[i])])
        part1 = (lines_list[i][0:(len(lines_list[i])//2)])
        part2 = (lines_list[i][(len(lines_list[i])//2):len(lines_list[i])])
        a=list(set(part1)&set(part2))
        print("Common letter is:")
        for char in a:
            print("Found:",char)
        if(char.islower()):
            score = (ord(char)-96)
        if(char.isupper()):
            score = (ord(char)-38)
        print("Character",char,"heeft score",score)
        totalScore += score
    print("# Totaal:",totalScore)
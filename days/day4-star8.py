#!/usr/bin/env/python3
occurances = 0
relative_path = './inputs/input-day4-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    totalScore = 0
    for i in range(0,len(lines_list)): 
        print(lines_list[i])
        range1 = lines_list[i].split(",")[0].rstrip()
        startrange1 = range1.split("-")[0]
        endrange1 = range1.split("-")[1]
        range2 = lines_list[i].split(",")[1].rstrip()
        startrange2 = range2.split("-")[0]
        endrange2 = range2.split("-")[1]
        print("Range1:",startrange1,endrange1,"Range2:",startrange2,endrange2)
        if(int(startrange2) <= int(startrange1) <= int(endrange2)):
            print("StartRange1 valt binnen Range2")
            occurances += 1
        elif(int(startrange2) <= int(endrange1) <= int(endrange2)):
            print("EndRange1 valt binnen Range2")
            occurances += 1
        elif(int(startrange1) <= int(startrange2) <= int(endrange1)):
            print("StartRange2 valt binnen Range1")
            occurances += 1
        elif(int(startrange1) <= int(endrange2) <= int(endrange1)):
            print("EndRange2 valt binnen Range1")
            occurances += 1
print("# Totalscore: ",occurances)
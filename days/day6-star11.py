#!/usr/bin/env/python3

relative_path = './inputs/input-day6-2022'
with open(relative_path,"r") as file_handle:
    line = file_handle.read()
    for i in range(0,len(line)):
        if i > 3: 
            checklist = []
            checklist += line[i-4:i]
            if len(checklist) == len(set(checklist)):
                print("all unique values",checklist,"at value",i)
                break
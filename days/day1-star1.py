#!/usr/bin/env/python3

relative_path = './inputs/input-day1-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list))
    elf_sums = []
    sumblock = []
    for i in range(0,len(lines_list)):
        if lines_list[i] != "\n":
            sumblock.append(int(lines_list[i].split("\\")[0].rstrip()))
        elif lines_list[i] == "\n":
            elf_sums.append(sum(sumblock))
            sumblock = []
    print("Highest Elf: "+sorted(elf_sums)[-1])
    print("Jeeeh Star1!")


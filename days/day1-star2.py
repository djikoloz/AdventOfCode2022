#!/usr/bin/env/python3

relative_path = './inputs/input-day1-2022'
with open(relative_path,"r") as file_handle:
    lines_list = file_handle.readlines()
    print(len(lines_list)," Lines counted")
    elf_sums = []
    sumblock = []
    for i in range(0,len(lines_list)):
        if lines_list[i] != "\n":
            sumblock.append(int(lines_list[i].split("\\")[0].rstrip()))
        elif lines_list[i] == "\n":
            elf_sums.append(sum(sumblock))
            sumblock = []
print("Highest Elf-score: ",sorted(elf_sums)[-1])
print("Jeeeh Star1!")
sumscore = []
for j in range(-3,0):
    print(sorted(elf_sums)[j])
    sumscore.append(sorted(elf_sums)[j])   
print("Sum high elf-scores: ",sum(sumscore))
print("Star2 Yeah!")
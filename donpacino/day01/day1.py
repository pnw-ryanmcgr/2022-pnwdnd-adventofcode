filein = open("day1_puzzle1.txt",'r')
filein = filein.readlines()
filein = [x[:-1] for x in filein]







def list_of_elves(cal_list):
    master = []
    master.append([])

    elf = 0
    for i in range(len(cal_list)):
        
        if(len(cal_list[i]) > 0):
            master[elf].append(int(cal_list[i]))
        else:
            elf+=1
            master.append([])

    return master

def get_cals_list(inputs):
    out = []
    for i in inputs:
        out.append(sum(i))
    return out


def top_x_cals(inputs,count):
    inputs.sort(reverse=True)
    out=0
    for i in range(count):
        out+=inputs[i]
    return out

master_list = list_of_elves(filein)

cals_list = get_cals_list(master_list)
top3elfcals = top_x_cals(cals_list,3)

print(max(cals_list))
print(top3elfcals)


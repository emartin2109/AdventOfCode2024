import re
print(sum(int(nbr1)*int(nbr2)for nbr1,nbr2 in re.findall(r"mul\((\d+),(\d+)\)",''.join(re.findall(r"do\(\)(.*?)don't\(\)","do()"+open('i').read().replace('\n','')+"don't()")))))
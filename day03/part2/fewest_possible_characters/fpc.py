import re

r=re.findall;print(sum(int(a)*int(b)for a,b in r(r"mul\((\d+),(\d+)\)",''.join(r(r"do\(\)(.*?)don't\(\)","do()"+open('i').read().replace('\n','')+"don't()")))))

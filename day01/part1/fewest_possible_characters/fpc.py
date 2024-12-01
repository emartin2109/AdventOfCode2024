import re
import numpy as n
a,b=map(lambda x:n.array(sorted(map(int,re.findall(x,open("i").read())))),[r"\d+ +",r" +\d+"])
print(sum(abs(a-b)))
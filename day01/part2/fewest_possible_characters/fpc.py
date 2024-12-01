import re
a,b=map(lambda x:sorted(map(int,re.findall(x,open("i").read()))),[r"\d+ +",r" +\d+"])
print(sum(x*b.count(x)for x in a))
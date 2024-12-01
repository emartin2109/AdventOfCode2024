import re as r
a,b=map(lambda x:sorted(map(int,r.findall(x,open("i").read()))),[r"\d+ +",r" +\d+"])
print(sum(i*b.count(i)for i in a))

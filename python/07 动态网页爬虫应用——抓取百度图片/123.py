import re
s="abcdabab"
# reg=r"(ab)+"
reg=r"(ab)+$"
print(re.search(reg,s))
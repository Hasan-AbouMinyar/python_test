import re

text = "Hasan Abouminyar is a Dev of Software engeaneer"

# result = re.findall("hasan",text, re.IGNORECASE)
# print(result)

s = re.search("D",text)
print(s.start())    

me = re.sub("a","A",text)
print(me)
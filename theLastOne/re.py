import re

text = "Hasan Abouminyar is a Dev of Software engeaneer"

# result = re.findall("hasan",text, re.IGNORECASE)
# print(result)

s = re.search("a",text, re.IGNORECASE)
print(s)    
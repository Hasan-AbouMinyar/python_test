import re

text = "h.hasan@ga22mil.com"

m = re.search(r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|ly)", text)

if m:
    print("Valid email found:", m.group())
else:
    print("No valid email found")
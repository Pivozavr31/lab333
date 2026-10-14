s = "()[]{}"
while "()" in s or "[]" in s or "{}" in s:
    s = s.replace("()", "").replace("[]","").replace("{}","")
is_valid = s == ""
print(is_valid)
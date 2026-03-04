# flag.py
# Flag stored as ASCII numbers
flag_codes = [66, 65, 83, 73, 83, 123, 72, 69, 76, 76, 79, 95, 80, 89, 84, 72, 79, 78, 125]
flag = "".join([chr(c) for c in flag_codes])
print(flag)
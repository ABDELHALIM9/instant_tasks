import re
with open("data.text","r")as file:
    f=file.read()
    print("this is the data: \n",f)
    pattern_emails= r"[a-zA-Z0-9.+]+@[a-zA-Z0-9]+.[a-zA-Z0-9.]+"
    pattern_names = r"Name:\s([a-zA-Z]+\s+[a-zA-Z]+)"
    pattern_phones = r"\+\d{1} \(\d{3}\) \d{3}-\d{4}"
    names= re.findall(pattern_names, f)
    emails=re.findall(pattern_emails,f)
    phones_numbers= re.findall(pattern_phones, f)
    print("this is the phones numbers:\n",phones_numbers)
    print("this is the emails numbers:\n",emails)
    print("this is the full names numbers:\n",names)

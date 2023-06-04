x = input()
y = ""
if "meth" in x:
    y = "."
elif "eth" in x:
    y = "/"
elif "prop" in x:
    y = "/\\"
elif "but" in x:
    y = "/\\/"
elif "pent" in x:
    y = "/\\/\\"
elif "hex" in x:
    y = "/\\/\\/"
elif "hept" in x:
    y = "/\\/\\/\\"
elif "oct" in x:
    y = "/\\/\\/\\/"
elif "non" in x:
    y = "/\\/\\/\\/\\"
elif "dec" in x:
    y = "/\\/\\/\\/\\/"

if "ene" in x:
    y = "/" + y
print(y)
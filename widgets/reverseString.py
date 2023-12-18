string = "string"


for i in range(len(string)):
    c = -1
    string.replace(string[i], string[(c-i)])

print(string[-1])
letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
string = ""
inp = input()

out = ""
prev_l = ''
for l in inp:
    if l in letters and prev_l in numbers:
        out += '\n'
    out += l
    prev_l = l

out = out.replace("+", " tighten ")
out = out.replace("-", " loosen ")
print(out)
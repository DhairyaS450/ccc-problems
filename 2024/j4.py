original = input() + '$'
result = input() + '$'
alphabet = "abcdefghijklmnopqrstuvwxyz"

quiet = '-'
silly = ['-', '-']

#The character that only exists in the second string must be the result of the silly key
for c in alphabet:
    if c in result and c not in original: 
        silly[1] = c 

i = 0
j = 0

while i < len(original) and j < len(result):
    if original[i] == result[j]: #same letter, no need to do anything
        i += 1
        j += 1
        continue

    if result[j] == silly[1]: #s[i] must be the original character
        silly[0] = original[i]
        i += 1
        j += 1
    else: #result is not the silly key, so it must be the quiet key
        quiet = original[i]
        i += 1

print(*silly)
print(quiet)
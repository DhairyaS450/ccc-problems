import re
rule1 = input().split()
rule2 = input().split()
rule3 = input().split()
inp = input().split()
moves = int(inp[0])
starting = inp[1]
ending = inp[2]

# Precompile regexes
pattern1 = re.compile(rule1[0])
pattern2 = re.compile(rule2[0])
pattern3 = re.compile(rule3[0])

def find_all_possibilities(current_word):
    rule1_possibilities = [(1, rule1[1], match.start(), match.end()) for match in pattern1.finditer(current_word)]
    rule2_possibilities = [(2, rule2[1], match.start(), match.end()) for match in pattern2.finditer(current_word)]
    rule3_possibilities = [(3, rule3[1], match.start(), match.end()) for match in pattern3.finditer(current_word)]
    possibilities = rule1_possibilities + rule2_possibilities + rule3_possibilities

    new_words = set()
    for possibility in possibilities:
        new_word = current_word[:possibility[2]] + possibility[1] + current_word[possibility[3]:]
        new_words.add((possibility[0], possibility[2] + 1, new_word))

    return new_words

# print(find_all_possibilities("BAA"))

visited = set()
found = False
def search_sequence(sequence, current_word, moves):
    global found
    if moves == 0 or found:
        return
    if (current_word, moves) in visited:
        return
    visited.add((current_word, moves))
    
    possibilities = find_all_possibilities(current_word)
    for possibility in possibilities:
        if possibility[2] == ending:
            found = True
            sequence.append(possibility)
            for step in sequence:
                print(step[0], step[1], step[2])
            return
        new_sequence = sequence + [possibility]
        search_sequence(new_sequence, possibility[2], moves - 1)

search_sequence([], starting, moves)
shelf = input()
def count(shelf):
    l_cnt = shelf.count("L")
    m_cnt = shelf.count("M")
    s_cnt = shelf.count("S")
    return [l_cnt, m_cnt, s_cnt]
l_cnt, m_cnt, s_cnt = count(shelf)
l_section = count(shelf[:l_cnt])
m_section = count(shelf[l_cnt:l_cnt+m_cnt])
s_section = count(shelf[l_cnt+m_cnt:l_cnt+m_cnt+s_cnt])
total_swaps = 0
single_swaps = min(l_section[1], m_section[0]) + min(l_section[2], s_section[0]) + min(m_section[2], s_section[1])

s = 0
if l_section[1] < m_section[0]:
    s = l_section[1]
else:
    s = m_section[0]
l_section[1] -= s
m_section[0] -= s
l_section[0] += s
m_section[1] += s

s = 0
if l_section[2] < s_section[0]:
    s = l_section[2]
else:
    s = s_section[0]
l_section[2] -= s
s_section[0] -= s
l_section[0] += s
s_section[2] += s

s = 0
if l_section[2] < s_section[0]:
    s = l_section[2]
else:
    s = s_section[0]
l_section[2] -= s
s_section[0] -= s
l_section[0] += s
s_section[2] += s

double_swaps = 2 * (l_section[1] + l_section[2])
print(single_swaps + double_swaps)
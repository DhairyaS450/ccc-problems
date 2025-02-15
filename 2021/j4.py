shelf = input()
def count_books(shelf):
    l_count = 0
    m_count = 0
    s_count = 0
    for book in shelf:
        if book == 'L':
            l_count += 1
        elif book == 'M':
            m_count += 1
        else:
            s_count += 1
    return [l_count, m_count, s_count]

# First count the number of books of each size
l_count, m_count, s_count = count_books(shelf)

# Create the sections for the books
l_section = shelf[:l_count]
m_section = shelf[l_count:l_count + m_count]
s_section = shelf[l_count + m_count:]

# Count the number of each type of book in each section
l_section_books = count_books(l_section)
m_section_books = count_books(m_section)
s_section_books = count_books(s_section)

# Make the swaps that correct 2 books (L in M section + M in L section, M in S section + S in M section, L in S section + S in L section)
l_m_swaps, s_m_swaps, s_l_swaps = min(m_section_books[0], l_section_books[1]), min(s_section_books[1], m_section_books[2]), min(s_section_books[0], l_section_books[2])

# Update the count of each section after making the swaps
l_section_books[1] -= l_m_swaps
m_section_books[0] -= l_m_swaps
l_section_books[0] += l_m_swaps
m_section_books[1] += l_m_swaps

m_section_books[2] -= s_m_swaps
s_section_books[1] -= s_m_swaps
m_section_books[1] += s_m_swaps
s_section_books[2] += s_m_swaps

s_section_books[0] -= s_l_swaps
l_section_books[2] -= s_l_swaps
s_section_books[2] += s_l_swaps
l_section_books[0] += s_l_swaps

# Count the remaining swaps needed
double_swaps = 2 * (l_section_books[1] + l_section_books[2])

swaps = l_m_swaps + s_m_swaps + s_l_swaps + double_swaps
print(swaps)
def max_sunny_streak(days):
    n = len(days)
    max_streak = 0
    foundP = False

    for i in range(n):
        if days[i] == 'P':
            foundP = True
            # Count S's to the left
            left = 0
            j = i - 1
            while j >= 0 and days[j] == 'S':
                left += 1
                j -= 1

            # Count S's to the right
            right = 0
            j = i + 1
            while j < n and days[j] == 'S':
                right += 1
                j += 1

            candidate = left + 1 + right
            max_streak = max(max_streak, candidate)

    # If no P exists, we must flip one S to a P
    if not foundP:
        max_streak = n - 1

    return max_streak

num_of_days = int(input())
history = [input() for day in range(num_of_days)]
print(max_sunny_streak(history))
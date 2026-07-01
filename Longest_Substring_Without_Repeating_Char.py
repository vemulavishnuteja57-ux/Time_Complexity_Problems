s = "abcabcbb"

longest = 0

for i in range(len(s)):
    seen = ""

    for j in range(i, len(s)):
        if s[j] in seen:
            break

        seen += s[j]

    if len(seen) > longest:
        longest = len(seen)

print(longest)
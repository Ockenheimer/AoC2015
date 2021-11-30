# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
# and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter,
# even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?


file = open("days/test", "r").readlines()

nice = 0

for line in file:
    # if min two vowels
    vowel_counts = {}
    for vowel in "aeiou":
        count = line.count(vowel)
        vowel_counts[vowel] = count
    counts = vowel_counts.values()
    if sum(counts) > 2:
        # if two touching letters
        doubleLetter = 0
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                doubleLetter = 1
        if doubleLetter == 1:

            # if not containing "ab", "cd", "pq", "xy"
            naughtyWords = ["ab", "cd", "pq", "xy"]
            if not "ab" in line and not "cd" in line and not "pq" in line and not "xy" in line:
                nice += 1
        #         print(line.strip() + " is nice")
        #     else:
        #         print(line.strip() + " naughty wording")
        # else:
        #     print(line.strip() + " no double letter")
    #else:
        #print(line.strip() + " not enough vowels")

print(nice)

nice2 = 0
doubleLetters = 0
for i in range(len(line) - 3):
    j: int
    for j in range(i+2, (len(line)-3)):
        if line[i] + line[i+1] == line[j] + line[j+1]:
            doubleLetters = 1
if doubleLetters == 1:
    xyxLetter = 0
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            xyxLetter = 1
    if xyxLetter == 1:
        nice2 += 1

print(nice2)
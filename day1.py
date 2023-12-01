XS = []
with open("test.txt", "r") as file:
    wynik = 0
    n_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in file:
        XS.append(line.split())

        s = line.strip()

        first_digit = None
        for i in range(len(s)):
            if s[i].isdigit():
                first_digit = s[i]
                break
            for word in n_dict:
                if s[i:].startswith(word):
                    first_digit = n_dict[word]
                    break
            if first_digit:
                break

        last_digit = None
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                last_digit = s[i]
                break
            for word in n_dict:
                if s[i:].startswith(word):
                    last_digit = n_dict[word]
                    break
            if last_digit:
                break

        calib = int(first_digit + last_digit)
        wynik += calib

print(wynik)


wynik = 0
to_add = []
for x in range(len(XS)):
    for y in XS[x]:
        for letter_pos in range(len(y)):
            if y[letter_pos].isdigit():
                to_add.append(y[letter_pos])
                break

        for letter_pos in reversed(y):
            if letter_pos.isdigit():
                to_add.append(letter_pos)
                break


def create_numbers_in_pairs(lst):
    return ["".join(lst[i : i + 2]) for i in range(0, len(lst), 2)]


to_add = create_numbers_in_pairs(to_add)

for i in to_add:
    wynik += int(i)

print(wynik)

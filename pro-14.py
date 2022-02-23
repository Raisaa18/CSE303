def pallindrome_checker_146(line):
    line = line.lower()
    if line == line[::-1]:
        return 1


line = str(input("Enter a word: "))

if pallindrome_checker_146(line) == 1:
    print(line, "is a pallindrome word")
else:
    print(line, "is not a pallindrome word")
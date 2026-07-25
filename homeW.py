# String operations using match-case

s = input("Enter a string: ")

print("\n1. Reverse")
print("2. Palindrome check")
print("3. Count words (using logic)")
print("4. Convert to UPPER (manual)")
print("5. Convert to lower")
print("6. Swap case")
print("7. Sort string characters")

ch = int(input("Enter your choice: "))

match ch:
    case 1:
        rev = ""
        for i in range(len(s)-1, -1, -1):
            rev += s[i]
        print("Reversed string:", rev)

    case 2:
        if s == s[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

    case 3:
        count = 0
        for i in range(len(s)):
            if (i == 0 and s[i] != ' ') or (s[i] != ' ' and s[i-1] == ' '):
                count += 1
        print("Total words:", count)

    case 4:
        result = ""
        for ch1 in s:
            if ch1 >= 'a' and ch1 <= 'z':
                result += chr(ord(ch1) - 32)
            else:
                result += ch1
        print("Uppercase string:", result)

    case 5:
        result = ""
        for ch1 in s:
            if ch1 >= 'A' and ch1 <= 'Z':
                result += chr(ord(ch1) + 32)
            else:
                result += ch1
        print("Lowercase string:", result)

    case 6:
        result = ""
        for ch1 in s:
            if ch1 >= 'a' and ch1 <= 'z':
                result += chr(ord(ch1) - 32)
            elif ch1 >= 'A' and ch1 <= 'Z':
                result += chr(ord(ch1) + 32)
            else:
                result += ch1
        print("Swapcase:", result)

    case 7:
        result = "".join(sorted(s))
        print("Sorted string:", result)

    case _:
        print("Invalid choice")


def is_palindrome(line: str) -> bool:
    chars = [c.lower() for c in line if c.isalpha()]
    return chars == chars[::-1]

print(is_palindrome(input().strip()))

# Problem 76: Calculate string similarity (common characters)
# Find and fix the error

def string_similarity(str1, str2):
    return len(set(str1)& set(str2))

s1 = "hello"
s2 = "world"
print(f"Common characters: {string_similarity(s1, s2)}")

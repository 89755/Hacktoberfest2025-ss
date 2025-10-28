def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

# Example
word1 = "Listen"
word2 = "Silent"
if are_anagrams(word1, word2):
    print("✅ They are anagrams.")
else:
    print("❌ Not anagrams.")

ransomNote = "aa"
magazine = "aab"
count = 0
for char in ransomNote:
    if char in magazine:
        count += 1

if count == len(ransomNote):
    print("True")
else:
    print("False")
       


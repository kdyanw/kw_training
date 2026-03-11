phrase = input("Enter a phrase: ")
character = input("Enter a character: ")
# Count how many times the character appears
count = phrase.count(character)

# Print result with correct plural form
if count == 1:
    print(count, character)
else:
    print(count, character + "'s")
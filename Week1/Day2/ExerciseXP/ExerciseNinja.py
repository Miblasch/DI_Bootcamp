

# Exercise 4: How many characters in a sentence?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. \
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. \
Excepteur sint occaecat cupidatat non proident, \
sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))


# Exercise 5: Longest word without a specific character
longest_sentence = ""

while True:
    sentence = input('Type a sentence without the letter "a" (or type "stop" to quit): ')

    if sentence.lower() == "stop":
        break

    if "a" in sentence.lower():
        print('Oops, that sentence contains the letter "a". Try again!')
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print(f"Congratulations! You set a new longest sentence ({len(sentence)} characters).")
    else:
        print("That sentence wasn't longer than your current record. Try again!")

print(f"\nYour longest sentence without the letter 'a' was: \"{longest_sentence}\"")
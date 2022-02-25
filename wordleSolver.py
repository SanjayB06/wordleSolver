from english_words import english_words_set as wordList

wordList = [x.lower() for x in wordList if len(x) == 5]

letterCount = {'e': 1679, 'a': 1550, 'r': 1126, 'o': 1053, 'l': 1004, 's': 958, 't': 947, 'i': 947, 'n': 869, 'c': 656, 'u': 611, 'y': 585, 'h': 535, 'd': 513, 'm': 467, 'p': 466, 'b': 423, 'g': 410, 'k': 298, 'f': 274, 'w': 232, 'v': 195, 'z': 72, 'x': 67, 'j': 58, 'q': 38}

wordByLetter = {}
wordListNoRepeats = ["".join(set(word)) for word in wordList]



for index in range(len(wordListNoRepeats)):
	constant = 0
	word = wordListNoRepeats[index]
	for letter in word:
		try:
			constant += letterCount[letter]
		except:
			continue
	realWord = wordList[index]
	wordByLetter[realWord] = constant
wordByLetter =  {k: v for k, v in sorted(wordByLetter.items(), key=lambda item: item[1],reverse = True)}
# result = input("What was the result ")
# attemptedWord = input("What word did you try ")
while True:
	result = input("What was the result? ").lower()
	if result in ["done","success","quit","q"]:
		break
	attemptedWord = input("What word did you attempt? ").lower()
	notIn = [attemptedWord[index] for index in range(5) if result[index] == "n"]
	In = {attemptedWord[index]:index for index in range(5) if result[index] == "y"}
	inButIdk = {attemptedWord[index]:index for index in range(5) if result[index] == "-"}
	wordByLetter = {k: v for k, v in wordByLetter.items() if (not any(char in k for char in notIn) and all(k[In[char]] == char for char in In) and all(k[inButIdk[char]] != char for char in inButIdk)) }
	print(wordByLetter)

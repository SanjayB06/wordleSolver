from data import wordByLetter

while True:
	attemptedWord = input("What word did you attempt? ").lower()
	result = input("What was the result? ").lower()
	if result in ["done","success","quit","q"]:
		break
	notIn = [attemptedWord[index] for index in range(5) if result[index] == "n"]
	In = {attemptedWord[index]:index for index in range(5) if result[index] == "y"}
	inButIdk = {attemptedWord[index]:index for index in range(5) if result[index] == "-"}
	wordByLetter = {k: v for k, v in wordByLetter.items() if (not any(char in k for char in notIn) and all(k[In[char]] == char for char in In) and all(k[inButIdk[char]] != char for char in inButIdk) and all(char in k for char in inButIdk)) }
	print(list(wordByLetter.keys())[:10])

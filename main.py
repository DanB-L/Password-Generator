import random
def main():
	lowerAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	higherAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	specialChars = [',', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ':', ';', '<', '>', ']', '?', '/', '|']
	optionLst = []


	length = int(input("Enter the length of your desired password: "))
	tmpLength = length 
	uppercase = int(input("How many uppercase letters would you like?: "))
	tmpLength = tmpLength - uppercase

	while uppercase != 0:
		optionLst.append("uppercase")
		uppercase = uppercase - 1
	
	number = int(input("How many numbers would you like?: "))
	tmpLength = tmpLength - number
	while number != 0:
		optionLst.append("number")
		number = number - 1
	
	special = int(input("How many special characters would you like"))
	tmpLength = tmpLength - special
	while special  != 0:
		optionLst.append("special")
		special = special - 1

	while True:
		if tmpLength != 0:
			optionLst.append("lowercase")
			tmpLength = tmpLength - 1
		else:
			break
	password = ""
	random.shuffle(optionLst)
	running = True
	while running == True:
		for i in optionLst:
			if i == "lowercase":
				tmpChar = ""
				tmpChar = random.choice(lowerAlpha)
				password = password + tmpChar
			elif i == "uppercase":
				tmpChar = random.choice(higherAlpha)
				password = password + tmpChar
			elif i == "special":
				tmpChar = random.choice(specialChars)
				password = password + tmpChar
			elif i == "number":
				tmpChar = random.choice(numbers)
				password = password + tmpChar
			else:
				print("ERROR: INVALID OPTION STORED")
		print(password)
		running = False
main()

coins = 0

print ("You have 0 coins.")

answer = input("Do you want another? ")

while True:
	if answer.lower() == "yes":
		coins = coins + 1
		print (" You have " + str(coins) + " coins. ")
		answer = input("Do you want another? ")
		
	if answer.lower() == "no":
		break

import random 
usercount = 0 
computercount = 0

print("---------Welcome to the Rock,paper,Scissor Game----------\n ")

Choices = ["Rock","Paper","Scissors"]
def getCompChoice():
	b = random.randint(0,2)
	print("Computer Chose ",Choices[b])
	return b

def getUserChpoice():
	a = int(input("Enter Your Input "))
	print("\n")
	print("Human Chose ",Choices[a])
	return a
round = 1
while(True):
	print("Enter a number for Round ",round)
	print("0. Rock")
	print("1. Paper")
	print("2. Scissor")
	userChoice = getUserChpoice()	
	compChoice = getCompChoice()

	if (userChoice == compChoice):
		usercount = usercount 
		computercount =computercount 
		print("\n---Scores---")
		print("UserScore ",	usercount,"CompScore",computercount)
		print("Nice, Human Block the Hit")
		print("\n")
	elif (userChoice == 0 and compChoice == 2):
		usercount = usercount +1
		computercount =	computercount
		print("\n---Scores---")
		print("UserScore ",	usercount,"CompScore",computercount)
		print("Ugh!!...... Human Won ")
		print("\n")
	elif (userChoice == 1 and compChoice == 0):
		usercount = usercount +1
		computercount =	computercount
		print("\n---Scores---")
		print("UserScore ",	usercount,"CompScore",computercount)
		print("Ugh!!...... Human Won ")
		print("\n")
	elif (userChoice == 0 and compChoice == 1):
		usercount = usercount +1
		computercount =	computercount
		print("\n---Scores---")
		print("UserScore ",	usercount,"CompScore",computercount)
		print("Ugh!!....... Human Won ")
		print("\n")
	else:
		usercount = usercount 
		computercount =computercount+1
		print("\n---Scores---")
		print("UserScore ",	usercount,"CompScore",computercount)
		print("Yes....... I defeat Human ")
		print("\n")
	if usercount == 5 or computercount ==5:
		if usercount ==5:
			print("Humans defeat the AI")
		elif computercount ==5:
			print("AI defeats Human \n --------Earth has been Conquered-------")
		break	

	round =round+1



    











	

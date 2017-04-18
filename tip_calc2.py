bill = float(input (" Type the bill amount: "))

service = input(" Type the level of service: good, fair or bad: ")

split = float(input ("Split how many ways? "))



if service == "good":
	tip = 0.2 * bill
	total = bill + tip
	totalpp = total / split
	
	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))
	print ("Amount per person: " + "{:.2f}".format(totalpp))

elif service == "fair":
	tip = 0.15 * bill
	total = bill + tip
	totalpp = total / split

	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))
	print ("Amount per person: " + "{:.2f}".format(totalpp))

elif service == "bad":
	tip = 0.10 * bill
	total = bill + tip
	totalpp = total / split

	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))
	print ("Amount per person: " + "{:.2f}".format(totalpp))





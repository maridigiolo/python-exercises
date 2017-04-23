bill = input (" Type the bill amount: ")

service = input(" Type the level of service: good, fair or bad: ")

bill = float (bill)


if service == "good":
	tip = 0.2 * bill
	total = bill + tip
	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))

elif service == "fair":
	tip = 0.15 * bill
	total = bill + tip
	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))

elif service == "bad":
	tip = 0.10 * bill
	total = bill + tip
	print (" Tip Amount: $" + "{:.2f}".format(tip))
	print (" Total Amount: $" + "{:.2f}".format(total))
	




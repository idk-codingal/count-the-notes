amount = int(input("Please enter the amount to withdraw :"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("Notes of 100$" ,note_1)
print("Notes of 50$" ,note_2)
print("Notes of 10$" ,note_3)

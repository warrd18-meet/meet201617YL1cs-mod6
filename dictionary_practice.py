#Module 6, Part 5: Practice with dictionaries here


my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###
num = my_phonebook["Statue of Liberty"] 
###
#Print the variable, num
###
print(num) 
###
#Change the value of the Ghostbusters' phone number to 2125559876
###
my_phonebook["Ghostbusters"]= 2125559876
#Here's an empty dictionary
your_phonebook={}

###
#Add 5 values to it like this
#your_phonebook['key']=value
###
your_phonebook={}
your_phonebook['food1']="chocolate"
your_phonebook['food2']="nutella"
your_phonebook['food3']="peanutbutter"
your_phonebook['food4']="jelly"
your_phonebook['food5']="biscuit"


####Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

sequence_of_keys= your_phonebook.keys()
#Loop over this sequence with a for loop
#using syntax like
for key in sequence_of_keys:
    print (key + str(your_phonebook[key]))
    
#for key in sequence_of_keys :
#    #Do stuff

#Use the loop to print to the shell the key and value
#of every element in the dictionary
###


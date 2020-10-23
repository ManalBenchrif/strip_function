#strip() is an inbuilt function in Python programming language that returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
#Syntax: string.strip([chars])
#Parameter: 
#There is only one optional parameter in it:
    #1)chars - a string specifying 
    #the set of characters to be removed. 
    #If the optional chars parameter is not given, all leading and trailing whitespaces are removed from the string.
    
str1 = 'manal benchrif, manal student ,manal'
# Print the string without striping. 
print(str1) 

# String whose set of characters are to be 
# remove from original string at both its ends. 
str2 ='manal'

# Print string after striping str2 from str1 at both its end. 
print(str1.strip(str2)) 

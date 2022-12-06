# chapter 3      
'''                                                string                            '''

name ="bishal"
print(type(name))

greeting="goodmorning "
print(name,greeting)

print(greeting[0:6])

print(name[0:3:1])

a="amazing"
print(a[1:6:2])


story= "once upon a time a boy name bishal went to study python in librabry where he meet a very  good person"
print(len(story))
print(story.endswith("y"))
print(story.count("o"))
print(story.capitalize())
print(story.find("bishal"))
print(story.replace("bishal","divya"))



# Escape sequence

story = "Bishal is good.\nHe is\t  very good"
print(story)


'''                         PRACTICE QUESTION                         '''

#Write a python program to display a user entered name followed by good afternoon using input() function
       
a=input("enter your name\n")
greetings = "Good Afternoon"
print(greetings,a)

#write a program to fill in a letter template given below with name and date.
     
                
story=('''dear <|Name|,> 
     congratulation!
     you are selected!
     Team Microsoft     
     have  a wonderfull journey ahead !

     <|Date|>      
     ''')      


name=input("enter your name\n")
date=input("enter today date\n")
story=(story.replace("<|Name|>",name))
story=(story.replace("<|Date|>",date))

print(story)                     

# write a program to find a double space

story=input(" write a story")
doublespaces=(story.find("  "))
print(doublespaces)

#wrie a program to find a single spaces
st = input(" story")
st=(st.find(" "))
print(st)

#write a program to format the following letter using escape sequence character

letter="dear Harry , this python course is nice. Thanks !"
print(letter)

formatted_letter="dear Harry,\n \tthis python course is nice.\nThanks !"
print(formatted_letter)
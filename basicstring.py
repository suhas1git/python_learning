#how to print statement 1#
#my_string = "i am siri"
#print(my_string)
#2nd type of printing
#print("hello world")

#input() function is a simple way to prompt the user for some input 
#here between statement errors are below print statements while adding 2 +s in one print it shows error while we give 1+ in 2 input statemts it thows error 
#brand = input("mention any kind of brand:")
#print(brand+"wow it is good brand" )
#age = input("how old are u?")
#print("you alredy "+ str(age)+"years old"+brand)
#here while running we gave the file string it thows an erroe like basic string .py gives error
#and for string bracres ()are optional and we mention str ot string anything is fine
#string = ("siri how are")
#print("the length of the string is:",len(string))

#filter()function
#always mention true false conditons first caps letter and make sure small ans caps 


#ages =[18,19,20,16]
#ef myFunc(x):
 ##     return True
   #    return False
    
#adult = filter(myFunc, ages)
#for x in adult:
 #   print(x)

#ages = [5, 12, 17, 18, 24, 32]

#def myFunc(x):
 # if x < 18:
  #  return False
  #else:
   # return True

#adults = filter(myFunc, ages)

#for x in adults:
 # print(x)

#defining a function
#def name():
 #   print("what is your name")

    #variables
    #variable store date values python has no command for decleare a variable
    

#x = 5
#y = "siri"
#print(x,y)
#print(y)  

#casting 
#x = int(3)
#y = str(4)
#z = float(5)
#print(x,y,z)
# python variable nameing 
#name start with lowercase, variable cannot start with number, it only contain alpha numeric value underscore (A-z,0-9,_), a variavle cannot be any of the python keyword.
#Myvar = "siri"
#0var = "siri"
#_myvar = "siri"these 3 statements throw error

#mYvar = "siri"
#print(mYvar)

# assign multiple values to variables
#x = y = z ="siri"
#print(x,y,z)

# unpacking 
#you have a collection of values list or tuple python allows to extract the values into variables this is called unpacking
#names = ["siri","sravani","venky"]
#x, y, z = names
#print(x,y,z)
# output variables
#x = "siri"
#y = "is"
#z = "very kind"
#print(x,y,z)
#print(x+y+z) we use both ways
# when you combime string and a number python will give you error
#x = 5
#y = "siri"
#print(x+y)its error but in the place of + operator you use , you get the result
#x = 3
#y = "siri"
#print(x,y)
#global variables variables that are created outside of a function global variable can be used by everyone both inside of functions and out side 
#now we creating variable outside of a function and use it inside the function 
#x = "sravani husband"

#def myfunc():
 #   x = "is good boy"
  #  print("venky"+x)
#myfunc()
#print("siri"+x)

s=input("enter some string:")
i=0
for x in s:
    print("the character present  index{}and atnegative index {}is {}".format(i,i-len (s),x))
    i=i+1

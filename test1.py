#1.History of python?
     #Father of python= Gudio Van Rossum(Netherlands)
       #1989(Started at centrum wiskunde &Information in the Netherlands)
     #First Released
        #python version 0.9-->1991
        #python 1.0-->1994
        #python 2.0--->Released in 2000(Introduced list comprehensions and garbage collection
        #python 3.0-->2008(Improve syntax and Unicode support
     #Modern python(3.x)
         #Actively Developed and widelybused in web dev,data science,automation etc..


#2.IDE?
    #IDE(Integrated Development Environment)
      #IDE is a software application.That provide a comprehensive set of tools.It combine various features like text,editor,complier,debug.
   #key features of an IDE
      #CodeEditor
        #The core component of an IDE
        #Use to write code with features like syntax,highlighting,auto-indentation and auto completion
   #Complier/Interpreter
      #complier(for c/c++)or interpreter(for python)Translate the code into machine language
   #Debugger
      #Helps find and fix bug by running the code step-by-step
   #Version Control Integratic
      #Most ModernIDEs offer integration with version control system like git to help you manage your codebase and collobrate with other developer
   #python.IDEs
     #1)pycharm
          #powerful feature like code completion,debugging and testing
     #2)VScode
         # Light weigth customized and extensible .It support through extension
     #3)spyder
         #Built for data science and scientific computing with an integrated ipython console and variable explore
     #4)Jupyter
        #Interactive environment for data analysis visualization and machine learnings

 #3.Type of tokens?  
    #In python tokens are the smallest unit in a program that have meaning to complier or intepreter.There are five types of tokens
    
       #1)Keyword
             #There are reserved words that have a special meaning in python.They cannot be used as identifier(variablename,functionname etc...
       #2)Identifier
             #Identifiers are names used to identify variables, functions, classes, modules, and objects.
         #Rules:

            #Must start with a letter (A–Z or a–z) or an underscore (_)
            #Can be followed by letters, digits (0–9), or underscores 
            #Cannot be a keyword
         #Ex
           #name, total, _temp, myFunction, ClassName

       #3)Literals
                 Literals are fixed values assigned to variables or constants. 
                   #Types of literals:
                      #String literals: 'hello', "world", '''multi-line'''
                      #Numeric literals: 10, 3.14, 0b101 (binary), 0o77 (octal), 0x1A (hex)
                      #Boolean literals: True, False
                      #Special literal: None
        
        #4)Operators
               #Operators are symbols that perform operations on variables and values. 
                  #Types:
                      #Arithmetic operators: +, -, *, /, %, //, **
                      #Comparison operators: ==, !=, >, <, >=, <=
                      #Logical operators: and, or, not
                      #Assignment operators: =, +=, -=, *=, etc.
                      #Bitwise operators: &, |, ^, ~, <<, >>
                      #Membership operators: in, not in
                      #Identity operators: is, is not

       #5)Punctuators (Separators or Delimiters)
            #These are symbols that help structure the Python code.
               #Examples:
                       # (), [], {} — grouping and indexing
                       # :, ,, . — colons, commas, dots
                       # =, -> — assignment and function return types
                       # @ — decorators
                       # ; — separates statements (rarely used)




#4. Datatypes?

   #datatypes in python

     #1)NumericTypes
           #These types are used when you’re working with numbers.
        #a)int (Integer)
             #Wholenumbers
                #Ex: a = 10, b = -5

        #b)float(Floating point)
           #Numbers with a decimal point
               #Ex: x = 3.14, y = -0.01
        #c)complex
            #Used for complex numbers (with imaginary part j)
                #Ex: z = 2 + 3j
 
      #2) Sequence Types 
          #These store multiple values in an order.
             #a.str (String)
               #Ex: name = "Alice"

            #b)list
                 # Acollection that is ordered and changeable
                    #Ex:fruits =['apple', 'banana', 'mango']

            #c.tuple
                #Like a list, but cannot be changed (immutable)
                   #Ex: colors = ('red', 'green', 'blue') 
            #d. range
                 #Generates a sequence of numbers
                    #Ex: range(0, 5) gives 0, 1, 2, 3, 4

      #3)Set Types
             #Unordered collections of unique items (no duplicates allowed).
                #a. set
                  #Ex: my_set = {1, 2, 3, 2} 
                      #output
                          #{1, 2, 3}

    #4) Dictionary
              #Stores key-value pair
                  #Ex:
                      #student = {
                                    "name": "dhachuu",
                                    "age": 20,
                                     "grade": "A"
                                  }
                                    print(student["name"])  
                                      # Output:
                                             #dhachuu
     #5)Boolean Type
          # True or False
             #ex
                  #a=10
                  #b=5
                  print(a > b)  
                     #Output: 
                      #True
     #6) NoneType
           #NoneType: Represents a null value, often used to indicate the absence of a value.
                #ex           
                  id = None
                  print(type(id)) 
                   #Output
                     #<class 'NoneType'>



#5.write the programme for the output?
	name: XXX
	age:22
	tamil:100
	eng:100
	maths:100
	s.s:100
	s:100

	total:500
	
	and find average?
            


  #Answer
      tamil=100
      eng=100
      maths=100
      socialscience=100
      science=100
      total=tamil+eng+maths+socialscience+science
      average=total/5
      print("total:",total)
      print("average:",average)
     
   #output
     total: 500
average: 100.0


#6. (5 & 12) & (2 | 6)
  #Answer

    #55

#7. (54 | 6 & 5) | (21 & 9)
   #Answer
     #output
        #4

#8. True or false. if it is false give the reason?
	1) a="name"
           a=12
           print(a)

	2) b="kalai""tamil"
	   print(b)

  #Answer
    #1)True
    #2)False
       #explain 
           #Incorrect syntax! The issue is lack of space or explicit concatenation between the two string literals.


#9.a=10
   b=2
   print(a/b+a%1)
     
   #Answer
     #output
     #5.0

#10. 5>>2 and 9<<3

  #Answer
   #1
   #72

#11.what is member ship operator give the example?

  #Membership operators in Python are used to test if a value is found within a sequence (such as lists, tuples, strings, or dictionaries). There are two membership        operators: in and not in.
  #in operator:
      This operator returns True if a value is present in the sequence, otherwise it returns False
   #list
       my_list = [1, 2, 3, 4, 5]
        print(3 in my_list)  
         #Output
         #True
        print(6 in my_list)  
       #Output
        #False

#string 
  my_string = "hello"
  print("e" in my_string)  
   #Output
     #True
  print("z" in my_string)  
   #Output
    #False

#tuple
  my_tuple = (10, 20, 30)
  print(20 in my_tuple)  
   #Output
   #True
  print(40 in my_tuple) 
   #Output
    #False

#dictonary
    my_dict = {"a":1, "b":2}
    print("a" in my_dict) 
     #Output
      #True
print("c" in my_dict) 
  #Output
  #False


#not in operator:
  This operator returns True if a value is not present in the sequence, otherwise it returns False

#list
  my_list = [1, 2, 3, 4, 5]
  print(3 not in my_list)  
    #Output
     #False
  print(6 not in my_list)  
   #Output
   #True

#string
   my_string = "hello"
   print("e" not in my_string)  
    #Output
    #False
    print("z" not in my_string) 
     #Output 
      #True

#tuple
    my_tuple = (10, 20, 30)
    print(20 not in my_tuple) 
      #Output
        #False
    print(40 not in my_tuple) 
       #Output
        #True

#12.Explain identity?

   #In Python, identity refers to the unique memory address of an object.You can check an object's identity using the id() function. 
   
    #ex:
       # Defining two variables with the same value
          a = 10
          b = 10
          print(id(a))  # Memory address of a
          print(id(b))  # Memory address of b

# Verifying identity comparison
  print(a is b)  # True because small integers are cached and have the same identity
#In Python, small integers and short strings are interned, meaning that they might have the same identity. 
 However, when working with mutable objects like lists, their identities differ

# lists
  x = [1, 2, 3]
  y = [1, 2, 3]

# identity
  print(id(x))  # Memory address of x
  print(id(y))  # Memory address of y

# Verifying identity comparison
  print(x is y)  # False because lists are mutable and stored separately


#13)output: hello hello hello hello hi hi hi hi------write a code.
       #Answer
         print(("hello " * 4) + ("hi " * 4))

#14.How to find the datatype and explain?
 	
	#In Python, you can determine the datatype of a variable using the type() function. 
	
	# Defining different types of variables
		 # Integer
                     num = 10
		 # String
                     text = "Hello" 
		 # Float 
                     decimal = 3.14
                 # Boolean
                      is_active = True
		 # List
                      items = [1, 2, 3]   

		print(type(num))      
                  # Output
                    #<class 'int'>
		print(type(text))     
                 # Output
                   #<class 'str'>
		print(type(decimal))  
                   # Output
                    #<class 'float'>
		print(type(is_active)) 
                  # Output
                   #<class 'bool'>
		print(type(items))    
                   # Output
                     #<class 'list'>

#15.convert the a='154' to integer?
    
#Answer
     a = '154'
     b= int(a)
     print(b_int)
      #output
       #154

   




  






















  


   


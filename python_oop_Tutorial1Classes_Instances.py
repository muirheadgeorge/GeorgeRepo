# Python Object-Oriented Programming
# Classes lets you logic group Data and Functions
# Easy to build upon and reuse code
#Data associated with a specific class is called an attribute
#Functions associated with a specifc class is called a method.
#Instance Variables can be unique for each instance
#Class Variables need to be the same for each instance. 
#Static Methods and Class Methods
#Regular Methods in a Class automatically take the Instance as the first argument.
#To change This so the class automatically takes the class as the first argument you add a decorator to the top of the instance called @classmethod

class AdultFare:
  num_of_fares = 0
  raise_amount = 1.04,  # Class Variable   

  
  
  def __init__(self,stop,price):
    self.stop = stop
    self.price = price #Constructor
    
    AdultFare.num_of_fares += 1
  def fullFare(self):
    return '{} {}'.format(self.stop,self.price) # Instance of the class


  def apply_raise(self):
      self.price = int(self.price * self.raise_amount) #Method of the class (function)
 
  @classmethod #This is called a decorator
  def set_raise(cls,amount):#cls referreds to the class variable name.
      cls.raise_amount = amount

AdultFare.set_raise(1.45)

fare_1 = AdultFare('St John\'s School',1.00) #Attribute of class(data)
fare_2 = AdultFare('St John\'s School',1.40)
fare_3 = AdultFare('St John\'s School',1.90)
fare_4 = AdultFare('St John\'s School',2.30)
fare_5 = AdultFare('St John\'s School',2.30)
fare_6 = AdultFare('St John\'s School',2.50)
fare_7 = AdultFare('St John\'s School',3.30)



print(AdultFare.raise_amount)

print(fare_5.raise_amount)



    
    







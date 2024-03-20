#!/usr/bin/env python3

class MyString:
  def __init__(self,value = ""):
    self.value = value
    
    # Value
  @property
  def value(self):
    return self._value
    
  @value.setter    
  def value(self,new_value):                        
    if (isinstance(new_value, str)):
      self._value = new_value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    if self.value[-1] in ["."]:
      return True
    else:
      return False    
    
  def is_question(self):
    if self.value[-1] in ["?"]:
      return True
    else:
      return False  
    
  def is_exclamation(self):
    if self.value[-1] in ["!"]:
      return True
    else:
      return False  
  
  def count_sentences(self):
    value_list = self.value.split()
    count = 0
    for value in value_list:
      if(value[-1] in [".","?","!"]):
        count+=1
    return count
    

word = 'hello hp vl'
word_list = word.split()


print(word_list)


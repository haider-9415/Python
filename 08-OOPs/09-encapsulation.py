"""
   we can craete methods and variables privet and protected and they are publically by default

   to make a variable or method protected, place single underscore 
   before it, after that we can access it in both inside and outside 
   of the class by using single underscore before it

   to make a variable or method private, place double underscore 
   before it, after that we can access it both inside and outside 
   of the class by using double underscore and the class name before it
"""

class mentor: 

    def __init__(self, mentor_name, mentor_email_id, mentor_contact):
        self._ment_name = mentor_name
        self.__ment_email_id = mentor_email_id
        self.ment_contact = mentor_contact
    
    def mentor_details(self): # to print details of __init__() inside the class
        return self._ment_name, self.__ment_email_id, self.ment_contact

ob_mentor = mentor('sudhanshu', 'abcd@pw.live', 1234567890)

# print(ob_mentor.ment_name) # it will give error, because, ment_name is protected

print("ob_mentor._ment_name --> ",ob_mentor._ment_name,'\n') # it will not give error, because, we have used '_' before it
print(".................................................................................\n")

# print(ob_mentor.ment_email_id) # it will give error, because, ment_email_id is private

# print(ob_mentor.__ment_email_id) # it will also give error, because, we can not access it like this


# we can access ment_email_id inside of the class
print("ob_mentor.mentor_details() --> ",ob_mentor.mentor_details(),'\n')
print(".................................................................................\n")

# to access privete variable outside of the class --> _class-name__variable-name
print("ob_mentor._mentor__ment_email_id --> ",ob_mentor._mentor__ment_email_id,'\n')
print(".................................................................................\n")


print('ob_mentor.__dict__ :\n',ob_mentor.__dict__)
print(".................................................................................\n")




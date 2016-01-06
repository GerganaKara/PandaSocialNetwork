from validate_email_address import validate_email

    

Class Panda:

    def __init__ (self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def __str__ (self):
        return "I am {} with email {} and gender {} ".format( self.__name, self__email, self__gender)

    def __repr__(self):
        return str(self)

    def get_name (self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def isMale(self):
        return self__gender.lower == "male"

    def isFemale(self):
        return self__gender.lower == "female"

    def __eq__(self, other):
        return self.__name == other.__name and self.__email == other.__email and self.__gender == other.__gender

    def __hash__(self):
        return hash(str (self.__name))

    def isEmailValid(self):
        return validate_email(self.__email)


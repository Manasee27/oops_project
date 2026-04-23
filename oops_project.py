class Chatbook:

    __user_id=0
    # There is only ONE copy of __user_id, no matter how many objects you create and many instances
    # its called class object

    def __init__(self):

        self.id = Chatbook.__user_id
        Chatbook.__user_id+=1
        # this is a way to access class variable
        self.__name="default_user"

        self.username = ''
        # self.username this is an instance variable, only applicable for one object
        self.password = ''
        self.loggedin = False
        self.menu()

    @staticmethod
    def getname():
        return Chatbook.__user_id
    
    @staticmethod
    def setname(val):
        Chatbook.__user_id =val
        return Chatbook.__user_id

    

    def menu(self):
        user_input = input("""Welcome to Chatbook, how to proceed?
1. Press '1' for signup
2. Press '2' to sign in
3. Press '3' to write a post
4. Press '4' to message a friend
5. Press any other key to exit
""")

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        else:
            # exit() this kills the entire python program
            return 
        # 'return' go back to caller (i.e., __init__)

    def signup(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("enter your password")
        self.username=email
        self.password=password
        print("You made an account successfully")
        self.menu()

    def signin(self):
        username=input("Enter your username: ")
        password = input("enter your password")

        if username ==self.username and password==self.password:
            print("you signed in successfully")
            self.loggedin=True
        else:
            print("try again")
        self.menu()


obj = Chatbook()
print("username",obj.username)
print(obj._Chatbook__name)
obj.setname(8)
print(obj.getname())
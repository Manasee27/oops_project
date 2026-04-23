class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

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
            exit()

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
print(obj.username)

class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

        def menu(self):
            user_input=input("""Welcome to Chatbook, how to proceed?
                             1. Press '1 for signup
                             2. Press '2' to sign in
                             3. Press '3' to write a post
                             4. Press '4' to message a friend
                             5. Press any other key to exit
                                                        
                             
                             """)
            if user_input=='1':
                pass
            if user_input=='2':
                pass           
            if user_input=='3':
                pass            
            else:
                exit
obj=chatbook()
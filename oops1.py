class employee:
    # special magic/dunder method - constructor
    def __init__(self):
        self.id= 123
        self.salary= 500000
        self.designation= 'software_dev'
        self.destination='USA'
        print('this line gets printed just by declaring the object')

    def travel(self,destination):
        print(f'employee is traveling to {destination}')

sam=employee()
print(type(sam))


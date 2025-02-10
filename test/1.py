import os

class push():
     def __init__(self):
        self.commit_message = str(input("message: "))
        m1 = f"'{self.commit_message}'"
        print(m1)

push()
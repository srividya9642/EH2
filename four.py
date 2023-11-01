class insufficientfundserror(Exception):
    def __init__(self,msg):
        self.msg=msg
acc_bal=600

def withdrawl (amount):
    if amount>acc_bal:
        try:
            raise insufficientfundserror  
            print(error)
        except:
            pass
    
    else:
       print("withdrawl and enjoy")

withdrawl (500)
print("good evening")

    


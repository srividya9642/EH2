#insufficient funds error(exception)
class insufficienterror:
    def __init__(self,msg):
        self.msg=msg
acc_bal=600

def withdrawl(amount):
    if amount>acc_bal:
       raise insufficientfundserror("buddy check your balance ")
    else:
        print("withdrawl and enjoy")

withdrawl(500)
print("good evening")
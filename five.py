class insufficientfundserror (exception):
    def __init__(self,msg):
        self.msg=msg
acc_bal=600
def withdrawl(amount):

    if amount>acc_bal:
       try:
           
           raise insufficientfundserror ("buddy check your bank balance")

       except ZeroDivisionError ("cant division by zero"):


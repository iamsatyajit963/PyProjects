class InvalidAccountException(Exception):
    pass
class Account:
    account_list=[1001,1002,1003,1004]
    def validate_account(self,account_id):
        status=0
        for acct_id in self.account_list:
            if(account_id==acct_id):
                status=1
                break
        if(status!=0):
            return True
        else:
            raise InvalidAccountException
try:
    account1=Account()
    account1.validate_account(1006)
    print("Valid account number")
except InvalidAccountException:
    print("Invalid account number")
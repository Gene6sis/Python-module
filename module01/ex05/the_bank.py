class Account(object):
    
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        
        if not isinstance(self.name, str) :
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        if not isinstance(new_account, Account) :
            return False
        # it can be appended to the attribute accounts
        if new_account in self.accounts :
            return False
        self.accounts.append(new_account)
        return True
    
    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not isinstance(origin, str) :
            return False
        if not isinstance(dest, str) :
            return False
        if not isinstance(amount, (float, int)) or amount < 0:
            return False
        
        o_account = next((account for account in self.accounts if account.name == origin), None)
        d_account = next((account for account in self.accounts if account.name == dest), None)

        if o_account is None : 
            return False
        if d_account is None :
            return False

        if (o_account.value - amount) < 0 :
            return False
        
        for account in (o_account, d_account) :
            # an even number of attributes,
            if not len(account.__dict__) % 2 :
                return False
            # an attribute starting with b,
            if (any([key.startswith('b') for key in account.__dict__])):
                return False
            # no attribute starting with zip or addr,
            if all([not key.startswith(('zip', 'addr')) for key in account.__dict__]):
                return False
            # no attribute name, id and value,
            if not hasattr(account, 'id') or not hasattr(account, 'value'):
                return False
            # name not being a string,
            # id not being an int,
            if not isinstance(account.name, str) or not isinstance(account.id, int):
                return False
            # value not being an int or a float.
            if not isinstance(account.value, (int, float)) :
                return False

        o_account.transfer(-amount)
        d_account.transfer(amount)
        return True
    
    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str) : 
            return False
        
        account = next((account for account in self.accounts if account.name == name), None)
        if account is None:
            return False
        
        for key in [key for key in account.__dict__ if key.startswith('b')]:
                account.__dict__.pop(key)

        if all([not key.startswith(('zip', 'addr')) for key in account.__dict__]):
            account.zip = '123-456'

        if not len(account.__dict__) % 2 :
            if ('fix' in account.__dict__.keys()):
                account.__dict__.pop('fix')
            else:
                account.__dict__["fix"] = True
        return True
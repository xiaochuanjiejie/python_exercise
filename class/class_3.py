__author__ = 'chuan'

class person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

if __name__ == '__main__':
    bob = person('Bob Smith')
    sue = person('Sue',job='dev',pay=10000)
    print bob.name,bob.pay
    print sue.name,sue.job,sue.pay
    print bob.name.split()[-1]
    sue.pay *= 1.10
    print sue.pay
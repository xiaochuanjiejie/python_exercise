__author__ = 'chuan'

def marker(N):
    def action(X):
        return X ** N
    return action

f = marker(2)
print f(3)
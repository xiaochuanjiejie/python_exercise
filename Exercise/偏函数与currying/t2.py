from functools import partial

def log(level, message, stack):
    print level + ": " + message
    print stack

log1 = partial(log,"Error")
log1("2","3")
print
logUnknownError = partial(partial(log, "Error"), "Unknown")
logUnknownError("stack content")
#-*- coding: utf-8 -*-
from functools import partial

def curriedLog(level):
    def logMsg(message):
          def logStack(stack):
              print level + ": " + message
              print stack
          return logStack
    return logMsg

curriedLogWarning = curriedLog("Warning")
#1. 偏函数后依然可以使用多参数，只要还有参数未固化；而Currying只能使用函数链
#work
curriedLogWarning("message")("stack")
print
curriedLogError  = curriedLog("Error")
curriedLogUnknownError = curriedLog("Error")("Unknown")
curriedLogUnknownError2 = curriedLogError("Unknown")
curriedLogUnknownError('3')
curriedLogUnknownError2('3')
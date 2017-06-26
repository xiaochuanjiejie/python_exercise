def log(level):
    def logMessage(message):
        print level + ": " + message
    return logMessage

#usage
log("Warning")("this is one warning message")

#or like this
logError = log("Error")
logError("this is one error message")

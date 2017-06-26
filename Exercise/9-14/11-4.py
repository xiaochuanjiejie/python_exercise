__author__ = 'xujunchuan'

def convert(minute):
    hour = minute / 60
    minute = minute % 60
    print '%d:%d' % (hour,minute)

convert(150)
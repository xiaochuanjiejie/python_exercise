#coding: utf-8

def safe_input(example):
    try:
        symbol = raw_input(example)
    except (EOFError,KeyboardInterrupt):
        symbol = None
    return symbol

if __name__ == '__main__':
    print safe_input('input: ')
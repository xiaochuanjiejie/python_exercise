__author__ = 'xujunchuan'

def list_name(lst):
    t_dict = globals()
    print type(t_dict),t_dict
    # global name
    for key in t_dict:
        if type(t_dict[key]) is type(lst) and t_dict[key] == lst:
            print key
            name = key
            print name

result = []
list_name(result)

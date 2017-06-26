#-*- coding: utf-8 -*-

import os

class Dos(object):
    def __init__(self):
        self.cmds = {'ls':'dir','more':'more','cat':'type','cp':'copy','mv':'ren','rm':'del'}
    def translate(self,cmd):
        t_cmd = cmd.split()
        if t_cmd[0] in self.cmds:
            t_cmd = self.cmds[t_cmd[0]]
        return ''.join(t_cmd)
    def start(self):
        v = raw_input('# ')
        while 1:
            if v == 'exit':
                break
            else:
                t_v = self.translate(v)
                output = os.popen(t_v).readlines()
                for out in output:
                    print out,

if __name__ == '__main__':
    t = Dos()
    print t.translate('ls')
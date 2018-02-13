# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:18:36 2017

@author: Jiang Jinjing
"""
from libdw import sm
class CommentsSM(sm.SM):
    startState = 'code' # helpful if give names instead of 0,1,2,3

    def getNextValues(self, state, inp):
        is_code=state=='code'
        is_comment=state=='comment'
        is_hash=inp=='#'
        is_newline=inp=='\n'
        
        if is_code and is_hash:
            nextState='comment'
            output = inp
            
        elif is_code and not is_hash:
            nextState='code'
            output=None
        
        elif is_comment and is_newline:
            nextState='code'
            output=None
            
        elif is_comment and not is_newline:
            nextState='comment'
            output=inp
            
        return nextState,output
        
#Anw
class CommentsSM(sm.SM):
    startState = 'out'

    def getNextValues(self, state, inp):
        if state == 'out':
            if inp == '#':
                return ('in', inp)
            else:
                return ('out', None)
        elif state == 'in':
            if inp == '\n':
                return ('out', None)
            else:
                return ('in', inp)

class FirstWordSM(sm.SM):
    startState = 'before'

    def getNextValues(self, state, inp):
        if state == 'before':
            if inp == '\n' or inp == ' ':
                return ('before', None)
            else:
                return ('inside', inp)
        elif state == 'inside':
            if inp == '\n':
                return ('before', None)
            elif inp == ' ':
                return ('after', None)
            else:
                return ('inside', inp)
        else:  # state == 'after':
            if inp == '\n':
                return ('before', None)
            else:
                return ('after', None)



class FirstWordSM(sm.SM):
    startState = 1

    def getNextValues(self, state, inp):

        if (state == 0 and inp==' ') or inp=='\n':
            nextState=0
            output =None
            
        elif inp!=' 'and (state == 0 or state == 1):
            nextState=1
            output= inp
        
        else:
            nextState=2
            output=None
            
        return nextState,output

'''
Write a state machine whose inputs are the characters of a string and which outputs either (a) the input character if it is part of the first word on a line or (b) None. For the purposes here, a word is any sequence of consecutive characters that does not contain spaces or end-of-line characters. In this problem, comments have no special status, if the first thing on a line is '# ', then the first word is '#'. 
For example: 
>> str = 'def f(x): # comment\n   return 1'
>>> m = FirstWordSM()
>>> m.transduce(str)
['d', 'e', 'f', 
None, None, None, None, None, None, None, None, None, None,
None, None, None, None, None, None, None, None, None, None, 
'r', 'e', 't', 'u', 'r', 'n', 
None, None]
>>> 
'''
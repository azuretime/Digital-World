import sm

class SimpleAccount(sm.SM):
    def __init__(self,startState):
        self.startState=startState
        
    def getNextValues(self, state, inp):
        if state < 100 and inp<0:
            return (state + inp -5, state + inp -5)
        else:
            return (state + inp, state + inp)
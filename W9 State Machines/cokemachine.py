class CM(sm.SM):
    startState = 0

    def getNextValues(self,state, inp):
        if state == 0 and inp == 100:
            nextstate = 0
            output=(0,'coke',0)
        elif state == 0 and inp == 50:
            nextstate = 1
            output=(50,'--',0)
        elif state == 1 and inp ==100:
            nextstate = 0
            output = (0, 'coke', 50)
        elif state == 1 and inp==50:
            nextstate = 0
            output = (0,'coke',0)
        else:
            nextstate = state
            output = (0,'--',inp)
        return nextstate,output
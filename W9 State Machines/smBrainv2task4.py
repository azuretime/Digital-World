import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState=0
    def getNextValues(self, state, inp):
        print inp.sonars# list
        print inp.odometry.theta
#        if state==0 and inp.sonars[3]>0.5:
#            return (state, io.Action(fvel = 0.1, rvel = 0.0))
#        elif state==0 and inp.sonars[3]<0.5:
#            state=1
#            return (state, io.Action(fvel = 0.0, rvel = 0.0 ))
#        elif state==1 and inp.sonars[3]<0.5:
#            return (state, io.Action(fvel = -0.1, rvel = 0.0 ))
#        elif state==1 and inp.sonars[3]>0.5:
#            state=0
#            return (state, io.Action(fvel = -0.1, rvel = 0.0 ))
#        if state==0 and inp.sonars[2]>0.5 and inp.sonars[1]>0.5 and inp.sonars[3]>0.5: #straight
#            return (state, io.Action(fvel = 0.1, rvel = 0.0))
#        elif state==0 and inp.sonars[1]>0.5 and inp.sonars[1]<1:
#            state='turn left'
#            return (state,io.Action(fvel = 0.0, rvel = -0.5 ))
#        elif state=='turn left' and inp.sonars[1]>0.5 :
#            return (state,io.Action(fvel = 0.0, rvel = -0.5 ))
#        elif state=='turn left' and inp.sonars[1]<=0.5:
#            state=1
#            return (state, io.Action(fvel = 0.1, rvel = 0.0))
#        elif state==1 and inp.sonars[2]>0.5 and inp.sonars[1]<0.5:
#            return (state, io.Action(fvel=0.1, rvel=0.0))
#        elif state==1 and inp.sonars[2]>0.5 and inp.sonars[1]>0.5:
#            state='turn right'
#            return (state, io.Action(fvel = 0.0, rvel = 0.5))
#        elif state==1 and inp.sonars[2]<0.5 and inp.sonars[1]<0.5:
#            state='turn left'
#            return (state, io.Action(fvel=0.0, rvel=-0.5))
#        elif state=='turn right'  and inp.sonars[2]<0.5:
#            state=1
#            return (state,io.Action(fvel = 0.0, rvel = 0.5))
#        elif state=='turn right' and inp.sonars[3]> 0.5 and inp.sonars[2]>0.5:
#            state=0
#            return (state, io.Action(fvel = 0.1, rvel = 0.0))
        
        #return (state, io.Action(fvel = 0.1, rvel = 0.0))
        if state==0:
            
            if  inp.sonars[3]<=0.5 :
                state='turn'
                return (state, io.Action(fvel=0.1, rvel=0.0))
#            elif inp.sonars[3]<=0.5:
#                state='turn'
#                return (state, io.Action(fvel=0.1, rvel=0.0))
            else:
                return (state, io.Action(fvel=0.1, rvel=0.0))
        elif state=='turn':
#            if inp.sonars[1]<=0.5:
#                return (state, io.Action(fvel=0.1, rvel=-0.5))
            if inp.sonars[3]<=0.5 :
                return (state, io.Action(fvel=0.1, rvel=0.5))
            
    
#            elif inp.sonars[1]>0.5:
#                return (state, io.Action (fvel=0.1, rvel=0.5))
            elif inp.sonars[3]>0.5:
                return (state, io.Action(fvel=0.1, rvel=-0.5))
            else:
                state==0
                return (state,io.Action(0.0, 0.0))
#            else:
#                state='skirt'
#                return(state, io.Action(fvel=0.1, rvel=0.0))
#        elif state=='skirt':
#           
#            if inp.sonars[1]<=0.5 :
#                return (state, io.Action(fvel=0.1, rvel=0.0))
#            elif inp.sonars[3]<=0.5:
#                return (state, io.Action(fvel=0.1, rvel=0.0))
#            elif inp.sonars[0]>=0.5:
#                state='turn'
#                return (state, io.Ation (fvel=0.0, rvel=0.0))
#            else:
#                state='turn'
#                return (state, io.Action(fvel=0.0, rvel=0.0))

    
        
mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass

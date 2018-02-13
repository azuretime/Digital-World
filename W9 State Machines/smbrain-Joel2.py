import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState=0
    def getNextValues(self, state, inp): #taking in sensory data as its input

        print inp.sonars# list
        print inp.odometry.theta
        if state == 0: #Detect wall
            if inp.sonars[2] < 0.5: #Rotate cw while moving fwd when d<0.5
                return (1, io.Action(fvel = 0.05, rvel = 0.2))
            else: #Keep going until d<0.5
                return (0, io.Action(fvel = 0.1, rvel = 0.0))
        if state == 1: #Snake-ing 
            if inp.sonars[2] > 0.5 and inp.sonars[4] > 0.5:
                return (1, io.Action(fvel = 0.05, rvel = -0.2))
            elif inp.sonars[2] > 0.5 and inp.sonars[4] < 0.5:
                return (1, io.Action(fvel = 0.05, rvel = 0.2))
            elif inp.sonars[2] > 0.5 and inp.sonars[4] <0.5:
                return (1, io.Action(fvel = 0.1, rvel = 0.0))
            elif inp.sonars[2] < 0.5:
                return (2, io.Action(fvel = 0.05, rvel = 0.2))

        if state == 2:
            if inp.sonars[2] <1.0:
                return (2, io.Action(fvel = 0.05, rvel = 0.2))
            else:
                return (1, io.Action(fvel = 0.1, rvel = 0.0))



    #fvel = forward velocity (m/s)
    #rvel = rotational velocity (rad/s)

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
                                  sonarMonitor=True) # sonar monitor widget

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

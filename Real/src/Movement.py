# Import all libs
import os, sys
from Constants import *
from Sensors import *
from Effectors import *
from wait_for_start import *

sys.path.append("/usr/lib")
import _kipr as KIPR

    
# Move forward
def forward(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, speed-LDRIFT)
	KIPR.mav(RMOTOR, speed-RDRIFT)
	while KIPR.gmpc(LMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.msleep(DELAY)

# Move backward
def backward(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, -speed+LDRIFT)
	KIPR.mav(RMOTOR, -speed+RDRIFT)
	while KIPR.gmpc(LMOTOR) >-ticks:
		pass
	KIPR.ao()  
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)

# Turn left
def left(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, -speed)
	KIPR.mav(RMOTOR, speed)
	while KIPR.gmpc(RMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)
	
# Sharp turn left
def deadLeft(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, 0)
	KIPR.mav(RMOTOR, speed)
	while KIPR.gmpc(RMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)

# Sharp turn right
def deadRight(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, speed)
	KIPR.mav(RMOTOR, 0)
	while KIPR.gmpc(LMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)
	
# Drift and turn left
def tDriftLeft(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, int((1/3)*speed))
	KIPR.mav(RMOTOR, speed)
	while KIPR.gmpc(RMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)
    
# Slower drift and turn left
def tDriftLeftE(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, int((1/6)*speed))
	KIPR.mav(RMOTOR, speed)
	while KIPR.gmpc(RMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)
    
# Turn right     
def right(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, speed)
	KIPR.mav(RMOTOR, -speed)
	while KIPR.gmpc(LMOTOR) < ticks:
		pass 
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)

# Travels forward for x seconds
def forward_time(speed, time):
	KIPR.motor(LMOTOR,  speed)
	KIPR.motor(RMOTOR, speed)
	KIPR.msleep(time)
	KIPR.ao()
	KIPR.msleep(DELAY)
	
# Travels backward for x seconds
def backward_time(speed, time):
	KIPR.motor(LMOTOR,  -speed)
	KIPR.motor(RMOTOR, -speed)
	KIPR.msleep(time)
	KIPR.ao()
	KIPR.msleep(DELAY)

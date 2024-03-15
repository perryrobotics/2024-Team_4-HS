#!/usr/bin/python
import os, sys
from Constants import *
from Sensors import *
from Effectors import *
from wait_for_start import *

sys.path.append("/usr/lib")
import _kipr as KIPR

    

def forward(speed, ticks):
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.mav(LMOTOR, speed-LDRIFT)
	KIPR.mav(RMOTOR, speed-RDRIFT)
	while KIPR.gmpc(LMOTOR) < ticks:
		pass
	KIPR.ao()
	KIPR.msleep(DELAY)

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
        
def forward_time(speed, time):
	KIPR.motor(LMOTOR,  speed)
	KIPR.motor(RMOTOR, speed)
	KIPR.msleep(time)
	KIPR.ao()
	KIPR.msleep(DELAY)

def backward_time(speed, time):
	KIPR.motor(LMOTOR,  -speed)
	KIPR.motor(RMOTOR, -speed)
	KIPR.msleep(time)
	KIPR.ao()
	KIPR.msleep(DELAY)

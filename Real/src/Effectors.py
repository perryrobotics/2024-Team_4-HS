# Import all libs
import os, sys
from Constants import *
from Sensors import *
from Movement import *
from wait_for_start import *
from math import *

sys.path.append("/usr/lib")
import _kipr as KIPR

# Slows servo movement
def move_servo_slow(port, end_pos, step):
	start_pos = KIPR.get_servo_position(port)
	if start_pos > end_pos:
		step = -step
	for pos in range(start_pos, end_pos, step):
		#print pos
		KIPR.set_servo_position(port, pos)
		KIPR.msleep(25)
	KIPR.set_servo_position(port, end_pos)

def arm_down(step):
	move_servo_slow(ARM_SERVO,ARM_DOWN, step)

def arm_back(step):
	move_servo_slow(ARM_SERVO,ARM_BACK, step)

def arm_forward(step):
	move_servo_slow(ARM_SERVO,ARM_FORWARD, step)
	#ove_servo_slow(ELBOW_SERVO,ELBOW_FORWARD, step)

def elbow_down(step):
	move_servo_slow(ELBOW_SERVO,ELBOW_DOWN, step)

def elbow_forward(step):
	move_servo_slow(ELBOW_SERVO,ELBOW_FORWARD, step)
	       
def elbow_up(step):
	move_servo_slow(ELBOW_SERVO,ELBOW_UP, step)
        
def claw_closed(step):
	move_servo_slow(CLAW_SERVO,CLAW_CLOSED, step)
        
def claw_halfopen(step):
	move_servo_slow(CLAW_SERVO,CLAW_HALFOPEN, step)
        
def claw_fullopen(step):
	move_servo_slow(CLAW_SERVO,CLAW_FULLOPEN, step)
        
def tail_up(step):
	move_servo_slow(TAIL_SERVO,TAIL_UP, step)

def tail_down(step):
	move_servo_slow(TAIL_SERVO,TAIL_DOWN, step)

def tail_middle(step):
	move_servo_slow(TAIL_SERVO,TAIL_MIDDLE, step)
        
    
def setup_claw_motor():
    KIPR.cmpc(CLAW_MOTOR)


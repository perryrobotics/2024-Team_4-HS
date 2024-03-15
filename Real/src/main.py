# Import all necessary libraries
import os, sys
from Constants import *
from Sensors import *
from Movement import *
from Effectors import *
from wait_for_start import *
import time
import threading 
sys.path.append("/usr/lib")
import _kipr as KIPR

# Keeps a motor static at a position when the function is called
def motor_hold_position(motor,pos):
	global thread_running
	print("In the thread")
	sys.stdout.flush()
	thread_running = True
	KIPR.cmpc(motor)
	
	while thread_running == True:
		#print(KIPR.gmpc(motor))
		if KIPR.gmpc(motor)<pos-10:
			KIPR.mav(motor, 70)
		elif KIPR.gmpc(motor)>pos+10:
			KIPR.mav(motor,-70)
		else:
			KIPR.mav(motor,0)
	print("Claw thread exiting!")
	sys.stdout.flush()
	KIPR.motor(motor,0)
KIPR.enable_servos()

#POSSIBLE-FLICK SWITCH FIRST
'''
move_servo_slow(ARM_SERVO, 800, 50)
move_servo_slow(ELBOW_SERVO, 550, 50)
left(700, 74)
forward(1200, 1500)
left(700, 70)
forward(1200, 3200)
right(700, 30)
forward(900, 700)
right(700, 700)
move_servo_slow(ELBOW_SERVO, 1940, 30)
left(700, 700)
move_servo_slow(ARM_SERVO, 1100, 8)			
'''

# Servo start positions initialized
move_servo_slow(ARM_SERVO, 230, 50)
move_servo_slow(ELBOW_SERVO, 100, 50)
move_servo_slow(1, 1720, 50)


#====================================================================================================

#Go Play Botball!!
x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR,-250), daemon = True)
x.start()
forward(1300, 4500)
move_servo_slow(ARM_SERVO, 1040, 50)
move_to_black(900)
backward(1200,500)
right(1000, 1050)
move_to_black(400)
thread_running = False
move_servo_slow(ELBOW_SERVO, 1430, 50)
move_servo_slow(ARM_SERVO, 230, 50)

# Mult-tasking via threading
x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR, 250), daemon = True)
x.start()
time.sleep(5)
thread_running = False

# Move forward to get the people in the claw
move_servo_slow(ARM_SERVO, 2040, 5)
backward(1200, 200)
right(900,960)					
forward(1200, 2000)
move_to_black(900)
right(900, 980)				
forward(1200, 3000)

# Align to the 1st pipe
forward(700, 1200)  
backward(1200, 2800)
left(1000, 1325)					
move_servo_slow(ARM_SERVO, 1750, 10)
backward(1200, 2300)
backward(500, 190)
move_servo_slow(1, 1150, 50)  
left(900, 10)

# Align small bot in front of airlock
forward(1200, 1300)
move_servo_slow(1, 2040, 10)
right(900, 2230)
backward(1200, 1600)
move_servo_slow(ARM_SERVO, 930, 10)
move_servo_slow(ELBOW_SERVO, 1940, 10)
forward(600, 1200)
left(200, 50)


x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR,-150), daemon = True)
x.start()
time.sleep(5)
thread_running = False

# Move claw down and drop the astronauts in the airlock
x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR, 150), daemon = True)
x.start()
time.sleep(5)
thread_running = False

# Alignment with the airlock switch
backward(1200, 670)
right(500, 220)
forward(1200,2000)
move_servo_slow(ARM_SERVO, 800, 10)
forward(900, 740)
left(500, 140)

# Flicks the airlock switch so big bot recieves the purple noodle
move_servo_slow(ARM_SERVO, 1000, 10)		
right(1000, 600)
move_servo_slow(1, 300, 50)
x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR,-350), daemon = True)
x.start()
time.sleep(5)
thread_running = False

# Gathering rocks and sorting
backward(1200, 300)
move_servo_slow(ELBOW_SERVO, 1196, 50)
move_servo_slow(ARM_SERVO, 20, 50)
forward(1200, 1400)
right(900, 300)
forward(1200, 1700)
deadLeft(1200, 200)
x = threading.Thread(target = motor_hold_position, args=(CLAW_MOTOR,100), daemon = True)
x.start()
tDriftLeft(1200, 1350)
forward(1200, 1500)
tDriftLeftE(900, 1800)
forward(1200, 3000)
thread_running = False
tDriftLeftE(1200, 400)
forward(1200, 800)
move_servo_slow(ARM_SERVO, 1500, 50)
move_servo_slow(ELBOW_SERVO, 800, 50)
deadRight(1200, 600)
backward

#!/usr/bin/python
import os, sys
from Constants import *
from Effectors import *
from Movement import *
from wait_for_start import *

sys.path.append("/usr/lib")
import _kipr as KIPR



def move_to_black(speed, port=LINE_PORT_RIGHT, thresh=THRESH): 
	KIPR.mav(LMOTOR, speed-LDRIFT)
	KIPR.mav(RMOTOR, speed-RDRIFT)
	while KIPR.analog(port) < thresh:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)
            
def back_to_black(speed, port, thresh): 
	KIPR.mav(LMOTOR, -speed+LDRIFT)
	KIPR.mav(RMOTOR, -speed+RDRIFT)
	while KIPR.analog(port) < thresh:
		pass
	KIPR.ao()
	KIPR.msleep(DELAY)
            
def move_to_white(speed, port=LINE_PORT_RIGHT, thresh=THRESH): 
	KIPR.mav(LMOTOR, speed-LDRIFT)
	KIPR.mav(RMOTOR, speed-RDRIFT)
	while KIPR.analog(port) > thresh:
		pass
	KIPR.ao()
	KIPR.cmpc(RMOTOR)
	KIPR.cmpc(LMOTOR)
	KIPR.msleep(DELAY)

def back_to_white(speed, port, thresh): 
	KIPR.mav(LMOTOR, -speed+LDRIFT)
	KIPR.mav(RMOTOR, -speed+RDRIFT)
	while KIPR.analog(port) < thresh:
		pass
	KIPR.ao()
	KIPR.msleep(DELAY)

def right_to_black(speed):
	KIPR.mav(Lmotor, speed)
	KIPR.mav(Rmotor, -speed)
	while KIPR.analog(line_port) < thresh:
		pass
	KIPR.ao()   
            
def left_to_black(speed):
	KIPR.mav(Lmotor, speed - 100)
	KIPR.mav(Rmotor, speed)
	while KIPR.analog(line_port) < thresh:
		pass
	KIPR.ao()  
   
def right_to_white(speed):
	KIPR.mav(Lmotor, speed)
	KIPR.mav(Rmotor, -speed)
	while KIPR.analog(line_port) > thresh:
		pass
	KIPR.ao()  
  
def left_to_white(speed):
	KIPR.mav(Lmotor, -speed)
	KIPR.mav(Rmotor, speed)
	while KIPR.analog(line_port) > thresh:
		pass
	KIPR.ao()
#line average
def line_average(port,times):
	line = []
	del line[:]
	for x in range(times):
		line.append(analog(port))
	for x in range(times-1):
		line[0] = line[0]+line.pop(1)
	line_average = line[0]/times
	return line_average

def line_median(port, times):
	med = []
	del med[:]
	if times%2 == 1:
 		times = times+1
	for x in range(times):
		med.append(analog(port))
	med.sort()
	median = times/2
	return med[median]

def line_average_median(port,times):
	median = []
	del median[:]
	if times%2 == 1:
		times = times +1
	for x in range(times):
		del line[:]
		line = []
		for x in range(times):
			line.append(analog(port))
		for x in range(times-1):
			line[0] = line[0]+line.pop(1)
		line_average = line[0]/times
		median.append(line_average)
	median.sort()
	med = times/2
	return median[med]
    
def line_follow_dist(speed, dist):
	print("Line following!!")
	KIPR.cmpc(LMOTOR)
	KIPR.cmpc(RMOTOR)
	while KIPR.gmpc(LMOTOR) <= dist:
		if KIPR.analog(LINE_PORT_LEFT) > THRESH:
			KIPR.mav(LMOTOR, -speed)
			KIPR.mav(RMOTOR, speed)
		elif KIPR.analog(LINE_PORT_RIGHT) > THRESH:
			KIPR.mav(LMOTOR, speed)
			KIPR.mav(RMOTOR, -speed)
		else:
			KIPR.mav(LMOTOR, speed+150)
			KIPR.mav(RMOTOR, speed)
	KIPR.ao()
	print("Done following!!")

def line_follow_bump(speed):
	print("Line following!!")
	while KIPR.digital(BUMP_PORT) == 0:
		if KIPR.analog(LINE_PORT_LEFT) > THRESH+400:
			KIPR.mav(LMOTOR, -speed)
			KIPR.mav(RMOTOR, speed)
		elif KIPR.analog(LINE_PORT_RIGHT) > THRESH+400:
			KIPR.mav(LMOTOR, speed)
			KIPR.mav(RMOTOR, -speed)
		else:
			KIPR.mav(LMOTOR, speed)
			KIPR.mav(RMOTOR, speed)
	KIPR.ao()
	print("Done following!!")
                
def line_follow_sensors(speed):
	print("Line following!!")
	KIPR.cmpc(LMOTOR)
	KIPR.cmpc(RMOTOR)
	while KIPR.analog(LINE_PORT_LEFT) < THRESH or KIPR.analog(LINE_PORT_RIGHT) < THRESH:
		if KIPR.analog(LINE_PORT_LEFT) > THRESH:
			KIPR.mav(LMOTOR, -speed)
			KIPR.mav(RMOTOR, speed)
		elif KIPR.analog(LINE_PORT_RIGHT) > THRESH:
			KIPR.mav(LMOTOR, speed)
			KIPR.mav(RMOTOR, -speed)
		else:
			KIPR.mav(LMOTOR, speed+150)
			KIPR.mav(RMOTOR, speed)
	KIPR.ao()
	print("Done following!!")



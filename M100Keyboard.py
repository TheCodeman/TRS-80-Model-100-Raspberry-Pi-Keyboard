"""
Test code to read TRS-80 Model 100 Keyboard and send chars to uinput .
written by Codeman

"""
import uinput
import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin=0
debounce = .01
delay = .1
control = 0
shift = 0
alt=0
code = 0
c0 = 4
c1 = 17
c2 = 18
c3 = 27
c4 = 22
c5 = 23
c6 = 24
c7 = 25
c8 = 5

r0 = 6
r1 = 12
r2 = 13
r3 = 19
r4 = 16
r5 = 26
r6 = 20
r7 = 21

lookup = 	[
				uinput.KEY_Z, uinput.KEY_A, uinput.KEY_Q, uinput.KEY_O,          uinput.KEY_1, uinput.KEY_9,  uinput.KEY_SPACE,  uinput.KEY_F1, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_X, uinput.KEY_S, uinput.KEY_W, uinput.KEY_P,          uinput.KEY_2, uinput.KEY_0,   uinput.KEY_BACKSPACE, uinput.KEY_F2, uinput.KEY_LEFTCTRL, 
				uinput.KEY_C, uinput.KEY_D, uinput.KEY_E, uinput.KEY_RIGHTBRACE, uinput.KEY_3, uinput.KEY_MINUS,      uinput.KEY_TAB,    uinput.KEY_F3, uinput.KEY_LEFTALT, 
				uinput.KEY_V, uinput.KEY_F, uinput.KEY_R, uinput.KEY_SEMICOLON,  uinput.KEY_4, uinput.KEY_EQUAL,       uinput.KEY_ESC,    uinput.KEY_F4, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_B, uinput.KEY_G, uinput.KEY_T, uinput.KEY_APOSTROPHE, uinput.KEY_5, uinput.KEY_LEFT,       uinput.KEY_F9,  uinput.KEY_F5, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_N, uinput.KEY_H, uinput.KEY_Y, uinput.KEY_COMMA,        uinput.KEY_6, uinput.KEY_RIGHT,    uinput.KEY_F10,  uinput.KEY_F6, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_M, uinput.KEY_J, uinput.KEY_U, uinput.KEY_DOT,      uinput.KEY_7, uinput.KEY_UP,       uinput.KEY_F11,  uinput.KEY_F7, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_L, uinput.KEY_K, uinput.KEY_I, uinput.KEY_SLASH,      uinput.KEY_8, uinput.KEY_DOWN,      uinput.KEY_ENTER,  uinput.KEY_F8, uinput.KEY_F12,
				uinput.KEY_PAGEUP, uinput.KEY_PAGEDOWN,
				]
device = 	uinput.Device([
				uinput.KEY_Z, uinput.KEY_A, uinput.KEY_Q, uinput.KEY_O,          uinput.KEY_1, uinput.KEY_9,  uinput.KEY_SPACE,  uinput.KEY_F1, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_X, uinput.KEY_S, uinput.KEY_W, uinput.KEY_P,          uinput.KEY_2, uinput.KEY_0, uinput.KEY_BACKSPACE, uinput.KEY_F2, uinput.KEY_LEFTCTRL, 
				uinput.KEY_C, uinput.KEY_D, uinput.KEY_E, uinput.KEY_RIGHTBRACE, uinput.KEY_3, uinput.KEY_MINUS,      uinput.KEY_TAB,    uinput.KEY_F3, uinput.KEY_LEFTALT, 
				uinput.KEY_V, uinput.KEY_F, uinput.KEY_R, uinput.KEY_SEMICOLON,  uinput.KEY_4, uinput.KEY_EQUAL,       uinput.KEY_ESC,    uinput.KEY_F4, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_B, uinput.KEY_G, uinput.KEY_T, uinput.KEY_APOSTROPHE, uinput.KEY_5, uinput.KEY_LEFT,       uinput.KEY_F9,  uinput.KEY_F5, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_N, uinput.KEY_H, uinput.KEY_Y, uinput.KEY_COMMA,        uinput.KEY_6, uinput.KEY_RIGHT,         uinput.KEY_F10,  uinput.KEY_F6, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_M, uinput.KEY_J, uinput.KEY_U, uinput.KEY_DOT,      uinput.KEY_7, uinput.KEY_UP,       uinput.KEY_F11,  uinput.KEY_F7, uinput.KEY_LEFTSHIFT, 
				uinput.KEY_L, uinput.KEY_K, uinput.KEY_I, uinput.KEY_SLASH,      uinput.KEY_8, uinput.KEY_DOWN,      uinput.KEY_ENTER,  uinput.KEY_F8, uinput.KEY_F12,
				])
				
def checkKB(row):
	global control, shift, alt, code
	col=-1

	if GPIO.input(c8) == True: #col 8
		time.sleep(debounce)
		if GPIO.input(c8) == True:
			if row==0:
				shift=1
			elif row==1:
				control=1
			elif row==5:
				shift=1
			elif row==2:
				alt =1
			elif row == 3:
				code = 1
		
			else:
				col = 8
		else :
			shift =0
			control =0
			alt =0 

	if GPIO.input(c0) == True:
		time.sleep(debounce)
		if GPIO.input(c0) == True:
			col = 0
	if GPIO.input(c1) == True:
		time.sleep(debounce)
		if GPIO.input(c1) == True:
			col = 1
	if GPIO.input(c2) == True:
		time.sleep(debounce)
		if GPIO.input(c2) == True:
			col = 2
	if GPIO.input(c3) == True:
		time.sleep(debounce)
		if GPIO.input(c3) == True:
			col = 3
	if GPIO.input(c4) == True:
		time.sleep(debounce)
		if GPIO.input(c4) == True:
			col = 4
	if GPIO.input(c5) == True:
		time.sleep(debounce)
		if GPIO.input(c5) == True:
			col = 5
	if GPIO.input(c6) == True:
		time.sleep(debounce)
		if GPIO.input(c6) == True:
			col = 6
	if GPIO.input(c7) == True:
		time.sleep(debounce)
		if GPIO.input(c7) == True:
			col = 7
	if col!=-1:																	

		key=lookup[row*9+col]

		if control==1 :

			device.emit_combo([uinput.KEY_LEFTCTRL, key])
			control=0
		elif shift==1:

			device.emit_combo([uinput.KEY_LEFTSHIFT, key])
			shift=0
		elif alt==1:

			device.emit_combo([uinput.KEY_LEFTALT, key])
			alt=0
		elif code==1:

			if row==6 and col ==5:
				device.emit_click(uinput.KEY_PAGEUP)

			if row==7 and col ==5:
				device.emit_click(uinput.KEY_PAGEDOWN)

			if row==3 and col ==3:
				device.emit_click((0x01,124))

			code=0
		else:

			device.emit_click(key)

		time.sleep(delay)
		col=-1
def scanKB():

	GPIO.output(r0,  GPIO.HIGH)
	checkKB(0)
	GPIO.output(r0,  GPIO.LOW)
	
	GPIO.output(r1,  GPIO.HIGH)
	checkKB(1)
	GPIO.output(r1,  GPIO.LOW)

	GPIO.output(r2,  GPIO.HIGH)
	checkKB(2)
	GPIO.output(r2,  GPIO.LOW)
	
	GPIO.output(r3,  GPIO.HIGH)
	checkKB(3)
	GPIO.output(r3,  GPIO.LOW)

	GPIO.output(r4,  GPIO.HIGH)
	checkKB(4)
	GPIO.output(r4,  GPIO.LOW)

	GPIO.output(r5,  GPIO.HIGH)
	checkKB(5)
	GPIO.output(r5,  GPIO.LOW)

	GPIO.output(r6,  GPIO.HIGH)
	checkKB(6)
	GPIO.output(r6,  GPIO.LOW)
	

	GPIO.output(r7,  GPIO.HIGH)
	checkKB(7)
	GPIO.output(r7,  GPIO.LOW)
	

	
GPIO.setup(c0,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c1,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c2,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c3,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c4,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c5,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c6,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c7,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c8,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(r0,  GPIO.OUT)
GPIO.setup(r1,  GPIO.OUT)
GPIO.setup(r2,  GPIO.OUT)
GPIO.setup(r3,  GPIO.OUT)
GPIO.setup(r4,  GPIO.OUT)
GPIO.setup(r5,  GPIO.OUT)
GPIO.setup(r6,  GPIO.OUT)
GPIO.setup(r7,  GPIO.OUT)


GPIO.output(r0,  GPIO.LOW)
GPIO.output(r1,  GPIO.LOW)
GPIO.output(r2,  GPIO.LOW)
GPIO.output(r3,  GPIO.LOW)
GPIO.output(r4,  GPIO.LOW)
GPIO.output(r5,  GPIO.LOW)
GPIO.output(r6,  GPIO.LOW)
GPIO.output(r7,  GPIO.LOW)

while True:
	scanKB()
	time.sleep(.005)
GPIO.cleanup()

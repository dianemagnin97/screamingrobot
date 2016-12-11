#TO DO:
#figure out how to connect it to iphone 6
#test out code on robot
#TRIPLE CHECK CODE for typos
#CHECK PIN NAMES if wrong try GRPIO.setmode(GPIO.BOARD) otherwise google dexter industry board
#research GPIO library (pins input output) to see if we can return input value instrad of HIGH (true) or LOW (false) (see online maybe?)



#setup
from threading import Timer
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#setup pins
vibePin = Serial
SoundPin = A1
BuzzPin = D11
lightPin = I2C

#serial vibration
GPIO.setup(vibePin, GPIO.IN)
#a1 sound
GPIO.setup(SoundPin, GPIO.IN)
#D11 buzzer 
GPIO.setup(BuzzPin, GPIO.OUT)
#l2c light
GPIO.setup(lightPin, GPIO.IN)

spacial_state = ""
sound_state = ""
light_state = ""
set_speed(150) #between 0-255
screaming_state = False

#GPIO.output(D11, GPIO.HIGH) #loud screens
#GPIO.input(PIN) #read pin value #true or false #HIGH or LOW
#time.sleep(in seconds) #delays

#checks how many times it has been blocked
stress = 0

#set to shut off after 3 minutes
timer = "off"
t = Timer(180, end)
t.start()
timer = "on"

#rotation time
def turnoff_rot_timer():
	rot_timer = "off"

rot_t = Timer(2, turnoff_rot_timer)


def screaming_robot(state=state):
	while timer == "on":
		servo(70)
		check_overall()
		check_lighting()
		check_sound()
		check_spacial()
		#if blocked
		if spacial_state == "blocked":
			print "I'm blocked! AAAAAAAAAHHHHHH!"
			GPIO.output(BuzzPin, GPIO.HIGH)
			screaming_state = True
			stress = 1
			rot_timer = "on"
			rot_t.start()
			#rotate for 2 seconds
			while rot_timer == "on":
				right_rot()							
		        time.sleep(1)
		        GPIO.output(BuzzPin, GPIO.LOW)
			#check if blocked again
			check_spacial()
			if spacial_state == "blocked":
			        GPIO.output(BuzzPin, GPIO.HIGH)
			        screaming_state = True		
				stress = 2
				rot_timer = "on"
				rot_t.start()
			#rotate for 2 seconds
				while rot_timer == "on":
					right_rot()
		                time.sleep(2)
		                GPIO.output(BuzzPin, GPIO.LOW)	
				check_spacial()	
				if spacial_state == "blocked":
				        GPIO.output(BuzzPin, GPIO.HIGH)
			                screaming_state = True		                        	
					stress = 3
					rot_timer = "on"
					rot_t.start()
			#rotate for 2 seconds
					while rot_timer == "on":
						right_rot()
					time.sleep(4)
		                        GPIO.output(BuzzPin, GPIO.LOW)
					check_spacial()	
					if spacial_state == "blocked":
						stress = 4
						GPIO.output(BuzzPin, GPIO.HIGH)
						screaming_state = True
						time.sleep(10)
						GPIO.output(BuzzPin, GPIO.LOW)
						screaming_state = False
						screaming_robot()




    #check if space in front of it is empty
        #if empty, go towards empty space
        #if space not empty (but not surrounded) set off "search space with counter"
            #turn 90* to find empty space, beep once (counter 1)
                #if empty, go towards it (counter 0, exit loop)
                #if not empty, turn 90 (counter 1, now 2)
                    #...
                    #if counter reaches 4 --> state = "surrounded"
                    #SCREAM for 10 seconds

def check_spacial(spacial_state=spacial_state):
	if GPIO.input(vibePin) == False:
		spacial_state = "free"
		fwd()
		stress = 0
	else:
		spacial_state = "blocked"
		stop()
		bwd()
		time.sleep(1)
		stop()
		servo(28)
		time.sleep(1)
		servo(112)
		time.sleep(1)
		servo(70)
		time.sleep(1)
		#counter = 1
  		#beep        
    #if state = surrounded

 def check_lighting(light_state=light_state):
 	if GPIO.input(lightPin):
 		light_state = "light"
 	else:
 		light_state = "dark"	
 		GPIO.output(BuzzPin, GPIO.HIGH)
 		screaming_state = True
 		set_speed(255)
 		time.sleep(5)
 		set_speed(150)

def check_sound(Sound_state=sound_state):
	print "sound level" + string(GPIO.input(soundPin))
	if GPIO.input(soundPin) > 150:
		sound_state = "loud"
		GPIO.output(BuzzPin, GPIO.HIGH)
 		screaming_state = True
 		set_speed(255)
 		time.sleep(5)
 		set_speed(150)
	else:
		sound_state = "quiet"	

def check_overall(overall_state= overall_state):
	if spacial_state == "free" and light_state == "light" and sound_state == "quiet":
		print "I have a bad feeling about this"
		GPIO.output(BuzzPin, GPIO.LOW)
		screaming_state = False

def end():
	GPIO.cleanup()
	break

screaming_robot()

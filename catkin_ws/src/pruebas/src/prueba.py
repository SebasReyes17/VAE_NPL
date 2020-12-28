#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String

pub_goal= rospy.Publisher("vae/speech_recog", String, queue_size=10)

def callback_function(msg):
	x = msg.data
	print(x)
	if(x=='VAE BUSCA PERSONA'):
		goal='persona'
	elif(x=='VAE BUSCA PERRO'):
		goal='perro'
	elif(x=='VAE BUSCA GATO'):
		goal='gato'
	elif(x=='VAE BUSCA COCHE'):
		goal='coche'
	elif(x=='VAE BUSCA GATO'):
		goal='gato'
	elif(x=='VAE VUELVE'):
		goal='vuelve'
	elif(x=='VAE ACELERA'):
		goal='acelera'
	elif(x=='VAE FRENA'):
		goal='frena'
	elif(x=='VAE PARA'):
		goal='para'
	elif(x=='VAE DUERME'):
		goal='duerme'
	else:
		goal=''
		loop.sleep()
	pub_goal.publish(goal)


def main():
	print "INITIALIZING SPEECH SYNTHESIS NODE..."
	rospy.init_node("speech_synthesize")
	rospy.Subscriber("/recognized",String, callback_function)
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
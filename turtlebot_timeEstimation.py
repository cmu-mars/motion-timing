#!/usr/bin/python

import os
import sys
import getopt
# from colors import *

class TurtleTimeModel:
	'Timimg Model for the Turtlebot Linear Motion'
	__speed = 0.0
	__distance = 0.0

	def __init__ (self, speed, distance):
		self.__speed = speed
		self.__distance = distance

	def computeRampUpTime (self):
	    r_up_time = 1.3766*self.__speed + 0.7991
	    return r_up_time

	def computeRampDownTime (self):
	    r_down_time = 2.642
	    return r_down_time

	def computeRampUpSpeed (self):
		r_up_speed = 0.2821*self.__speed - 0.0428
		return r_up_speed

	def computeRampDownSpeed (self):
		r_down_speed = 0.4215*self.__speed + 0.0162
		return r_down_speed

	def computeRampDownDistance (self):
		r_down_distance = self.computeRampDownTime () * self.computeRampDownSpeed ()
		return r_down_distance

	def computeRampUpDistance (self):
		r_up_distance = self.computeRampUpTime () * self.computeRampUpSpeed ()
		return r_up_distance

	def computeShortDistance (self):
		totalTime = self.computeRampUpTime () + self.computeRampDownTime ()
		overall_speed = self.__distance/totalTime
		return totalTime, overall_speed

	def computeTotalTime (self):
	    totalTime = self.computeRampUpTime () + self.computeRampDownTime ()
	    rStable_distance = self.__distance - self.computeRampDownDistance () - self.computeRampUpDistance ()
	    rStable_time = rStable_distance/self.__speed
	    totalTime = totalTime + rStable_time
	    return totalTime


def main(argv):
   speed = 0
   distance = 0
   try:
      opts, args = getopt.getopt(argv,"hs:d:")
   except getopt.GetoptError:
      print 'turtlebot_timeEstimation -s <Speed> -d <Distance>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'turtlebot_timeEstimation -s <Speed in  m/s> -d <Distance in m>'
         sys.exit()
      elif opt in ("-s", "--speed"):
         speed = float(arg)
      elif opt in ("-d", "--distance"):
         distance = float(arg)
   print '\n\nDesired Speed: ',speed, 'm/secs'
   print 'Distance: ', distance, 'm'

   if (speed > 0.0 and speed <= 0.8):
   		times = TurtleTimeModel (speed, distance)
   		if (distance < (times.computeRampUpDistance () + times.computeRampDownDistance ())):
   			totalTime, overall_speed = times.computeShortDistance ()
			sys.stdout.write("\033[1;31m")
   			print 'WARNING: Distance is less than the minimum distance travelled in Ramp Up and Ramp Down motion'
   			sys.stdout.write("\033[0;0m")
   			print 'Ramp Up Time: ', times.computeRampUpTime (), 'secs'
	   		print 'Ramp Down Time: ', times.computeRampDownTime (), 'secs'
	   		print 'Average Speed over the entire path:', overall_speed, 'm/secs'
	   		print '-------------------------------------------------------'
	   		print 'Total Time: ', totalTime, 'secs\n\n'
   		else:
	   		print 'Ramp Up Time: ', times.computeRampUpTime (), 'secs'
	   		print 'Ramp Down Time: ', times.computeRampDownTime (), 'secs'
	   		print '-------------------------------------------------------'
	   		print 'Total Time: ', times.computeTotalTime (), 'secs\n\n'
   else:
   		print 'Maximum Speed on the Turtlebot : 0.8m/secs\n\n'

if __name__ == "__main__":
   main(sys.argv[1:])





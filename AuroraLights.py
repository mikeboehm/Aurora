class Lights(object):
	def __init__(self):
		pass
	
	# Turns the reading light on and off
	def toggle_light(self):
		pass
	
	def toggle_light_on(self):
		pass

	def toggle_light_off(self):
		pass
	
	# Sets the light relative to where we are in the sequence
	def set_sunrise_colour(self, progress):
		if progress <= 50:
			colour = self.phase_one(progress)
		else:
			colour = self.phase_two(progress)
		
		self.set_lights(colour)
		
	def test(self):
		print 'Aurora Lights!'
		
	# Black to Red
	def phase_one(self, progress):
# 		print '=' * 10 + ' phase_one() ' + '=' * 10
		# rgb(255,0,0)		
		
		# Factor in that progress within phase_one() will only go as high as 50
		progress = (progress / 50) * 100
		
		red = float(255)/100
		red *= progress
		green = 0
		blue = 0
		
		colour = {'red': red, 'green': green, 'blue': blue}
		
		return colour
	
	# Red to white
	def phase_two(self, progress):
# 		print '=' * 10 + ' phase_two() ' + '=' * 10
		# rgb(255,255,255)
		# Factor in that progress within phase_two() will start at >50
		progress = (progress - 50) * 2
		
		red = 255
		green = (float(255)/100)* progress
		blue = (float(255)/100)* progress
		
		colour = {'red': red, 'green': green, 'blue': blue}
		
		return colour
		
	def set_lights(self, colour):
		red = int(colour['red'])
		green = int(colour['green'])
		blue = int(colour['blue'])

		print 'R:' + str(red) + ', G:' + str(green) + ', B:' + str(blue)
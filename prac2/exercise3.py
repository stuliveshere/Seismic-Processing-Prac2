#write a function that performs a bit of an amplitude correction

from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exercise1 import initialise


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------
@io
def tar(dataset, **kwargs):
	#pull some values out of the
	#paramter dictionary
	gamma = kwargs['gamma']
	t = kwargs['times']
	
	#calculate the correction coeffieicnt
	r  = None #you need to fill this in
	
	#applyt the correction to the data
	dataset['trace'] *= r
	return dataset

	
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
	#intialise workspace and parameter dictionary
	workspace, params = None

	#set the value of gamma you want to test here
	params['gamma'] = None
	#and apply
	tar(workspace, None, **params)
	
	#we cant use agc to look at this.  The display 
	#function has been modified so you can adjust
	#the clip
	params['clip'] = 1e-4
	toolbox.display(workspace, None, **params)
	pylab.show()
	
	
	

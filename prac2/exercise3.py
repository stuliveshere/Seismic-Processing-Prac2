#import su files from prac1
#sort into cdp/offsets
#view a cdp gather

from toolbox import io
import toolbox
import numpy as np
import os
import matplotlib.pyplot as pylab
from exercise1 import initialise


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------
@io
def tar(data, **kwargs):
        #pull some values out of the
        #paramter dictionary
        gamma = kwargs['gamma']
        t = kwargs['times']
        
        #calculate the correction coeffieicnt

        
        #applyt the correction to the data


        return data

        
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #intialise dataset and parameter dictionary


        #set the value of gamma you want to test here
        params['gamma'] = 0
        
        #and apply
        tar(dataset, None, **params)
        
        #and display
        
        toolbox.display(dataset, None, **params)
        pylab.show()
        
        
        

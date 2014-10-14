#import su file
#view the gathers to make sure 
#they imported properly

from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab



#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def initialise(file):
        #intialise empty parameter dictionary

        kwargs = None #you need to fill this in
        
        #load file
        dataset = None #and this
        
        #allocate stuff
        dataset['cdp'] =  None #and this
        kwargs['ns'] = None #and this
        kwargs['dt'] =None #and this
        
        #also add the time vector - it's useful later
        kwargs['times'] = np.linspace(0.001, 1.0, 1000) #i'll give you this one
        return dataset, kwargs
        
        
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #intialise workspace and parameter dictionary
        workspace, params = None
        
        #the scan tool scans the file headers for non-zero values
        toolbox.scan(workspace)
        
        #the scroll tool allows you to skip through an entire volume, but
        #you have to define the sort keys, and step size
        params['primary'] = None
        params['secondary'] = None
        params['step'] = None
        
        #the scroll tool is like the display tool, but
        #you can use the left and right arrows to
        #scroll through a volume
        toolbox.scroll(workspace, None, **params)
        
        #the viewing tools have been changed so that 
        #you can view more than one thing at once.
        #but you need to put this at the end.
        pylab.show()
        
        
        

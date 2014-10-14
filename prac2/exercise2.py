#sort into cdp/offsets
#view a cdp gather

from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exercise1 import initialise


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

None

        
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #intialise workspace and parameter dictionary
        workspace, params = None
        
        # we are going to pull out 1 cdp for testing with.
        #firstly, use the scroll tool to view the cdps, and 
        #then pick one near the middle of the volume
        params['primary'] = None
        params['secondary'] = None
        params['step'] =None
        toolbox.scroll(workspace, None, **params)
        
        #we then want to extract that single cdp
        #for testing with later. we can do that 
        #the following way
        #cdp = workspace[workspace['cdp'] == 0 ]
        #view it
        #toolbox.agc(cdp, None ,**params)
        #toolbox.display(cdp, None, **params)
        
        #we have the right cdp = but the traces are in the wrong 
        #order. lets sort by offset
        
        #cdp = np.sort(cdp, order=['cdp', 'offset'])
                
        #output it for later
        #toolbox.cp(cdp, 'cdp.su', None)       
        #params['clip'] = 1e-6
        #toolbox.display('cdp.su', None, **params)
        
        
        pylab.show()
        
        
        

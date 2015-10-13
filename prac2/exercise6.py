#import su files from prac1
#sort into cdp/offsets
#view a cdp gather

from toolbox import io
import toolbox
import numpy as np
np.seterr(all='ignore')
import os
import matplotlib.pyplot as pylab
from exercise1 import initialise
from exercise3 import tar
from exercise4 import nmo
from exercise5 import _stack_gather


#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def semb(workspace,**kwargs):
        vels = kwargs['velocities']
        nvels = vels.size
        ns = kwargs['ns']
        result = np.zeros((nvels,ns),'f')
        for v in range(nvels):
                panel = workspace.copy()
                kwargs['vels'] = np.ones(kwargs['ns'], 'f') * vels[v]
                nmo(panel, None, **kwargs)
                result[v,:] += np.abs(_stack_gather(panel)['trace'])
                
                
        pylab.imshow(result.T, aspect='auto', extent=(min(vels), max(vels),kwargs['ns']*kwargs['dt'],0.), cmap='gist_heat')
        pylab.xlabel('velocity')
        pylab.ylabel('time')
        pylab.colorbar()
        pylab.show()

        
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #initialise dataset
        
        #build list of velocities to stack
        velocities = np.arange(10, 4e6, 10)
        
        #set some parameters
        params['velocities'] = velocities
        params['smute'] =30
        params['primary'] = 'cdp'
        params['secondary'] = 'offset'
        
        #agc might help
        #~ toolbox.agc(workspace, None, None)
        
        #run the semblance
        #~ semb(workspace, **params)
        
        #pick your times and velocities
        v = []
        t = []
        params['vels'] = toolbox.build_vels(t, v, ns=params['ns'])
        
        #run the nmo to check
        
        #display
        
        
        

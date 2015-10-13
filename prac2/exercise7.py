#write a function which will flatten a cdp

from toolbox import io
import toolbox
import numpy as np
from exercise1 import initialise
import pylab

#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def _lmo_calc(aoffset, velocity):
        '''function to calculate the timeshift
        at a given offset'''
        
@io
def lmo(dataset, **kwargs):
        offsets = np.unique(dataset['offset'])
        for offset in offsets:
                aoffset = np.abs(offset)
                shift = _lmo_calc(aoffset, kwargs['lmo'])
                shift  = (shift*1000).astype(np.int)
                inds= [dataset['offset'] == offset]
                dataset['trace'][inds] =  np.roll(dataset['trace'][inds], shift, axis=-1) #results[inds]
        return dataset

#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #initialise dataset 
        
        #set some parameters
        params['primary'] = 'cdp'
        params['secondary'] = 'offset'
        params['lmo'] = 0.0
        
        #apply agc
        
        #apply lmo
        
        #zero out the bits we dont want

        #reverse and apply LMO

       #display 





from toolbox import io
import toolbox
import numpy as np
from exercise3 import tar
from exercise4 import nmo
from exercise1 import initialise
import pylab

#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

def _stack_gather(gather):
        '''stacks a single gather into a trace.
        uses header of first trace. normalises
        by the number of traces'''
        pass

@io	
def stack(dataset, **kwargs):
        cdps = np.unique(dataset['cdp'])
        sutype = np.result_type(dataset)
        result = np.zeros(cdps.size, dtype=sutype)
        for index, cdp in enumerate(cdps):
                gather = dataset[dataset['cdp'] == cdp]
                trace = _stack_gather(gather)
                result[index] = trace
        return result
        
if __name__ == '__main__':
        #initialise your test cdp first

        
        #first do the true amplitude recovery

        
        #set nmo parameters	
        params['smute'] = 0
        params['vels'] = toolbox.build_vels([0.5], [1], ns=params['ns'])
        #then apply NMO
        
        #we will apply a pre-stack agc
        toolbox.agc(workspace, None, None)
        
        #stack it
        section = stack(workspace, None, **params)
        
        #display it
        #params['clip'] = 1e-5
        toolbox.display(section, None, **params)
        
        pylab.show()
        
        
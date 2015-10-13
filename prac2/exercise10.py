#we need a velocity filter

from toolbox import io
import toolbox
import numpy as np
import matplotlib.pyplot as pylab
from exercise1 import initialise
from exercise3 import tar
from exercise4 import nmo
from exercise5 import stack
from exercise7 import lmo

#-----------------------------------------------------------------------
#              useful functions
#-----------------------------------------------------------------------

@io
def fk(dataset, **kwargs):
        shots = np.unique(dataset['sx'])
        for shot in shots:
                inds = [dataset['sx'] == shot]
                slice = dataset[inds]
                slice = np.sort(slice, order=['sx','gx'])
                fft =  np.fft.rfft2(slice['trace'])
                ctype = np.dtype([('offset', np.float), ('trace', (np.complex128, fft.shape[1]))])
                workspace = np.zeros(slice.size, dtype=ctype)
                workspace['trace'] = fft
                nfft =  fft.shape[0]/2
                workspace['trace'] = np.roll(workspace['trace'], nfft, axis=-2)
                workspace['offset'] = slice['offset']
                lmo(workspace, None, **kwargs)
                smoother = np.ones(500)/500.
                workspace['trace'][:,-500:]  = np.apply_along_axis(lambda m: np.convolve(m, smoother, mode='same'), axis=-1, arr=workspace['trace'][:,-500:])
                kwargs['lmo'] *= -1
                lmo(workspace, None, **kwargs)
                workspace['trace'] = np.roll(workspace['trace'], nfft, axis=0)
                dataset['trace'][inds] = np.fft.irfft2(workspace['trace'])
        return dataset
#-----------------------------------------------------------------------
#              main functions
#-----------------------------------------------------------------------

if __name__ == "__main__":
        #intialise workspace and parameter dictionary
        print 'initialising'
        workspace, params = initialise('survey.su')
        workspace = workspace[workspace['sx'] == 500]
        
        params['lmo'] = 3000.0
        fk = fk(workspace, None, **params)
        
        #~ 
        #~ params['primary'] = None
        toolbox.display(workspace, None, **params)
        pylab.show()

"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

ctr = 0

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block to be used in places where FFT can be used."""

    def __init__(self, fft_size=1024):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Mock FFT',   # will show up in GRC
            #in_sig=[np.complex64],
            #out_sig=[np.complex64]
            in_sig=[(np.complex64,fft_size)],
            out_sig=[(np.complex64,fft_size)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.fft_size = fft_size

    def work(self, input_items, output_items):
        """Starting point for writing a custom FFT block."""

        # input_items is an array of an array of blocks. So far I've never 
        # seen len(input_items) be anything other than 1 but it seems possible
        # that it can be greater than that.
        assert len(input_items) > 0

        # I've seen len(input_items[0]) be 4 and 7. I'm guessing that grc simply
        # bundles these up depending on how much memory is available so you shouldn't
        # make any assumptions about how many blocks you'll get in one call.
        assert len(input_items[0]) > 0
        
        # I'm pretty sure that each individual block better be the specified size
        assert len(input_items[0][0]) == self.fft_size
        
        #output_items[0][:] = input_items[0] # * 5
        output_items = input_items
        print 'processing set'
        for item in output_items:
            print 'Length of item =',len(item)
        
        
        return len(output_items)
        

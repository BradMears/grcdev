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

        global ctr
        ctr +=1

        # input_items is a list of ndarray of ndarray of complex64
        # output_items has the same shape
        assert type(input_items) == list
        assert type(input_items[0]) == np.ndarray
        assert type(input_items[0][0]) == np.ndarray
        assert type(input_items[0][0][0]) == np.complex64
        assert input_items[0].shape == output_items[0].shape
        assert len(input_items) > 0
        assert len(input_items[0]) > 0
        assert len(input_items[0][0]) == self.fft_size

        for ii,_ in enumerate(input_items):
            assert len(output_items[ii]) == len(input_items[ii])
            for jj,_ in enumerate(input_items[ii]):
                assert len(input_items[ii][jj]) == self.fft_size
                assert len(output_items[ii][jj]) == self.fft_size
                for kk,val in enumerate(input_items[ii][jj]):
                    assert type(val) == np.complex64
                    output_items[ii][jj][kk] = 123 + 456j #val

        return len(output_items)
        

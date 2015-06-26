#!/usr/bin/env python

from core.handler import HDF5Handler

handler = HDF5Handler('mydata.hdf5')
handler.open()

for i in range(100):
    handler.put(i, 'numbers')

handler.close()



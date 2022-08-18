#! /usr/bin/env python3
import sys

# Write a context manager that temporarily redirects stdout
# to the file indicated by outfilename and then restores
# stdout on exit

class Redirector:

    def __init__(self, outfilename):
        self.outfilename = outfilename

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_val, ex_trace):
        pass

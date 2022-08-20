#! /usr/bin/env python3
import sys

# Write a context manager that temporarily redirects stdout
# to the file indicated by outfilename and then restores
# stdout on exit

class Redirector:

    def __init__(self, outfilename):
        self.outfilename = outfilename
        self.outfile = None
        self.saved_stdout = None

    def __enter__(self):
        self.outfile = open(self.outfilename, 'w')
        self.saved_stdout = sys.stdout
        sys.stdout = self.outfile

    def __exit__(self, ex_type, ex_val, ex_trace):
        if self.outfile:
            self.outfile.close()
        sys.stdout = self.saved_stdout


if __name__ == '__main__':
    with Redirector('captured'):
        print('I am Arthur, King of the Britons!')
        print('King of the who?')
    print("Well, I didn't vote for you")    

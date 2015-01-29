# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 09:55:02 2015

@author: JRoussin
"""

import sys
import re
import os
#import getopt
import argparse
import datetime
import win32file

"""
    TODO
        Check whether inputFilenameDate is Friday, if so roll forward to Monday not Saturday.        
        Verify input file exists
"""

#inputFilenameComplete = ' '.join(sys.argv[2:]).replace('"','')
#inputFilenameName, inputFilenameExtension = os.path.splitext(inputFilenameComplete)

parser = argparse.ArgumentParser()
parser.add_argument('-f', nargs = '+')
args = parser.parse_args(sys.argv[1:])

inputFilenameComplete = ' '.join(args.f).replace('"','')
inputFilenameName, inputFilenameExtension = os.path.splitext(inputFilenameComplete)

loc = re.search(r'\d{4}-\d{2}-\d{2}', inputFilenameComplete)

##opts, args = getopt.getopt(argv,"d:f:")
##opts, args = getopt.getopt(sys.argv[1:],"hd:f:o:",["ifile=","ofile="])
#opts, args = getopt.getopt(sys.argv[1:],"d:f:")

#for opt,arg in opts:
#    if opt == '-d':
#        d = arg
##    if opt == '-f':
##        arg2 = re.sub('"', '', arg)        
##        inputFilename, inputFilenameExtension = os.path.splitext(arg)        
##        outputFilename = inputFilename + ' ' + today + inputFilenameExtension

inputDate = datetime.datetime.strptime(loc.group(0), '%Y-%m-%d')

outputDate = inputDate + datetime.timedelta(days = 1)

outputFilenameDate = outputDate.strftime('%Y-%m-%d')

outputFilenameComplete = inputFilenameName[0:loc.start(0)] + outputFilenameDate + inputFilenameExtension

win32file.CopyFile (inputFilenameComplete, outputFilenameComplete, 1)
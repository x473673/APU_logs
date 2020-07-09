#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

def printTypes(filename):
	logfile = open(filename,'r')
	errors = []
	line = logfile.readline()
	while line:
		match = re.match('\s{40}(\wx\w\w)\s{7}(\wx\w\w)',line)
		if match: errors.append(match.group(1,2))
		line = logfile.readline()
	logfile.close()
	short = list(dict.fromkeys(errors))
	print('Present error types in this file, format: (<ErrType>,<SCSIOperationCode>):')
	print(*short,sep = "\n")

def findType(filename,errtype,scsicode=''):
	logfile = open(filename,'r')
	discs = []
	line = logfile.readline()
	errLog = False
	chosenDisc = ''
	discInfo = ''
	while line:
		discMatch = re.match('.*\s(\w\w:\w:\w)\s',line)
		if discMatch:
			chosenDisc = discMatch.group(1)
			errLog = False
		errorMatch = re.match('.*\sErrors\sLogged(.*)$',line)
		if errorMatch:
			errLog = True
			discInfo = errorMatch.group(1)
		typeMatch = re.match('\s{40}'+errtype+'\s{7}'+scsicode,line)
		if typeMatch and errLog and chosenDisc+discInfo not in discs: discs.append(chosenDisc+discInfo)
		line = logfile.readline()
	logfile.close()
	print(*discs,sep = "\n")
	

if len(sys.argv) == 1:
	print('specify a log file')
	exit(1)
if len(sys.argv) == 2:
	printTypes(sys.argv[1])
	exit(0)
if len(sys.argv) == 3:
	findType(sys.argv[1],sys.argv[2])
	exit(0)
if len(sys.argv) == 4:
	findType(sys.argv[1],sys.argv[2],sys.argv[3])
	exit(0)
print('too many arguments')


#
# Custom Makefile for building NEC5 source files
# This assumes the source file has the file suffix .DAT
# All .dat files will be compared with their .OUT file 
# any files that need updating will then be processed.
# Tim Seed
# DV3A Mar 2024
#
#
#This needs to be run using WSL (Windows Subsystem for Linux)
COMP:=/mnt/e/nec5/NEC5CL.exe

# Not needed - but trying to be clear
.SUFFIXES: .out .dat 

# Get all the sources
SOURCES=$(wildcard *.dat)
#change the file suffix to the target, from SOURCES
TARGETS=$(patsubst %.dat,%.out,$(SOURCES))

all: $(TARGETS)

# Using Make inbuilt Macros 
# $< means SOURCE
# $@ means TARGET
%.out : %.dat
	$(COMP) $< $@

#Clean up
.Phony: clean
clean:
	rm *.out

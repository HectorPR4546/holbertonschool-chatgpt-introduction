#!/usr/bin/python3
import sys

"""
This script prints all command-line arguments passed to it, excluding the script name.
"""

# Loop over all arguments except the script name
for arg in sys.argv[1:]:
    print(arg)

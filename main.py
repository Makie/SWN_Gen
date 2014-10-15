#!./venv/Scripts/python

""" Docstring for swn_gen.py. """

import os
import json
import logging.config

import sectors

WELCOME_MESSAGE = \
    ["      _______ _  _  _ __   _        ______ _______ __   _",
     "      |______ |  |  | | \  |       |  ____ |______ | \  |",
     "      ______| |__|__| |  \_| _____ |_____| |______ |  \_|",
     "", " Welcome to SWN_GEN a sector generator for Stars Without Number."]

print(*WELCOME_MESSAGE, sep="\n")


if __name__ == '__main__':
    main()
import os, sys
try:
    __import__("km").login()
except Exception as e:
    exit(str(e))

import os, sys
try:
    __import__("bdid").login()
except Exception as e:
    exit(str(e))
#! /usr/bin/env python3

import sys
import pyperclip

passwords = { 'fb' : '1233','gmail':'12345'}
account=sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
print('password copied to clipboard')
        
        
    

#!/usr/bin/python

'''

Author 	: Abhishek Yadav
Github 	: https://github.com/abydv
License : MIT


MIT License

Copyright (c) 2022 Abhishek Yadav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


'''

from .colors import *
from udemy import __version__

def banner():
    banner = f'''
%s%s              __                               ____  
%s%s   __  ______/ /__  ____ ___  __  __      ____/ / /  
%s%s  / / / / __  / _ \/ __ `__ \/ / / /_____/ __  / /   
%s%s / /_/ / /_/ /  __/ / / / / / /_/ /_____/ /_/ / /    
%s%s \__,_/\__,_/\___/_/ /_/ /_/\__, /      \__,_/_/     
%s%s                           /____/
                                 %s%sVersion : %s%s{__version__}
                                 %s%sAuthor  : %s%sAbhishek Yadav
                                 %s%sGithub  : %s%shttps://github.com/abydv

''' % (fc, sb,fc, sb,fc, sb, fm, sb, fy, sb, fy, sb, fy,sd, fg, sd, fy, sd, fg, sd, fy, sd, fg, sd)
    return banner

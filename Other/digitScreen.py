import string
import random
import time

def the_matrix(max_lines,line_width):
    lines=1
    line_char=1
    my_string=string.letters+string.digits
    
    while (lines <= max_lines):
        get_char=random.choice(my_string)
        print '%2s' %get_char
        print out_char,         #','makes a line
        time.sleep(0.1)
        if (line_char==line_width):
            print '\n'
            line_char = 1
            lines += 1
        else：
            line_char+=1
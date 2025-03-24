# Eli Robison, Debugging Notes

import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call': # when the function is called
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line': # when a new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return': # when we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception': # when their is an exeption
        print(f'Exception in {frame.f_code.co_name}: {arg}')

sys.settrace(trace_calls)

tracer = trace.Trace(count=False, trace=True)

# What is tracing?
    #
def add(x, y):
    print(sub(x, y))
    return x + y

def sub(x, y):
    return x - y

print(add(5, 2))

# tracer.run('add(8/9)')

# Basic tracing command
    # python -m trace --trace file path

"""
    --trace (displays lines ass executed)
    --count (displays number of times executed)
    --listfuncs (displays functions used in the program)
    --trackcalls (displays relationships between functions)
"""

# What are some ways we can debug by tracing?
    # it lets you observe what your program is doing without interupting it.

# How do you access the debugger in VS Code?
    # press the debugger on the left
    # F5 fey
    # dropdown on the play menu

# What is testing?
    # running your code to make sure it works as required, try to break thr code.

# What are boundary conditions?
    # check the entries most likely to be wrong.

# How do you handle when users give strange inputs?
    # condituionals and loops/ try except.
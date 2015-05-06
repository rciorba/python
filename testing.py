
import sys
import time

start = 0 
lineNo = 0
lastTime = 0

def trace_lines(frame, event, arg):
    if event != 'line':
        return
		
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print '  %s line %s -- %d' % (func_name, line_no, int(round(time.time() * 1000)) - lastTime)
    global lastTime 
    lastTime = int(round(time.time() * 1000)) 
	
def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print 'Call to %s on line %s of %s' % (func_name, line_no, filename)

    return trace_lines
    #return

def g():
	print "here"
	time.sleep(4)
	time.sleep(3)

sys.settrace(trace_calls)
g()
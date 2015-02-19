#


# template for "Stopwatch: The Game"

# define global variables
import simplegui
import random

mins = 0
sec = 0
tenth_sec = 0
tenths_sec = 0
time = 0
interval = 100
count = 0
correct_hit = 0
def start():
    timer.start()
def stop():
    timer.stop()
    global count, correct_hit
    
    if tenths_sec == 0 and tenth_sec>0:
       correct_hit+=1    
    if tenths_sec == 0 and tenths_sec>0 and sec>0:
       correct_hit+=1
    if tenths_sec == 0 and tenth_sec==0 and sec>0:
       correct_hit+=1
    if tenths_sec == 0 and tenth_sec==0 and sec==0 and mins>0:
       correct_hit+=1
    if tenths_sec == 0 and tenth_sec>0 and sec==0 and mins>0:
       correct_hit+=1
    count+=1
    if count == 5:
       count = 0
       correct_hit = 0
       return count
def reset():
    global mins, sec, tenth_sec, tenths_sec
    mins = 0
    sec = 0
    tenth_sec = 0
    tenths_sec = 0
    time = 0
    count = 0
    correct_hit == 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global mins, sec, tenth_sec, tenths_sec, counter
    
    convert_to_string = str(mins)+":"+str(sec)+str(tenth_sec)+"."+str(tenths_sec)
    return convert_to_string

def counter():
    count_to_string = str(correct_hit)+ "/"+str(count)
    return count_to_string

frame = simplegui.create_frame("Stop watch", 400, 200)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    
    global mins, sec, tenth_sec, tenths_sec

    tenths_sec+=1
    if tenths_sec == 10:
       tenth_sec+=1
       tenths_sec = 0 
       return tenths_sec
    if tenth_sec == 10:      
       tenth_sec=0
       sec+=1
       return sec
    if sec == 6:
       mins+=1
       sec = 0
       return mins
   
# define draw handler
def draw(canvas):
    canvas.draw_text(format(), [150, 130], 45, 'White')
#def draw(canvas):
    canvas.draw_text(counter(), [300, 50], 45, 'White')
    
# create frame


# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric

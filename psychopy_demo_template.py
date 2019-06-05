# -*- coding: utf-8 -*-
# Delete the unnecessary parts of this template before publishing the script
"""
[Title of experiment]
[Author Information] 
[Last Modified : 2019. 3. 24.]

Credit : 

1. Software: 

Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv, J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-01193-y
Peirce, J. W., & MacAskill, M. R. (2018). Building Experiments in PsychoPy. London: Sage.
Peirce J. W. (2009). Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2 (10), 1-8. doi:10.3389/neuro.11.010.2008
Peirce, J. W. (2007). PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162 (1-2):8-13 doi:10.1016/j.jneumeth.2006.11.017

2. Template:
PsychoPy - Psychology software for Python (Release 3.0.6) by Jonathan Pierce, Ph.D. 
https://www.psychopy.org/PsychoPyManual.pdf

Cognitive Psychology Experiments Demonstrations by Attila Krajcsi, Krisztina Peres, and Gábor Lengyel
[https://sites.google.com/site/kognitivgyakorlatok/home/fejlesztoknek/ psychopy_demo_template.py]
Copyright © 2013 Eötvös Loránd Tudományegyetem, Pedagógiai és Pszichológiai Kar, Pszichológiai Intézet, Kognitív Pszichológiai Tanszék

3. Korean Translation & Modified by 

Yoon Kyung Lee, M.A. in Cognitive Psychology
Seoul National University
yoonlee78@snu.ac.kr

"""

# 모듈 import
from psychopy import visual, core, event, gui
import random

# Stimuli
stims = ['a', 'b', 'c']
random.shuffle(stims) # Randomize list
# import random required

win = visual.Window([1200,600], allowGUI=True, fullscr=True, waitBlanking=True, monitor='testMonitor', units='pix') # Create window

# Open log file to write
file_name = exp_info['participant']+'_parity.csv'
log_file = open(file_name, 'a')
log_file.write('participant, task, stimulus, response, RT\n') # Heading

# Instruction
text_instruction = visual.TextStim(win, pos=[0,0], text=texts['instr'][exp_info['language']]) # Text object
text_instruction.draw()
win.flip() # draw the instruction
event.waitKeys() # wait for key press to continue

# Experiment
text_stimulus = visual.TextStim(win, pos=[0,0], text='dummy') # Text object
trial_clock = core.Clock() # Clock for measuring response time
for stim in stims:
    # Example trial
    text_stimulus.setText(stim)
    text_stimulus.draw()
    win.flip() # draw the prepared window
    trial_clock.reset() # start measuring reaction time
    response=event.waitKeys()[0] # response
    RT = trial_clock.getTime() # store reaction time
    if response == 'escape':  # stops experiment if esc is pressed
        core.quit()
    event.clearEvents()

    win.flip() # show a clean window
    core.wait(0.5) # ITI

    log_file.write('"%s", task, %s, %s, %.4f\n' %(exp_info['participant'], stim, response, RT))

log_file.close()

# Analyze data
try:
    import analyze_log
    analyze_log.analyze_log (filename=file_name, output_file='', 
                         indep_var='stimulus', dep_var='RT', function='median', filt_cond = '$error$==0',
                         print_results = True, write_results = True, display_graph = True, 
                         graph_types=['boxplot', 'line'])
except:
    print 'I cannot analyze the results. Copy the analyze_log.py file to the folder, your experiment is.'

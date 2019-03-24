# -*- coding: utf-8 -*-
# Delete the unnecessary parts of this template before publishing the script
"""
Title of the demo
Author of the demo: (optionally add affiliation and contact information)
Date of the last modification: 2013 May 13
Supported by 

Copyright 2013 [Author(s)]
Licensed under the MIT License. You may obtain a copy of the License at http://opensource.org/licenses/MIT
"""

# Imports
from psychopy import visual, core, event, gui
import random

# Language specific components
def _(string):
    # You should use texts dictionary to strore the strings, and set exp_info['language'] to specify the language
    return texts[string][exp_info['language']]
texts = {
    'instr':
        {'en':'If the word displayed on the screen is a meaningful English word, press the %s button, otherwise the button %s.',
        'hu':u'Ha a képernyőn megjelenő szó értelmes magyar szó, akkor nyomd meg a %s gombot, egyébként pedig a %s gombot.'},
    'words':
        {'en':['cat', 'dog', 'hunfert'],
        'hu':['kutya', 'macska', u'gyilmók']},
}
# List of available language: texts.values()[0].keys()
# Get a specific item example: _(‘instr’)

exp_info = {'participant':'participant_ID',
    'language': texts.values()[0].keys()} # default parameters of the experiment

# Setting some parameters on GUI
dlg = gui.DlgFromDict(exp_info, title='exp_title',
   order = ['participant', 'language'],
    tip = {'participant':'Identifier of the participant.',
        'language':'Language of the instructions.',})
if not dlg.OK:
    print 'User Cancelled'
    core.quit()

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

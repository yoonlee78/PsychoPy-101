#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.0),
    on Thu May  9 16:54:42 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.0'
expName = 'lexical_decision'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/yoon/psychopy/PsychoPy-101/practice/lexical_decision.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
Intro_text = visual.TextStim(win=win, name='Intro_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix_text = visual.TextStim(win=win, name='fix_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Task"
TaskClock = core.Clock()
task_instr = visual.TextStim(win=win, name='task_instr',
    text='default text',
    font='Arial',
    units='height', pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_present = visual.TextStim(win=win, name='text_present',
    text='default text',
    font='Arial',
    units='cm', pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
Intro_text.setText('Welcome!\nPress 1 for word,\nPress 0 for non-word\nTo start, press SPACE\n')
key_resp = keyboard.Keyboard()
# keep track of which components have finished
IntroComponents = [Intro_text, key_resp]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_text* updates
    if t >= 0.0 and Intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro_text.tStart = t  # not accounting for scr refresh
        Intro_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Intro_text, 'tStartRefresh')  # time at next scr refresh
        Intro_text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Intro_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        Intro_text.tStop = t  # not accounting for scr refresh
        Intro_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(Intro_text, 'tStopRefresh')  # time at next scr refresh
        Intro_text.setAutoDraw(False)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        key_resp.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if key_resp.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        key_resp.tStop = t  # not accounting for scr refresh
        key_resp.frameNStop = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
        key_resp.status = FINISHED
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro_text.started', Intro_text.tStartRefresh)
thisExp.addData('Intro_text.stopped', Intro_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "fix"-------
t = 0
fixClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
fix_end = keyboard.Keyboard()
# keep track of which components have finished
fixComponents = [fix_text, fix_end]
for thisComponent in fixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_text* updates
    if t >= 0.0 and fix_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_text.tStart = t  # not accounting for scr refresh
        fix_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_text, 'tStartRefresh')  # time at next scr refresh
        fix_text.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        fix_text.tStop = t  # not accounting for scr refresh
        fix_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(fix_text, 'tStopRefresh')  # time at next scr refresh
        fix_text.setAutoDraw(False)
    
    # *fix_end* updates
    if t >= 0.0 and fix_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_end.tStart = t  # not accounting for scr refresh
        fix_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_end, 'tStartRefresh')  # time at next scr refresh
        fix_end.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(fix_end.clock.reset)  # t=0 on next screen flip
        fix_end.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_end.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        fix_end.tStop = t  # not accounting for scr refresh
        fix_end.frameNStop = frameN  # exact frame index
        win.timeOnFlip(fix_end, 'tStopRefresh')  # time at next scr refresh
        fix_end.status = FINISHED
    if fix_end.status == STARTED:
        theseKeys = fix_end.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            fix_end.keys = theseKeys.name  # just the last key pressed
            fix_end.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fix"-------
for thisComponent in fixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix_text.started', fix_text.tStartRefresh)
thisExp.addData('fix_text.stopped', fix_text.tStopRefresh)
# check responses
if fix_end.keys in ['', [], None]:  # No response was made
    fix_end.keys = None
thisExp.addData('fix_end.keys',fix_end.keys)
if fix_end.keys != None:  # we had a response
    thisExp.addData('fix_end.rt', fix_end.rt)
thisExp.addData('fix_end.started', fix_end.tStartRefresh)
thisExp.addData('fix_end.stopped', fix_end.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('text_cond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task"-------
    t = 0
    TaskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    task_instr.setColor('white', colorSpace='rgb')
    task_instr.setPos((0,-1))
    task_instr.setText('word: 1, non-word: 0')
    task_instr.setFont('Gulim')
    task_instr.setHeight(0.1)
    text_present.setColor('white', colorSpace='rgb')
    text_present.setPos((0, 0))
    text_present.setText(engText
)
    text_present.setFont('calibri')
    text_present.setHeight(0.1)
    task_resp = keyboard.Keyboard()
    # keep track of which components have finished
    TaskComponents = [task_instr, text_present, task_resp]
    for thisComponent in TaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_instr* updates
        if t >= 0.0 and task_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_instr.tStart = t  # not accounting for scr refresh
            task_instr.frameNStart = frameN  # exact frame index
            win.timeOnFlip(task_instr, 'tStartRefresh')  # time at next scr refresh
            task_instr.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if task_instr.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            task_instr.tStop = t  # not accounting for scr refresh
            task_instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(task_instr, 'tStopRefresh')  # time at next scr refresh
            task_instr.setAutoDraw(False)
        
        # *text_present* updates
        if t >= 0.0 and text_present.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_present.tStart = t  # not accounting for scr refresh
            text_present.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_present, 'tStartRefresh')  # time at next scr refresh
            text_present.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_present.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_present.tStop = t  # not accounting for scr refresh
            text_present.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_present, 'tStopRefresh')  # time at next scr refresh
            text_present.setAutoDraw(False)
        
        # *task_resp* updates
        if t >= 0.0 and task_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_resp.tStart = t  # not accounting for scr refresh
            task_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(task_resp, 'tStartRefresh')  # time at next scr refresh
            task_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(task_resp.clock.reset)  # t=0 on next screen flip
            task_resp.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if task_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            task_resp.tStop = t  # not accounting for scr refresh
            task_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(task_resp, 'tStopRefresh')  # time at next scr refresh
            task_resp.status = FINISHED
        if task_resp.status == STARTED:
            theseKeys = task_resp.getKeys(keyList=['1', '0', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                task_resp.keys = theseKeys.name  # just the last key pressed
                task_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (task_resp.keys == str(CorrAns)) or (task_resp.keys == CorrAns):
                    task_resp.corr = 1
                else:
                    task_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task"-------
    for thisComponent in TaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('task_instr.started', task_instr.tStartRefresh)
    trials.addData('task_instr.stopped', task_instr.tStopRefresh)
    trials.addData('text_present.started', text_present.tStartRefresh)
    trials.addData('text_present.stopped', text_present.tStopRefresh)
    # check responses
    if task_resp.keys in ['', [], None]:  # No response was made
        task_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           task_resp.corr = 1;  # correct non-response
        else:
           task_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('task_resp.keys',task_resp.keys)
    trials.addData('task_resp.corr', task_resp.corr)
    if task_resp.keys != None:  # we had a response
        trials.addData('task_resp.rt', task_resp.rt)
    trials.addData('task_resp.started', task_resp.tStartRefresh)
    trials.addData('task_resp.stopped', task_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
bye.setText('You are done!\n\nThank you! Bye !')
bye_resp = keyboard.Keyboard()
# keep track of which components have finished
EndComponents = [bye, bye_resp]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye* updates
    if t >= 0.0 and bye.status == NOT_STARTED:
        # keep track of start time/frame for later
        bye.tStart = t  # not accounting for scr refresh
        bye.frameNStart = frameN  # exact frame index
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if bye.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        bye.tStop = t  # not accounting for scr refresh
        bye.frameNStop = frameN  # exact frame index
        win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
        bye.setAutoDraw(False)
    
    # *bye_resp* updates
    if t >= 0.0 and bye_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        bye_resp.tStart = t  # not accounting for scr refresh
        bye_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(bye_resp, 'tStartRefresh')  # time at next scr refresh
        bye_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(bye_resp.clock.reset)  # t=0 on next screen flip
        bye_resp.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if bye_resp.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        bye_resp.tStop = t  # not accounting for scr refresh
        bye_resp.frameNStop = frameN  # exact frame index
        win.timeOnFlip(bye_resp, 'tStopRefresh')  # time at next scr refresh
        bye_resp.status = FINISHED
    if bye_resp.status == STARTED:
        theseKeys = bye_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            bye_resp.keys = theseKeys.name  # just the last key pressed
            bye_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('bye.started', bye.tStartRefresh)
thisExp.addData('bye.stopped', bye.tStopRefresh)
# check responses
if bye_resp.keys in ['', [], None]:  # No response was made
    bye_resp.keys = None
thisExp.addData('bye_resp.keys',bye_resp.keys)
if bye_resp.keys != None:  # we had a response
    thisExp.addData('bye_resp.rt', bye_resp.rt)
thisExp.addData('bye_resp.started', bye_resp.tStartRefresh)
thisExp.addData('bye_resp.stopped', bye_resp.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Fri Sep 18 13:38:25 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.2.4'
expName = 'CPED_even'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
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
    originPath='/Users/jingwenjin/Desktop/Archive/Experiment_RJP/CPED_even_RJP_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=(0.827,0.827,0.827), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welc_Resp = keyboard.Keyboard()
Welc_Text = visual.TextStim(win=win, name='Welc_Text',
    text='欢迎进入表情识别测查!',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Exp_Instr"
Exp_InstrClock = core.Clock()
ExpInstr_Resp = keyboard.Keyboard()
ExpInstr_Text = visual.TextStim(win=win, name='ExpInstr_Text',
    text='在本测查中有两种类型\n的决策，一类关于判定\n一个人脸的表情是否为\n惊恐，另一类判定一个\n人脸的表情是否为平静。\n每一轮只有其中一种决策。\n',
    font='Songti SC',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Prac_Text"
Prac_TextClock = core.Clock()
PracInstr_Resp = keyboard.Keyboard()
PracInstr_Text = visual.TextStim(win=win, name='PracInstr_Text',
    text='下面，我们来练习一下。',
    font='Songti SC',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
InstrText_Image = visual.ImageStim(
    win=win,
    name='InstrText_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Instr_Resp = keyboard.Keyboard()

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
jitter = np.arange(1, 3, .1)
shuffle(jitter)
FixCross_Image = visual.ShapeStim(
    win=win, name='FixCross_Image', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.35, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "StimPres_Prac"
StimPres_PracClock = core.Clock()
thisLoop_P = 0

PracStimPres_Images = visual.ImageStim(
    win=win,
    name='PracStimPres_Images', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
PracMaskImage_Before = visual.ImageStim(
    win=win,
    name='PracMaskImage_Before', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
PracMaskImage_After = visual.ImageStim(
    win=win,
    name='PracMaskImage_After', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
PracKeyResp = keyboard.Keyboard()
PracFixCross_Resp = visual.ShapeStim(
    win=win, name='PracFixCross_Resp', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.35, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
PracFixCross_PostCue = visual.ShapeStim(
    win=win, name='PracFixCross_PostCue', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.35, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
PracCue_Image = visual.ImageStim(
    win=win,
    name='PracCue_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)

# Initialize components for Routine "Feedback_Prac"
Feedback_PracClock = core.Clock()
Feedback_Prac_Text = visual.TextStim(win=win, name='Feedback_Prac_Text',
    text='default text',
    font='Calibri',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "PracEnd_Feedback"
PracEnd_FeedbackClock = core.Clock()
PracEnd_Feedback_Text = visual.TextStim(win=win, name='PracEnd_Feedback_Text',
    text='default text',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ActualRun_Instr"
ActualRun_InstrClock = core.Clock()
ActualRunInstr_Resp = keyboard.Keyboard()
ActualRun_text = visual.TextStim(win=win, name='ActualRun_text',
    text='下面我们进入正式测查。\n在正式测查中，每一轮\n会有更多的决策。',
    font='Songti SC',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
InstrText_Image = visual.ImageStim(
    win=win,
    name='InstrText_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Instr_Resp = keyboard.Keyboard()

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
jitter = np.arange(1, 3, .1)
shuffle(jitter)
FixCross_Image = visual.ShapeStim(
    win=win, name='FixCross_Image', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.35, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "Stim_Pres"
Stim_PresClock = core.Clock()
thisLoop = 0

Stim_Pres_Image = visual.ImageStim(
    win=win,
    name='Stim_Pres_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
Mask_Before_Image = visual.ImageStim(
    win=win,
    name='Mask_Before_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
Mask_After_Image = visual.ImageStim(
    win=win,
    name='Mask_After_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
KeyResp = keyboard.Keyboard()
FixCross_Resp = visual.ShapeStim(
    win=win, name='FixCross_Resp', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.35, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
FixCross_PostCue = visual.ShapeStim(
    win=win, name='FixCross_PostCue', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=0.25, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Cue_Image = visual.ImageStim(
    win=win,
    name='Cue_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Feedback_Text = visual.TextStim(win=win, name='Feedback_Text',
    text='default text',
    font='Calibri',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Feedback_EndBlock"
Feedback_EndBlockClock = core.Clock()
BlockEnd_Feedback_Text = visual.TextStim(win=win, name='BlockEnd_Feedback_Text',
    text='default text',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Break_Resp = keyboard.Keyboard()
Break_Text = visual.TextStim(win=win, name='Break_Text',
    text='如需要，请稍事休息，\n当您准备好请按空格\n键进入下一轮。\n',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
TY_Text = visual.TextStim(win=win, name='TY_Text',
    text='谢谢您！\n',
    font='Songti SC',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
# update component parameters for each repeat
Welc_Resp.keys = []
Welc_Resp.rt = []
# keep track of which components have finished
WelcomeComponents = [Welc_Resp, Welc_Text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welc_Resp* updates
    waitOnFlip = False
    if Welc_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welc_Resp.frameNStart = frameN  # exact frame index
        Welc_Resp.tStart = t  # local t and not account for scr refresh
        Welc_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welc_Resp, 'tStartRefresh')  # time at next scr refresh
        Welc_Resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Welc_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welc_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Welc_Resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Welc_Text* updates
    if Welc_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welc_Text.frameNStart = frameN  # exact frame index
        Welc_Text.tStart = t  # local t and not account for scr refresh
        Welc_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welc_Text, 'tStartRefresh')  # time at next scr refresh
        Welc_Text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welc_Text.started', Welc_Text.tStartRefresh)
thisExp.addData('Welc_Text.stopped', Welc_Text.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Exp_Instr"-------
# update component parameters for each repeat
ExpInstr_Resp.keys = []
ExpInstr_Resp.rt = []
# keep track of which components have finished
Exp_InstrComponents = [ExpInstr_Resp, ExpInstr_Text]
for thisComponent in Exp_InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Exp_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Exp_Instr"-------
while continueRoutine:
    # get current time
    t = Exp_InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Exp_InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExpInstr_Resp* updates
    waitOnFlip = False
    if ExpInstr_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExpInstr_Resp.frameNStart = frameN  # exact frame index
        ExpInstr_Resp.tStart = t  # local t and not account for scr refresh
        ExpInstr_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExpInstr_Resp, 'tStartRefresh')  # time at next scr refresh
        ExpInstr_Resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ExpInstr_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExpInstr_Resp.status == STARTED and not waitOnFlip:
        theseKeys = ExpInstr_Resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *ExpInstr_Text* updates
    if ExpInstr_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExpInstr_Text.frameNStart = frameN  # exact frame index
        ExpInstr_Text.tStart = t  # local t and not account for scr refresh
        ExpInstr_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExpInstr_Text, 'tStartRefresh')  # time at next scr refresh
        ExpInstr_Text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Exp_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Exp_Instr"-------
for thisComponent in Exp_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ExpInstr_Text.started', ExpInstr_Text.tStartRefresh)
thisExp.addData('ExpInstr_Text.stopped', ExpInstr_Text.tStopRefresh)
# the Routine "Exp_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Prac_Text"-------
# update component parameters for each repeat
PracInstr_Resp.keys = []
PracInstr_Resp.rt = []
# keep track of which components have finished
Prac_TextComponents = [PracInstr_Resp, PracInstr_Text]
for thisComponent in Prac_TextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Prac_TextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Prac_Text"-------
while continueRoutine:
    # get current time
    t = Prac_TextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Prac_TextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PracInstr_Resp* updates
    waitOnFlip = False
    if PracInstr_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PracInstr_Resp.frameNStart = frameN  # exact frame index
        PracInstr_Resp.tStart = t  # local t and not account for scr refresh
        PracInstr_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PracInstr_Resp, 'tStartRefresh')  # time at next scr refresh
        PracInstr_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PracInstr_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PracInstr_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PracInstr_Resp.status == STARTED and not waitOnFlip:
        theseKeys = PracInstr_Resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            PracInstr_Resp.keys = theseKeys.name  # just the last key pressed
            PracInstr_Resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *PracInstr_Text* updates
    if PracInstr_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PracInstr_Text.frameNStart = frameN  # exact frame index
        PracInstr_Text.tStart = t  # local t and not account for scr refresh
        PracInstr_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PracInstr_Text, 'tStartRefresh')  # time at next scr refresh
        PracInstr_Text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prac_TextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prac_Text"-------
for thisComponent in Prac_TextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if PracInstr_Resp.keys in ['', [], None]:  # No response was made
    PracInstr_Resp.keys = None
thisExp.addData('PracInstr_Resp.keys',PracInstr_Resp.keys)
if PracInstr_Resp.keys != None:  # we had a response
    thisExp.addData('PracInstr_Resp.rt', PracInstr_Resp.rt)
thisExp.addData('PracInstr_Resp.started', PracInstr_Resp.tStartRefresh)
thisExp.addData('PracInstr_Resp.stopped', PracInstr_Resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PracInstr_Text.started', PracInstr_Text.tStartRefresh)
thisExp.addData('PracInstr_Text.stopped', PracInstr_Text.tStopRefresh)
# the Routine "Prac_Text" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks_Prac = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks_Prac.xlsx'),
    seed=None, name='Blocks_Prac')
thisExp.addLoop(Blocks_Prac)  # add the loop to the experiment
thisBlocks_Prac = Blocks_Prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_Prac.rgb)
if thisBlocks_Prac != None:
    for paramName in thisBlocks_Prac:
        exec('{} = thisBlocks_Prac[paramName]'.format(paramName))

for thisBlocks_Prac in Blocks_Prac:
    currentLoop = Blocks_Prac
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_Prac.rgb)
    if thisBlocks_Prac != None:
        for paramName in thisBlocks_Prac:
            exec('{} = thisBlocks_Prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instr"-------
    # update component parameters for each repeat
    InstrText_Image.setImage(InstrText_File)
    Instr_Resp.keys = []
    Instr_Resp.rt = []
    # keep track of which components have finished
    InstrComponents = [InstrText_Image, Instr_Resp]
    for thisComponent in InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instr"-------
    while continueRoutine:
        # get current time
        t = InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrText_Image* updates
        if InstrText_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrText_Image.frameNStart = frameN  # exact frame index
            InstrText_Image.tStart = t  # local t and not account for scr refresh
            InstrText_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrText_Image, 'tStartRefresh')  # time at next scr refresh
            InstrText_Image.setAutoDraw(True)
        
        # *Instr_Resp* updates
        waitOnFlip = False
        if Instr_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Resp.frameNStart = frameN  # exact frame index
            Instr_Resp.tStart = t  # local t and not account for scr refresh
            Instr_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Resp, 'tStartRefresh')  # time at next scr refresh
            Instr_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Instr_Resp.keys = theseKeys.name  # just the last key pressed
                Instr_Resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instr"-------
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks_Prac.addData('InstrText_Image.started', InstrText_Image.tStartRefresh)
    Blocks_Prac.addData('InstrText_Image.stopped', InstrText_Image.tStopRefresh)
    # check responses
    if Instr_Resp.keys in ['', [], None]:  # No response was made
        Instr_Resp.keys = None
    Blocks_Prac.addData('Instr_Resp.keys',Instr_Resp.keys)
    if Instr_Resp.keys != None:  # we had a response
        Blocks_Prac.addData('Instr_Resp.rt', Instr_Resp.rt)
    Blocks_Prac.addData('Instr_Resp.started', Instr_Resp.tStartRefresh)
    Blocks_Prac.addData('Instr_Resp.stopped', Instr_Resp.tStopRefresh)
    # the Routine "Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trials_Prac = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Trials_StimPres_Prac.xlsx', selection=str(thisLoop_P)+":"+str(thisLoop_P+2)),
        seed=None, name='Trials_Prac')
    thisExp.addLoop(Trials_Prac)  # add the loop to the experiment
    thisTrials_Prac = Trials_Prac.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Prac.rgb)
    if thisTrials_Prac != None:
        for paramName in thisTrials_Prac:
            exec('{} = thisTrials_Prac[paramName]'.format(paramName))
    
    for thisTrials_Prac in Trials_Prac:
        currentLoop = Trials_Prac
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Prac.rgb)
        if thisTrials_Prac != None:
            for paramName in thisTrials_Prac:
                exec('{} = thisTrials_Prac[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FixCross"-------
        # update component parameters for each repeat
        jitter = np.arange(1, 3, .1)
        shuffle(jitter)
        # keep track of which components have finished
        FixCrossComponents = [FixCross_Image]
        for thisComponent in FixCrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FixCross"-------
        while continueRoutine:
            # get current time
            t = FixCrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross_Image* updates
            if FixCross_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross_Image.frameNStart = frameN  # exact frame index
                FixCross_Image.tStart = t  # local t and not account for scr refresh
                FixCross_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross_Image, 'tStartRefresh')  # time at next scr refresh
                FixCross_Image.setAutoDraw(True)
            if FixCross_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross_Image.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross_Image.tStop = t  # not accounting for scr refresh
                    FixCross_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixCross_Image, 'tStopRefresh')  # time at next scr refresh
                    FixCross_Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FixCross"-------
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials_Prac.addData('FixCross_Image.started', FixCross_Image.tStartRefresh)
        Trials_Prac.addData('FixCross_Image.stopped', FixCross_Image.tStopRefresh)
        # the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "StimPres_Prac"-------
        # update component parameters for each repeat
        thisLoop_P+=1
        
        PracStimPres_Images.contrast = Contrast
        PracMaskImage_Before.contrast = Contrast
        PracMaskImage_After.contrast = Contrast
        PracStimPres_Images.setImage(StimImageFile)
        PracMaskImage_Before.setImage(MaskImageFile)
        PracMaskImage_After.setImage(MaskImageFile)
        PracKeyResp.keys = []
        PracKeyResp.rt = []
        PracCue_Image.setImage(Cue)
        # keep track of which components have finished
        StimPres_PracComponents = [PracStimPres_Images, PracMaskImage_Before, PracMaskImage_After, PracKeyResp, PracFixCross_Resp, PracFixCross_PostCue, PracCue_Image]
        for thisComponent in StimPres_PracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        StimPres_PracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "StimPres_Prac"-------
        while continueRoutine:
            # get current time
            t = StimPres_PracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=StimPres_PracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PracStimPres_Images* updates
            if PracStimPres_Images.status == NOT_STARTED and frameN >= 258:
                # keep track of start time/frame for later
                PracStimPres_Images.frameNStart = frameN  # exact frame index
                PracStimPres_Images.tStart = t  # local t and not account for scr refresh
                PracStimPres_Images.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracStimPres_Images, 'tStartRefresh')  # time at next scr refresh
                PracStimPres_Images.setAutoDraw(True)
            if PracStimPres_Images.status == STARTED:
                if frameN >= (PracStimPres_Images.frameNStart + 6):
                    # keep track of stop time/frame for later
                    PracStimPres_Images.tStop = t  # not accounting for scr refresh
                    PracStimPres_Images.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracStimPres_Images, 'tStopRefresh')  # time at next scr refresh
                    PracStimPres_Images.setAutoDraw(False)
            
            # *PracMaskImage_Before* updates
            if PracMaskImage_Before.status == NOT_STARTED and frameN >= 240:
                # keep track of start time/frame for later
                PracMaskImage_Before.frameNStart = frameN  # exact frame index
                PracMaskImage_Before.tStart = t  # local t and not account for scr refresh
                PracMaskImage_Before.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracMaskImage_Before, 'tStartRefresh')  # time at next scr refresh
                PracMaskImage_Before.setAutoDraw(True)
            if PracMaskImage_Before.status == STARTED:
                if frameN >= (PracMaskImage_Before.frameNStart + 18):
                    # keep track of stop time/frame for later
                    PracMaskImage_Before.tStop = t  # not accounting for scr refresh
                    PracMaskImage_Before.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracMaskImage_Before, 'tStopRefresh')  # time at next scr refresh
                    PracMaskImage_Before.setAutoDraw(False)
            
            # *PracMaskImage_After* updates
            if PracMaskImage_After.status == NOT_STARTED and frameN >= 264:
                # keep track of start time/frame for later
                PracMaskImage_After.frameNStart = frameN  # exact frame index
                PracMaskImage_After.tStart = t  # local t and not account for scr refresh
                PracMaskImage_After.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracMaskImage_After, 'tStartRefresh')  # time at next scr refresh
                PracMaskImage_After.setAutoDraw(True)
            if PracMaskImage_After.status == STARTED:
                if frameN >= (PracMaskImage_After.frameNStart + 18):
                    # keep track of stop time/frame for later
                    PracMaskImage_After.tStop = t  # not accounting for scr refresh
                    PracMaskImage_After.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracMaskImage_After, 'tStopRefresh')  # time at next scr refresh
                    PracMaskImage_After.setAutoDraw(False)
            
            # *PracKeyResp* updates
            waitOnFlip = False
            if PracKeyResp.status == NOT_STARTED and frameN >= 108:
                # keep track of start time/frame for later
                PracKeyResp.frameNStart = frameN  # exact frame index
                PracKeyResp.tStart = t  # local t and not account for scr refresh
                PracKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracKeyResp, 'tStartRefresh')  # time at next scr refresh
                PracKeyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracKeyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracKeyResp.status == STARTED and not waitOnFlip:
                theseKeys = PracKeyResp.getKeys(keyList=['z', 'm'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    PracKeyResp.keys = theseKeys.name  # just the last key pressed
                    PracKeyResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (PracKeyResp.keys == str(CorrResp)) or (PracKeyResp.keys == CorrResp):
                        PracKeyResp.corr = 1
                    else:
                        PracKeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *PracFixCross_Resp* updates
            if PracFixCross_Resp.status == NOT_STARTED and frameN >= 282:
                # keep track of start time/frame for later
                PracFixCross_Resp.frameNStart = frameN  # exact frame index
                PracFixCross_Resp.tStart = t  # local t and not account for scr refresh
                PracFixCross_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracFixCross_Resp, 'tStartRefresh')  # time at next scr refresh
                PracFixCross_Resp.setAutoDraw(True)
            
            # *PracFixCross_PostCue* updates
            if PracFixCross_PostCue.status == NOT_STARTED and frameN >= 90:
                # keep track of start time/frame for later
                PracFixCross_PostCue.frameNStart = frameN  # exact frame index
                PracFixCross_PostCue.tStart = t  # local t and not account for scr refresh
                PracFixCross_PostCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracFixCross_PostCue, 'tStartRefresh')  # time at next scr refresh
                PracFixCross_PostCue.setAutoDraw(True)
            if PracFixCross_PostCue.status == STARTED:
                if frameN >= (PracFixCross_PostCue.frameNStart + 150):
                    # keep track of stop time/frame for later
                    PracFixCross_PostCue.tStop = t  # not accounting for scr refresh
                    PracFixCross_PostCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracFixCross_PostCue, 'tStopRefresh')  # time at next scr refresh
                    PracFixCross_PostCue.setAutoDraw(False)
            
            # *PracCue_Image* updates
            if PracCue_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracCue_Image.frameNStart = frameN  # exact frame index
                PracCue_Image.tStart = t  # local t and not account for scr refresh
                PracCue_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracCue_Image, 'tStartRefresh')  # time at next scr refresh
                PracCue_Image.setAutoDraw(True)
            if PracCue_Image.status == STARTED:
                if frameN >= 90:
                    # keep track of stop time/frame for later
                    PracCue_Image.tStop = t  # not accounting for scr refresh
                    PracCue_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracCue_Image, 'tStopRefresh')  # time at next scr refresh
                    PracCue_Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimPres_PracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "StimPres_Prac"-------
        for thisComponent in StimPres_PracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials_Prac.addData('PracStimPres_Images.started', PracStimPres_Images.tStartRefresh)
        Trials_Prac.addData('PracStimPres_Images.stopped', PracStimPres_Images.tStopRefresh)
        Trials_Prac.addData('PracMaskImage_Before.started', PracMaskImage_Before.tStartRefresh)
        Trials_Prac.addData('PracMaskImage_Before.stopped', PracMaskImage_Before.tStopRefresh)
        Trials_Prac.addData('PracMaskImage_After.started', PracMaskImage_After.tStartRefresh)
        Trials_Prac.addData('PracMaskImage_After.stopped', PracMaskImage_After.tStopRefresh)
        # check responses
        if PracKeyResp.keys in ['', [], None]:  # No response was made
            PracKeyResp.keys = None
            # was no response the correct answer?!
            if str(CorrResp).lower() == 'none':
               PracKeyResp.corr = 1;  # correct non-response
            else:
               PracKeyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for Trials_Prac (TrialHandler)
        Trials_Prac.addData('PracKeyResp.keys',PracKeyResp.keys)
        Trials_Prac.addData('PracKeyResp.corr', PracKeyResp.corr)
        if PracKeyResp.keys != None:  # we had a response
            Trials_Prac.addData('PracKeyResp.rt', PracKeyResp.rt)
        Trials_Prac.addData('PracKeyResp.started', PracKeyResp.tStartRefresh)
        Trials_Prac.addData('PracKeyResp.stopped', PracKeyResp.tStopRefresh)
        Trials_Prac.addData('PracFixCross_Resp.started', PracFixCross_Resp.tStartRefresh)
        Trials_Prac.addData('PracFixCross_Resp.stopped', PracFixCross_Resp.tStopRefresh)
        Trials_Prac.addData('PracFixCross_PostCue.started', PracFixCross_PostCue.tStartRefresh)
        Trials_Prac.addData('PracFixCross_PostCue.stopped', PracFixCross_PostCue.tStopRefresh)
        Trials_Prac.addData('PracCue_Image.started', PracCue_Image.tStartRefresh)
        Trials_Prac.addData('PracCue_Image.stopped', PracCue_Image.tStopRefresh)
        # the Routine "StimPres_Prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_Prac"-------
        # update component parameters for each repeat
        if PracKeyResp.corr == 1:
            msg="+1"
            clr="green"
        else:
            msg="0"
            clr="black"
        Feedback_Prac_Text.setColor(clr, colorSpace='rgb')
        Feedback_Prac_Text.setText(msg)
        # keep track of which components have finished
        Feedback_PracComponents = [Feedback_Prac_Text]
        for thisComponent in Feedback_PracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Feedback_PracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Feedback_Prac"-------
        while continueRoutine:
            # get current time
            t = Feedback_PracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Feedback_PracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback_Prac_Text* updates
            if Feedback_Prac_Text.status == NOT_STARTED and frameN >= 30:
                # keep track of start time/frame for later
                Feedback_Prac_Text.frameNStart = frameN  # exact frame index
                Feedback_Prac_Text.tStart = t  # local t and not account for scr refresh
                Feedback_Prac_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback_Prac_Text, 'tStartRefresh')  # time at next scr refresh
                Feedback_Prac_Text.setAutoDraw(True)
            if Feedback_Prac_Text.status == STARTED:
                if frameN >= 90:
                    # keep track of stop time/frame for later
                    Feedback_Prac_Text.tStop = t  # not accounting for scr refresh
                    Feedback_Prac_Text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Feedback_Prac_Text, 'tStopRefresh')  # time at next scr refresh
                    Feedback_Prac_Text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_PracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_Prac"-------
        for thisComponent in Feedback_PracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials_Prac.addData('Feedback_Prac_Text.started', Feedback_Prac_Text.tStartRefresh)
        Trials_Prac.addData('Feedback_Prac_Text.stopped', Feedback_Prac_Text.tStopRefresh)
        # the Routine "Feedback_Prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Trials_Prac'
    
    
    # ------Prepare to start Routine "PracEnd_Feedback"-------
    # update component parameters for each repeat
    Trials_Prac.data['PracKeyResp.corr']
    nCorr = Trials_Prac.data['PracKeyResp.corr'].sum() 
    msg = "你获得了 %i 分！" %nCorr
    PracEnd_Feedback_Text.setText(msg)
    # keep track of which components have finished
    PracEnd_FeedbackComponents = [PracEnd_Feedback_Text]
    for thisComponent in PracEnd_FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracEnd_FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracEnd_Feedback"-------
    while continueRoutine:
        # get current time
        t = PracEnd_FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracEnd_FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PracEnd_Feedback_Text* updates
        if PracEnd_Feedback_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracEnd_Feedback_Text.frameNStart = frameN  # exact frame index
            PracEnd_Feedback_Text.tStart = t  # local t and not account for scr refresh
            PracEnd_Feedback_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracEnd_Feedback_Text, 'tStartRefresh')  # time at next scr refresh
            PracEnd_Feedback_Text.setAutoDraw(True)
        if PracEnd_Feedback_Text.status == STARTED:
            if frameN >= 90:
                # keep track of stop time/frame for later
                PracEnd_Feedback_Text.tStop = t  # not accounting for scr refresh
                PracEnd_Feedback_Text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PracEnd_Feedback_Text, 'tStopRefresh')  # time at next scr refresh
                PracEnd_Feedback_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracEnd_FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracEnd_Feedback"-------
    for thisComponent in PracEnd_FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks_Prac.addData('PracEnd_Feedback_Text.started', PracEnd_Feedback_Text.tStartRefresh)
    Blocks_Prac.addData('PracEnd_Feedback_Text.stopped', PracEnd_Feedback_Text.tStopRefresh)
    # the Routine "PracEnd_Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Blocks_Prac'


# ------Prepare to start Routine "ActualRun_Instr"-------
# update component parameters for each repeat
ActualRunInstr_Resp.keys = []
ActualRunInstr_Resp.rt = []
# keep track of which components have finished
ActualRun_InstrComponents = [ActualRunInstr_Resp, ActualRun_text]
for thisComponent in ActualRun_InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ActualRun_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ActualRun_Instr"-------
while continueRoutine:
    # get current time
    t = ActualRun_InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ActualRun_InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ActualRunInstr_Resp* updates
    waitOnFlip = False
    if ActualRunInstr_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ActualRunInstr_Resp.frameNStart = frameN  # exact frame index
        ActualRunInstr_Resp.tStart = t  # local t and not account for scr refresh
        ActualRunInstr_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ActualRunInstr_Resp, 'tStartRefresh')  # time at next scr refresh
        ActualRunInstr_Resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ActualRunInstr_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ActualRunInstr_Resp.status == STARTED and not waitOnFlip:
        theseKeys = ActualRunInstr_Resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *ActualRun_text* updates
    if ActualRun_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ActualRun_text.frameNStart = frameN  # exact frame index
        ActualRun_text.tStart = t  # local t and not account for scr refresh
        ActualRun_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ActualRun_text, 'tStartRefresh')  # time at next scr refresh
        ActualRun_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ActualRun_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ActualRun_Instr"-------
for thisComponent in ActualRun_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ActualRun_text.started', ActualRun_text.tStartRefresh)
thisExp.addData('ActualRun_text.stopped', ActualRun_text.tStopRefresh)
# the Routine "ActualRun_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks_even.xlsx'),
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instr"-------
    # update component parameters for each repeat
    InstrText_Image.setImage(InstrText_File)
    Instr_Resp.keys = []
    Instr_Resp.rt = []
    # keep track of which components have finished
    InstrComponents = [InstrText_Image, Instr_Resp]
    for thisComponent in InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instr"-------
    while continueRoutine:
        # get current time
        t = InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrText_Image* updates
        if InstrText_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrText_Image.frameNStart = frameN  # exact frame index
            InstrText_Image.tStart = t  # local t and not account for scr refresh
            InstrText_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrText_Image, 'tStartRefresh')  # time at next scr refresh
            InstrText_Image.setAutoDraw(True)
        
        # *Instr_Resp* updates
        waitOnFlip = False
        if Instr_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Resp.frameNStart = frameN  # exact frame index
            Instr_Resp.tStart = t  # local t and not account for scr refresh
            Instr_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Resp, 'tStartRefresh')  # time at next scr refresh
            Instr_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Instr_Resp.keys = theseKeys.name  # just the last key pressed
                Instr_Resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instr"-------
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks.addData('InstrText_Image.started', InstrText_Image.tStartRefresh)
    Blocks.addData('InstrText_Image.stopped', InstrText_Image.tStopRefresh)
    # check responses
    if Instr_Resp.keys in ['', [], None]:  # No response was made
        Instr_Resp.keys = None
    Blocks.addData('Instr_Resp.keys',Instr_Resp.keys)
    if Instr_Resp.keys != None:  # we had a response
        Blocks.addData('Instr_Resp.rt', Instr_Resp.rt)
    Blocks.addData('Instr_Resp.started', Instr_Resp.tStartRefresh)
    Blocks.addData('Instr_Resp.stopped', Instr_Resp.tStopRefresh)
    # the Routine "Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Trials_StimPres_even.xlsx', selection=str(thisLoop)+":"+str(thisLoop+20)),
        seed=None, name='Trials')
    thisExp.addLoop(Trials)  # add the loop to the experiment
    thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in Trials:
        currentLoop = Trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FixCross"-------
        # update component parameters for each repeat
        jitter = np.arange(1, 3, .1)
        shuffle(jitter)
        # keep track of which components have finished
        FixCrossComponents = [FixCross_Image]
        for thisComponent in FixCrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FixCross"-------
        while continueRoutine:
            # get current time
            t = FixCrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross_Image* updates
            if FixCross_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross_Image.frameNStart = frameN  # exact frame index
                FixCross_Image.tStart = t  # local t and not account for scr refresh
                FixCross_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross_Image, 'tStartRefresh')  # time at next scr refresh
                FixCross_Image.setAutoDraw(True)
            if FixCross_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross_Image.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross_Image.tStop = t  # not accounting for scr refresh
                    FixCross_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixCross_Image, 'tStopRefresh')  # time at next scr refresh
                    FixCross_Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FixCross"-------
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials.addData('FixCross_Image.started', FixCross_Image.tStartRefresh)
        Trials.addData('FixCross_Image.stopped', FixCross_Image.tStopRefresh)
        # the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Stim_Pres"-------
        # update component parameters for each repeat
        thisLoop +=1
        
        Stim_Pres_Image.contrast = Contrast
        Mask_Before_Image.contrast = Contrast
        Mask_After_Image.contrast = Contrast
        Stim_Pres_Image.setImage(StimImageFile)
        Mask_Before_Image.setImage(MaskImageFile)
        Mask_After_Image.setImage(MaskImageFile)
        KeyResp.keys = []
        KeyResp.rt = []
        Cue_Image.setImage(Cue)
        # keep track of which components have finished
        Stim_PresComponents = [Stim_Pres_Image, Mask_Before_Image, Mask_After_Image, KeyResp, FixCross_Resp, FixCross_PostCue, Cue_Image]
        for thisComponent in Stim_PresComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Stim_PresClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Stim_Pres"-------
        while continueRoutine:
            # get current time
            t = Stim_PresClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Stim_PresClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_Pres_Image* updates
            if Stim_Pres_Image.status == NOT_STARTED and frameN >= 258:
                # keep track of start time/frame for later
                Stim_Pres_Image.frameNStart = frameN  # exact frame index
                Stim_Pres_Image.tStart = t  # local t and not account for scr refresh
                Stim_Pres_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_Pres_Image, 'tStartRefresh')  # time at next scr refresh
                Stim_Pres_Image.setAutoDraw(True)
            if Stim_Pres_Image.status == STARTED:
                if frameN >= (Stim_Pres_Image.frameNStart + 6):
                    # keep track of stop time/frame for later
                    Stim_Pres_Image.tStop = t  # not accounting for scr refresh
                    Stim_Pres_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Stim_Pres_Image, 'tStopRefresh')  # time at next scr refresh
                    Stim_Pres_Image.setAutoDraw(False)
            
            # *Mask_Before_Image* updates
            if Mask_Before_Image.status == NOT_STARTED and frameN >= 240:
                # keep track of start time/frame for later
                Mask_Before_Image.frameNStart = frameN  # exact frame index
                Mask_Before_Image.tStart = t  # local t and not account for scr refresh
                Mask_Before_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mask_Before_Image, 'tStartRefresh')  # time at next scr refresh
                Mask_Before_Image.setAutoDraw(True)
            if Mask_Before_Image.status == STARTED:
                if frameN >= (Mask_Before_Image.frameNStart + 18):
                    # keep track of stop time/frame for later
                    Mask_Before_Image.tStop = t  # not accounting for scr refresh
                    Mask_Before_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Mask_Before_Image, 'tStopRefresh')  # time at next scr refresh
                    Mask_Before_Image.setAutoDraw(False)
            
            # *Mask_After_Image* updates
            if Mask_After_Image.status == NOT_STARTED and frameN >= 264:
                # keep track of start time/frame for later
                Mask_After_Image.frameNStart = frameN  # exact frame index
                Mask_After_Image.tStart = t  # local t and not account for scr refresh
                Mask_After_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mask_After_Image, 'tStartRefresh')  # time at next scr refresh
                Mask_After_Image.setAutoDraw(True)
            if Mask_After_Image.status == STARTED:
                if frameN >= (Mask_After_Image.frameNStart + 18):
                    # keep track of stop time/frame for later
                    Mask_After_Image.tStop = t  # not accounting for scr refresh
                    Mask_After_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Mask_After_Image, 'tStopRefresh')  # time at next scr refresh
                    Mask_After_Image.setAutoDraw(False)
            
            # *KeyResp* updates
            waitOnFlip = False
            if KeyResp.status == NOT_STARTED and frameN >= 108:
                # keep track of start time/frame for later
                KeyResp.frameNStart = frameN  # exact frame index
                KeyResp.tStart = t  # local t and not account for scr refresh
                KeyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(KeyResp, 'tStartRefresh')  # time at next scr refresh
                KeyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(KeyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(KeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if KeyResp.status == STARTED and not waitOnFlip:
                theseKeys = KeyResp.getKeys(keyList=['z', 'm'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    KeyResp.keys = theseKeys.name  # just the last key pressed
                    KeyResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (KeyResp.keys == str(CorrResp)) or (KeyResp.keys == CorrResp):
                        KeyResp.corr = 1
                    else:
                        KeyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *FixCross_Resp* updates
            if FixCross_Resp.status == NOT_STARTED and frameN >= 282:
                # keep track of start time/frame for later
                FixCross_Resp.frameNStart = frameN  # exact frame index
                FixCross_Resp.tStart = t  # local t and not account for scr refresh
                FixCross_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross_Resp, 'tStartRefresh')  # time at next scr refresh
                FixCross_Resp.setAutoDraw(True)
            
            # *FixCross_PostCue* updates
            if FixCross_PostCue.status == NOT_STARTED and frameN >= 90:
                # keep track of start time/frame for later
                FixCross_PostCue.frameNStart = frameN  # exact frame index
                FixCross_PostCue.tStart = t  # local t and not account for scr refresh
                FixCross_PostCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross_PostCue, 'tStartRefresh')  # time at next scr refresh
                FixCross_PostCue.setAutoDraw(True)
            if FixCross_PostCue.status == STARTED:
                if frameN >= (FixCross_PostCue.frameNStart + 150):
                    # keep track of stop time/frame for later
                    FixCross_PostCue.tStop = t  # not accounting for scr refresh
                    FixCross_PostCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixCross_PostCue, 'tStopRefresh')  # time at next scr refresh
                    FixCross_PostCue.setAutoDraw(False)
            
            # *Cue_Image* updates
            if Cue_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cue_Image.frameNStart = frameN  # exact frame index
                Cue_Image.tStart = t  # local t and not account for scr refresh
                Cue_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cue_Image, 'tStartRefresh')  # time at next scr refresh
                Cue_Image.setAutoDraw(True)
            if Cue_Image.status == STARTED:
                if frameN >= 90:
                    # keep track of stop time/frame for later
                    Cue_Image.tStop = t  # not accounting for scr refresh
                    Cue_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Cue_Image, 'tStopRefresh')  # time at next scr refresh
                    Cue_Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Stim_PresComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Stim_Pres"-------
        for thisComponent in Stim_PresComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials.addData('Stim_Pres_Image.started', Stim_Pres_Image.tStartRefresh)
        Trials.addData('Stim_Pres_Image.stopped', Stim_Pres_Image.tStopRefresh)
        Trials.addData('Mask_Before_Image.started', Mask_Before_Image.tStartRefresh)
        Trials.addData('Mask_Before_Image.stopped', Mask_Before_Image.tStopRefresh)
        Trials.addData('Mask_After_Image.started', Mask_After_Image.tStartRefresh)
        Trials.addData('Mask_After_Image.stopped', Mask_After_Image.tStopRefresh)
        # check responses
        if KeyResp.keys in ['', [], None]:  # No response was made
            KeyResp.keys = None
            # was no response the correct answer?!
            if str(CorrResp).lower() == 'none':
               KeyResp.corr = 1;  # correct non-response
            else:
               KeyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for Trials (TrialHandler)
        Trials.addData('KeyResp.keys',KeyResp.keys)
        Trials.addData('KeyResp.corr', KeyResp.corr)
        if KeyResp.keys != None:  # we had a response
            Trials.addData('KeyResp.rt', KeyResp.rt)
        Trials.addData('KeyResp.started', KeyResp.tStartRefresh)
        Trials.addData('KeyResp.stopped', KeyResp.tStopRefresh)
        Trials.addData('FixCross_Resp.started', FixCross_Resp.tStartRefresh)
        Trials.addData('FixCross_Resp.stopped', FixCross_Resp.tStopRefresh)
        Trials.addData('FixCross_PostCue.started', FixCross_PostCue.tStartRefresh)
        Trials.addData('FixCross_PostCue.stopped', FixCross_PostCue.tStopRefresh)
        Trials.addData('Cue_Image.started', Cue_Image.tStartRefresh)
        Trials.addData('Cue_Image.stopped', Cue_Image.tStopRefresh)
        # the Routine "Stim_Pres" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        # update component parameters for each repeat
        if KeyResp.corr == 1:
            msg="+1"
            clr="green"
        else:
            msg="0"
            clr="black"
        Feedback_Text.setColor(clr, colorSpace='rgb')
        Feedback_Text.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = [Feedback_Text]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Feedback"-------
        while continueRoutine:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback_Text* updates
            if Feedback_Text.status == NOT_STARTED and frameN >= 30:
                # keep track of start time/frame for later
                Feedback_Text.frameNStart = frameN  # exact frame index
                Feedback_Text.tStart = t  # local t and not account for scr refresh
                Feedback_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback_Text, 'tStartRefresh')  # time at next scr refresh
                Feedback_Text.setAutoDraw(True)
            if Feedback_Text.status == STARTED:
                if frameN >= 90:
                    # keep track of stop time/frame for later
                    Feedback_Text.tStop = t  # not accounting for scr refresh
                    Feedback_Text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Feedback_Text, 'tStopRefresh')  # time at next scr refresh
                    Feedback_Text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials.addData('Feedback_Text.started', Feedback_Text.tStartRefresh)
        Trials.addData('Feedback_Text.stopped', Feedback_Text.tStopRefresh)
        # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Trials'
    
    
    # ------Prepare to start Routine "Feedback_EndBlock"-------
    # update component parameters for each repeat
    Trials.data['KeyResp.corr']
    nCorr = Trials.data['KeyResp.corr'].sum() 
    msg = "你获得了 %i 分!" %nCorr
    BlockEnd_Feedback_Text.setText(msg)
    # keep track of which components have finished
    Feedback_EndBlockComponents = [BlockEnd_Feedback_Text]
    for thisComponent in Feedback_EndBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback_EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedback_EndBlock"-------
    while continueRoutine:
        # get current time
        t = Feedback_EndBlockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback_EndBlockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlockEnd_Feedback_Text* updates
        if BlockEnd_Feedback_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlockEnd_Feedback_Text.frameNStart = frameN  # exact frame index
            BlockEnd_Feedback_Text.tStart = t  # local t and not account for scr refresh
            BlockEnd_Feedback_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlockEnd_Feedback_Text, 'tStartRefresh')  # time at next scr refresh
            BlockEnd_Feedback_Text.setAutoDraw(True)
        if BlockEnd_Feedback_Text.status == STARTED:
            if frameN >= 90:
                # keep track of stop time/frame for later
                BlockEnd_Feedback_Text.tStop = t  # not accounting for scr refresh
                BlockEnd_Feedback_Text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlockEnd_Feedback_Text, 'tStopRefresh')  # time at next scr refresh
                BlockEnd_Feedback_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback_EndBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback_EndBlock"-------
    for thisComponent in Feedback_EndBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks.addData('BlockEnd_Feedback_Text.started', BlockEnd_Feedback_Text.tStartRefresh)
    Blocks.addData('BlockEnd_Feedback_Text.stopped', BlockEnd_Feedback_Text.tStopRefresh)
    # the Routine "Feedback_EndBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break"-------
    # update component parameters for each repeat
    Break_Resp.keys = []
    Break_Resp.rt = []
    # keep track of which components have finished
    BreakComponents = [Break_Resp, Break_Text]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_Resp* updates
        waitOnFlip = False
        if Break_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_Resp.frameNStart = frameN  # exact frame index
            Break_Resp.tStart = t  # local t and not account for scr refresh
            Break_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_Resp, 'tStartRefresh')  # time at next scr refresh
            Break_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Break_Resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Break_Resp.keys = theseKeys.name  # just the last key pressed
                Break_Resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_Text* updates
        if Break_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_Text.frameNStart = frameN  # exact frame index
            Break_Text.tStart = t  # local t and not account for scr refresh
            Break_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_Text, 'tStartRefresh')  # time at next scr refresh
            Break_Text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Break_Resp.keys in ['', [], None]:  # No response was made
        Break_Resp.keys = None
    Blocks.addData('Break_Resp.keys',Break_Resp.keys)
    if Break_Resp.keys != None:  # we had a response
        Blocks.addData('Break_Resp.rt', Break_Resp.rt)
    Blocks.addData('Break_Resp.started', Break_Resp.tStartRefresh)
    Blocks.addData('Break_Resp.stopped', Break_Resp.tStopRefresh)
    Blocks.addData('Break_Text.started', Break_Text.tStartRefresh)
    Blocks.addData('Break_Text.stopped', Break_Text.tStopRefresh)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Blocks'


# ------Prepare to start Routine "ThankYou"-------
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [TY_Text]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ThankYou"-------
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TY_Text* updates
    if TY_Text.status == NOT_STARTED and frameN >= 0.0:
        # keep track of start time/frame for later
        TY_Text.frameNStart = frameN  # exact frame index
        TY_Text.tStart = t  # local t and not account for scr refresh
        TY_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TY_Text, 'tStartRefresh')  # time at next scr refresh
        TY_Text.setAutoDraw(True)
    if TY_Text.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 3-frameTolerance:
            # keep track of stop time/frame for later
            TY_Text.tStop = t  # not accounting for scr refresh
            TY_Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TY_Text, 'tStopRefresh')  # time at next scr refresh
            TY_Text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TY_Text.started', TY_Text.tStartRefresh)
thisExp.addData('TY_Text.stopped', TY_Text.tStopRefresh)
# the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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

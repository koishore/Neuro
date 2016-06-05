import pyttsx
import random
from Tkinter import *
import time

root = Tk()
root.configure(background = '#000c1a')

old = ['a state of benefit: advantage','awkward in action: clumsy','tendency of mind: attitude','ability to accomplish: might','animal with wings: bird','masticating apparatus: mouth','be the pleasure of: please','finest point or part: noon','majority of instances: most','condition or attribute: circumstance','remain alive: live','a small cube: dice','to consume by: eat','a thrusting blow: punch','a limited interval: time','expression of sorrow: sad','division of literary word: book','without definitive aim: random','form of solid nourishment: food','the celestial heaven: sky','relatively little extent: thin','float in air: fly','in an erect position: up','set of incoherent particles: mass','form of denomination: money','from one system to another: migrate','garment for body: clothes','expression of mirth: laugh','water suspended in air: cloud','downward thrust of foot: stamp']

new1 = ['remain alive: live','a small cube: dice','to consume by: eat','a thrusting blow: punch','a limited interval: time','expression of sorrow: sad','division of literary word: book','without definitive aim: random','form of solid nourishment: food','the celestial heaven: sky','relatively little extent: thin','float in air: fly','in an erect position: up','set of incoherent particles: mass','form of denomination: money','from one system to another: migrate','garment for body: clothes','expression of mirth: laugh','water suspended in air: cloud','downward thrust of foot: stamp']

new2 = ['a state of benefit: advantage','awkward in action: clumsy','tendency of mind: attitude','ability to accomplish: might','animal with wings: bird','masticating apparatus: mouth','be the pleasure of: please','finest point or part: noon','majority of instances: most','condition or attribute: circumstance','major natural elevation: mountain','fail to encounter: miss','elaborate vocal signal: song','not ever: never','condition with respect to: position','territory of a nation: country','extend in undulations: roll','to examine: search','to gaze in a specific manner: look','amiably pleasant: nice']

new3 = ['one that computes: computer','short, irregular movements: wiggle','to know how to: can','figure of representation: emblem','uprightly formed: straight','substance for curing disease: medicine','to rise suddenly: jump','piece of rock: stone','neutralise active qualities: kill','journey by water: sail','blossom of a plant: flower','absence of quantity: zero','sequence of a record: list','to feel aversion: hate','appointment for a time: date','concise use of something: economy','art of sound: music','portion bounded by a curve: circle','sequential arrangement: index','art of illusions: magic']

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def instruction():

	engine.say("A sentence comprises of a sentence frame and a semantically related word. For example: definition of something: meaning. The sentences will be repeated twice with a interval of 3 seconds in between. There are a total of 30 sentences in the initial testing. Try to remember the sentences. 24 hours later, you will be required to undergo a similar test. There are a total of 60 sentences in the final testing. You will have to classify the sentences as old or new while your brain activity is monitored.  Press TRIAL to hear a trial. Press INITIAL to begin the initial testing. Press FINAL to begin final testing.")
	engine.runAndWait()
	time.sleep(1)

def trial():

	engine.say("definition of something: meaning.")
	engine.runAndWait()
	time.sleep(2)
	engine.say("definition of something: meaning.")
	engine.runAndWait()
	time.sleep(1)

def initial():

	for j in range (0,30):
	
		randold = random.choice(old)
		old.remove(randold)
		
		for jsub in range (0,2):

			engine.say(randold)
			engine.runAndWait()
			time.sleep(2)

def final():

	for k1 in range (0,20):
	
		randnew1 = random.choice(new1)
		new1.remove(randnew1)
		
		engine.say(randnew1)
		engine.runAndWait()
		time.sleep(2)

	for k2 in range (0,20):
	
		randnew2 = random.choice(new2)
		new2.remove(randnew2)
		
		engine.say(randnew2)
		engine.runAndWait()
		time.sleep(2)

	for k3 in range (0,20):
	
		randnew3 = random.choice(new3)
		new3.remove(randnew3)
		
		engine.say(randnew3)
		engine.runAndWait()
		time.sleep(2)

labelframe = LabelFrame(root, bg = '#000c1a')
labelframe.pack(fill="both", expand="yes")
 
head = Label(labelframe, bg = '#000c1a', text="Instructions", font = ('Lato', 20), fg = "#669999")
head.pack(side = TOP)

left = Label(labelframe, bg = '#000c1a', text="A sentence comprises of a sentence frame and a semantically related word.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="For example: definition of something: meaning.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="The sentences will be repeated twice with a interval of 2 seconds in between.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="There are a total of 30 sentences in the initial testing.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="Try to remember the sentences.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="24 hours later, you will be required to undergo a similar test.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="There are a total of 60 sentences in the final testing.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="You will have to classify the sentences as old or new while your brain activity is monitored.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="Press INSTRUCTIONS to hear these instructions.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="Press TRIAL to hear a trial.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="Press INITIAL to begin the initial testing.", font = ('Lato', 15), fg = "#669999")
left.pack()

left = Label(labelframe, bg = '#000c1a', text="Press FINAL to begin final testing.", font = ('Lato', 15), fg = "#669999")
left.pack()

bins = Button(root, text = "INSTRUCTIONS", command = instruction, bg = '#000011', bd = 0, font = ('Lato', 30),pady = 10, padx = 50, fg = '#4590b4')
bins.pack(side = LEFT)

bt = Button(root, text = "TRIAL", command = trial, bg = '#000011', bd = 0, font = ('Lato', 30),pady = 10, padx = 50, fg = '#4590b4')
bt.pack(side = LEFT)

bi = Button(root, text = "INITIAL", command = initial, bg = '#000011', bd = 0, font = ('Lato', 30),pady = 10, padx = 50, fg = '#4590b4')
bi.pack(side = RIGHT)

bf = Button(root, text = "FINAL", command = final, bg = '#000011', bd = 0, font = ('Lato', 30),pady = 10, padx = 50, fg = '#4590b4')
bf.pack(side = RIGHT)

root.mainloop()

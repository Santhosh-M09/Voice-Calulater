import speech_recognition as sr
import pyttsx3
import math as m

listener = sr.Recognizer() # voice recognizer
mic = sr.Microphone() # microphone method
engine = pyttsx3.init() # text to speech method
voices = engine.getProperty('voices') # getting properties of all voices
engine.setProperty('voice', voices[1].id) # setting female voice id


def talk(text): # function to text to speech
    engine.say(text)
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice command
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# responses for the user
response=['Welcome to smart calculator','My name is Tesa',
		'Thanks for enjoy with me ','Sorry ,this is beyond my ability']
# calculating LCM
def lcm(a,b):
	L=a if a>b else b
	while L<=a*b:
		if L%a==0 and L%b==0:
			return L
		L+=1

# calculating HCF
def hcf(a,b):
	H=a if a<b else b
	while H>=1:
		if a%H==0 and b%H==0:
			return H
		H-=1

# Addition
def add(a,b):
	return a+b

# Subtraction
def sub(a,b):
	return a-b

# Multiplication
def mul(a,b):
	return a*b

# Division
def div(a,b):
	return a/b

# Remainder
def mod(a,b):
	return a%b

# Scientific calculations
# Square Root
def sqr(a):
    return m.sqrt(a)

# Power
def pow(a, b):
    return m.pow(a, b)

# Cosine
def cos(a):
    return m.cos(a)

# Sin
def sin(a):
    return m.sin(a)

# Tan
def tan(a):
    return m.tan(a)

# Degrees
def degrees(a):
    return m.degrees(a)

# Floor value
def floor(a):
    return m.floor(a)

# Factorial
def fact(a):
    return m.factorial(a)
    
# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    talk(response[2])
    input('press enter key to exit')
    exit()

def myname(): 
    print(response[1])
    talk(response[1])
def sorry():
    print(response[3])
    talk(response[3])

# Arithmetic functions to pass through
operations = {'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,
			'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,
			'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,
			'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,
			'INTO':mul,'DIVISION':div,'MOD':mod,'REMANDER'
			:mod,'MODULAS':mod, 'SQUARE':sqr, 'ROOT' : sqr,
            'POWER':pow, 'COSINE': cos, 'TAN':tan, 'SIN': sin,
            'DEGREE':degrees, 'FLOOR': floor, 'FACTORIAL':fact}

def extract_from_text(text): # to extract numbers from string
    l=[]
    for t in text.split(' '): # to seperate words
        try:
            l.append(float(t)) # to append integers to list 'l'

        except ValueError:   # to pass if strings are present
            pass
    return l

commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}
		
print('--------------'+response[0]+'------------')
print('--------------'+response[1]+'--------------------')
talk(response[0])
talk(response[1])

while True:
    text = take_command()
    for word in text.split(' '):
        if word.upper() in operations.keys(): # to enter the correct arithmetic function
            try:
                l = extract_from_text(text) # getting numbers for calculation
                if len(l) > 1:  
                    r = operations[word.upper()] (l[0],l[1])    # for basic calculations                    
                    print(r) # returning value of basic calculations
                    talk(r)
                else:
                    m = operations[word.upper()] (l[0]) # for scientific calculations                    
                    print(m) # returning value of scientific calculations
                    talk(m)
            except:
                talk('something went wrong plz enter again !!')
                print('something went wrong plz enter again !!')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()] ()
            break
    else:
        sorry()
        
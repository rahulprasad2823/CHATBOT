from nltk.chat.util import Chat, reflections
import requests
import time
from datetime import datetime

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is J.A.R.V.I.S like in Iron Man, but you can just call me Jarvis and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing very well\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
      r"how is the condition in India is (.*)?",
      ["Great, India is developing.",]
    ],
    [
      r"who is the creator of Corona virus?",
      ["One and only China.",]
      
    ],
    [
      r"can we get rid of COVID-19(.*)?",
      ["yes,if god decides.",]
    ],
    [
      r"which is the most affected country with covid-19?",
      ["sadly, USA is the most affected one.",]
    ],
    [
      r"can anyone donate to get rid of the virus ?",
      ["yes,if he/she likes to donate.",]
    ],
    [
      r"(.*) is required to stop the virus?",
      ["yes,lockdown will stop spreading of the virus.",]
    ],
    [
      r"do social distancing is important in the present situation ?",
      ["it is going to help alot.",]
    ],
    [
      r"do precautions are needed to be safe ?",
      ["yes, without precautions your not safe.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["RahulVamshi created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['LPU, INDIA',]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is amazing like always","It's hot here in %1","It's chilli here in %1", "In %1 there is a 50% chance of rain",]
    ],
    [
        r"i work (in|at) (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"is it (.*) in (.*)",
        ["No its not %1 in %2","It could be", "Yes its %1 in %2"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Kohli", "ABD"]
],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["THOR"]
],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

#A Function to run the chatbot
def chatty():
  print("Hi, I'm CHATBOT and I want to help and chat with you ! \nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
  chat = Chat(pairs,reflections )
  chat.converse()
  
#Run the chatbot
chatty()
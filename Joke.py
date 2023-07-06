import random
from translate import Translator

RandomyJokey = {
    
  "1" : "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? An Echo ",
  
  "2": "You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. A candle." ,
  
  "3" : "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? A Map ",  
  
  "4" : "What is seen in the middle of March and April that can’t be seen at the beginning or end of either month? The letter R",
  
  "5" : "You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why? All the people were married.",
  
  "6" : "What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word? Heroine ",
  

  "7" : "I come from a mine and get surrounded by wood always. Everyone uses me. What am I? A Pencil lead ",

  "8" : "What disappears as soon as you say its name? Selince",

  "9" : "I have keys, but no locks and space, and no rooms. You can enter, but you can’t go outside. What am I?A keyboard ",

  "10" : "What gets wet while drying? A towel ",
  
  "11" : "How many letters are in the alphabet? There are 11 letters in the words “the alphabet",
  
  1 : "Which school does an ice cream man go to? Sundae school",

  2 : "Why is the teacher wearing sunglasses in the class? Because she has bright students in her class",

  3: "Why do music teachers do well in a baseball game? Because they have a perfect pitch",

  4: """  Knock, Knock
  Who’s there?
  A broken pencil
  A broken pencil who?
  Never mind… It’s pointless!""",

  5: "Name the flying mammal in the kindergarten class. AlphaBAT",
  
  6 : 'What’s so fresh in the chemistry class? The experiMINTS',

  7 : 'Why did the student throw her watch out of the school window? She wanted to see time fly.',

  8 : "Why do magicians score well in exams? Because they can handle tricky questions",

  9 : "Name the dinosaur that has the best vocabulary. The thesaurus",

  10: " Why does the math class make students sad? Because it is full of problems",

  11 :" Why does the music teacher need a ladder in the school? To reach higher notes",

  12:" How do bees go to school? By school buzz",

  13 : "I would love to change the world, but they won't give me the source code.",
  
  14 : "If at first you don't succeed, call it version 1.0.",
  
    15 : "Q: What is 001011010110101010100101010010101015 in binary? A: A major glitch!",
  
    16: "What do you call a python which is exactly 3.14m long ? A πthon",
  
    17: "Did you hear about the computer nerd who was nearly eaten alive by a giant snake? Now he's programming in python.",
    
    18: 'Knock, knock. Who’s There? Very long pause… “Java.”',
  
    19 : 'Why do Java developers wear glasses? Because they don’t C#!',
  
    20 : "A C++ walks into a bar and sees a C. C is drunk, falling on the floor spitting and rolling. How classless! says C++.",
  
    21 : "What is an algorithm? A word programmers use when they don’t want to explain what they did.",
  
    22: """  How does machine learning work?
Q: What is 11 times 11?
A: It’s 65.
Q: Not at all. It’s 121.
A: It’s 121.""",
  
    23:" Two programmers are talking about their social life, and one says: The only date I get is the Java Update.",
  
    24:"What is an object-oriented way to become wealth. Inheritance."
  
  }
Schooly = {
  1 : "Which school does an ice cream man go to? Sundae school",

  2 : "Why is the teacher wearing sunglasses in the class? Because she has bright students in her class",

  3: "Why do music teachers do well in a baseball game? Because they have a perfect pitch",

  4: """  Knock, Knock
  Who’s there?
  A broken pencil
  A broken pencil who?
  Never mind… It’s pointless!""",

  5: "Name the flying mammal in the kindergarten class. AlphaBAT",
  
  6 : 'What’s so fresh in the chemistry class? The experiMINTS',

  7 : 'Why did the student throw her watch out of the school window? She wanted to see time fly.',

  8 : "Why do magicians score well in exams? Because they can handle tricky questions",

  9 : "Name the dinosaur that has the best vocabulary. The thesaurus",

  10: " Why does the math class make students sad? Because it is full of problems",

11 :" Why does the music teacher need a ladder in the school? To reach higher notes",

12:" How do bees go to school? By school buzz"
}
Hardestriddles = {
  "1" : "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? An Echo ",
  
  "2": "You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. A candle." ,
  
  "3" : "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? A Map ",  
  
  "4" : "What is seen in the middle of March and April that can’t be seen at the beginning or end of either month? The letter R",
  
  "5" : "You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why? All the people were married.",
  
  "6" : "What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word? Heroine ",
  

  "7" : "I come from a mine and get surrounded by wood always. Everyone uses me. What am I? A Pencil lead ",

  "8" : "What disappears as soon as you say its name? Selince",

  "9" : "I have keys, but no locks and space, and no rooms. You can enter, but you can’t go outside. What am I?A keyboard ",

  "10" : "What gets wet while drying? A towel ",
  
  "11" : "How many letters are in the alphabet? There are 11 letters in the words “the alphabet",

  }
CodingJoks = {
    13 : "I would love to change the world, but they won't give me the source code.",
  
    14 : "If at first you don't succeed, call it version 1.0.",
  
    15 : "Q: What is 001011010110101010100101010010101015 in binary? A: A major glitch!",
  
    16: "What do you call a python which is exactly 3.14m long ? A πthon",
  
    17: "Did you hear about the computer nerd who was nearly eaten alive by a giant snake? Now he's programming in python.",
    
    18: 'Knock, knock. Who’s There? Very long pause… “Java.”',
  
    19 : 'Why do Java developers wear glasses? Because they don’t C#!',
  
    20 : "A C++ walks into a bar and sees a C. C is drunk, falling on the floor spitting and rolling. How classless! says C++.",
  
    21 : "What is an algorithm? A word programmers use when they don’t want to explain what they did.",
  
    22: """  How does machine learning work?
Q: What is 11 times 11?
A: It’s 65.
Q: Not at all. It’s 121.
A: It’s 121.""",
  
    23:" Two programmers are talking about their social life, and one says: The only date I get is the Java Update.",
  
    24:"What is an object-oriented way to become wealth. Inheritance."
  }
DadJoks = {
  
  1 : "What did the zero say to the eight?" "That belt looks good on you.", 
  2: "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.",
  3: "Where do fruits go on vacation? Pear-is!", 
  9:"I asked my dog what's two minus two. He said nothing.",
  4: "What did Baby Corn say to Mama Corn? Where's Pop Corn?", 
  5:"What's the best thing about Switzerland?" "I don't know, but the flag is a big plus.",
  6:"What does a sprinter eat before a race? Nothing, they fast!", 
  7:"Where do you learn to make a banana split? Sundae school.", 
  8:"What has more letters than the alphabet? The post office!", 
  10: "Dad, did you get a haircut? No, I got them all cut!",
  11:"What do you call a poor Santa Claus? St. Nickel-less.", 
  12:"I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
  13:"Where do boats go when they're sick? To the boat doc." ,
  14: "I don't trust those trees. They seem kind of shady." }

def Riddles(Language): 

  JokesUp = random.choice(list(Hardestriddles.values()))
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")
  
def Get_Joke (Language):
  Language = str(Language)
  
  JokesUp = random.choice(list(RandomyJokey.values()))
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")
  

def SchoolJoke (Language):
  Language = str(Language)
  global Schooly
  JokesUp = random.choice(list(Schooly.values()))
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")

def CodingJokes(Language):
  Language = str(Language)
  JokesUp = random.choice(list(CodingJoks.values()))
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")

def BadJokes(Language):
  JokesUp = random.choice(list(DadJoks.values()))
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")
  
def PrintJoke(Jokey, Language):
  Language = str(Language)
  JokesUp = Jokey
  translator = Translator(to_lang=Language)
  translation = translator.translate(JokesUp)
  print(translation)
  print("")

def AddToGet_Joke(Joke):
  Jokely = RandomyJokey.update({20: Joke})

def AddToSchoolJoke(Joke):
  Jokely = Schooly.update({20: Joke})

def AddToRiddles(Joke):
  Jokely = Hardestriddles.update({20: Joke})

def AddToCodingJoke(Joke):
  Jokely = CodingJoks.update({20: Joke})


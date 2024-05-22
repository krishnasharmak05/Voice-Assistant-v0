# Use indexes and lists to do a random choice from selected jokes from the below urls - DONE
# Get JARVIS to say some jokes - DONE

# Use NLP and neural networks to make my voice assistant give greetings and general feedback, info about itself, and such stuff...


import random
import sys
import time
import pyttsx3 as tts
import threading


def write_with_animation(word: str, type_delay: float):
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(type_delay)
    # print("Animation:", end= " ")
    # print(threading.current_thread().name)


def say_jokes(given_joke):
    engine = tts.init()
    tts_settings(engine)
    engine.say(given_joke)
    engine.runAndWait()
    engine.stop()
    #print("TTS: ",end = "")
    #print(threading.current_thread().name)


def tts_settings(engine):
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)

    # VOLUME
    volume = engine.getProperty("volume") 
    engine.setProperty("volume", 1.0)

    # VOICE
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id) 


def joke_selector():
    jokes = {
        "I told my wife she should embrace her mistakes -": " She gave me a hug.",
        "Parallel lines have so much in common.": " It's a shame they'll never meet.",
        "Why don't skeletons fight each other?": " They don't have the guts.",
        "I'm reading a book on anti-gravity.": " It's impossible to put down.",
        "What do you call a fake noodle?": " An impasta",
        "Why did the scarecrow win an award?": " Because he was outstanding in his field.",
        "How do you organize a space party?": " You planet.",
        "I'm on a seafood diet.": " I see food and I eat it.",
        "Why did the bicycle fall over?": " Because it was two-tired.",
        "What do you call a bear with no teeth?": " A gummy bear.",
        "I told my computer I needed a break,": " now it won't stop sending me Kit-Kats.",
        "I'm trying to organize a hide and seek competition,": " but good players are really hard to find.",
        "The best time to buy a clock is right now,": " it's always going back in time.",
        "I used to play piano by ear,": " but now I use my hands like everyone else.",
        "What's orange and sounds like a parrot?": " A carrot.",
        "Did you hear about the kidnapping at the park?": " They woke up, it's fine.",
        "The first time I got a universal remote": ' I thought, "This changes everything."',
        "I'm reading a book about anti-gravity;": " it's impossible to put down",
        "Why did the golfer bring two pairs of pants? ": "In case he got a hole in one.",
        "I'm trying to organize a space-themed party,": " but I can't find the right atmosphere.",
        "I'd tell you a chemistry joke,": " but I know I wouldn't get a reaction.",
        "What do you call a belt made out of watches?": " A waist of time.",
        "Why don't scientists trust atoms?": " Because they make up everything.",
        "Why did the scarecrow win an award?": " Because he was outstanding in his field.",
        "What do you call an alligator detective?": " An investi-gator.",
        "Why did the tomato turn red?": " Because it saw the salad dressing.",
        "What did the janitor say when he jumped out of the closet?": ' "Supplies!"',
        "How does a penguin build its house?": " Igloos it together.",
        "The most corrupt CEOs are those of the pretzel companies.":" They're always so twisted.",
        "An apple a day keeps the doctor away…":"Or at least it does if you throw it hard enough.",
        "I have a stepladder because my real ladder left when I was just a kid.": "",
        "I visited my friend at his new house. He told me to make myself at home.": "So I threw him out. I hate having visitors.",
        "Why did Mozart hate all of his chickens?": "When he asked them who the best composer was, they all replied, “Bach, Bach, Bach.”",
        "The other day, my wife asked me to pass her lipstick, but I accidentally passed her a glue stick.": "She still isn't talking to me",
        "Patient: Oh doctor, I'm just so nervous. This is my first operation.": "Doctor: Don't worry. Mine too.",
        "I just got my doctor's test results and I'm really upset.":" Turns out, I'm not gonna be a doctor.",
        "Never break someone's heart. They only have one": "Break their bones instead. They have 206 of them.",
        "The guy who stole my diary just died.": " My thoughts are with his family.",
        "What's worse than biting into an apple and discovering a worm?":" Biting into an apple and discovering half a worm.",
        "As I get older, I remember all the people I lost along the way.": "Maybe a career as a tour guide was not the right choice.",
        "You're not completely useless.":"You can always serve as a bad example.",
        "My wife left a note on the fridge that said, “This isn't working.”.":"I'm not sure what she's talking about. I opened the fridge door and it's working fine!",
        "What's the last thing to go through a fly's head as it hits the windshield of a car going 70 miles per hour?": " Its butt.",
        "My boss told me to have a good day.":" So I went home.",
        "A child determined to burn his home down. His dad watched, tears in his eyes.":" He put his arm across the mother and stated, “That's arson.”",
        "Imagine when you walked into a bar and there was a lengthy line of individuals ready to take a swing at you.":" That's the punch line.",
        "Why are friends a lot like snow?": "If you pee on them, they disappear.",
        "When I see the names of lovers engraved on a tree, I don't find it cute or romantic.":"I find it weird how many people take knives with them on dates.",
        "Why don't skeletons ever go trick or treating?": "Because they have no body to go with.",
        "My boss said to me, “You're the worst train driver ever. How many have you derailed this year?”":"I said, “I'm not sure; it's hard to keep track.”",
        "My wife and I have reached the difficult decision that we do not want children.":" If anybody does, please just send me your contact details and we can drop them off tomorrow.",
        "My parents raised me as an only child, which really pissed off my sister.":"",
        "What rhymes with “boo” and stinks?":" You",
        "“I work with animals,” the man says to his date. “That's so sweet,” she replies. “I love a man who cares about animals. Where do you work?”":" I'm a butcher, he says",
        "Watching my daughter at the park earlier. Another parent asked, “Which one is yours?” I replied, “I'm still deciding.”":"They looked horrified.",
        "My mother said one man's trash is another man's treasure.":" Turns out I'm adopted.",
        "When my uncle Frank died, he needed his ashes to be buried in his favorite beer mug.": "His final wish was to be Frank in Stein.",
        "Why do vampires seem sick?": "They're always coffin.",
        "Today I made a decision to go go to my childhood house. I asked the residents if I may come inside because I was feeling nostalgic, however, they refused and slammed the door on my face.": " My mother and father are the worst.",
        "What did one wall say to the other wall?": ' "I\'ll meet you at the corner."',
        "I'm reading a book on the history of glue.": " I just can't seem to put it down.",
        "What do you get when you cross a snowman and a vampire?": " Frostbite.",
        "Why did the bicycle fall over?": " Because it was two-tired.",
        "Why was the math book sad?": " It had too many problems.",
        "Parallel lines have so much in common.": " It's a shame they'll never meet.",
        "I used to play piano by ear,": " but now I use my hands.",
        "I told my wife she was drawing her eyebrows too high.": " She looked surprised.",
        "I'm friends with 25 letters of the alphabet.": " I don't know why.",
        "How do you make a tissue dance?": " Put a little boogie in it.",
        "What do you call a factory that makes good products?": " A satisfactory.",
        "I'm trying to lose weight, but it keeps finding me.": "",
        "What did one hat say to the other?": ' "You stay here, I\'ll go on ahead."',
        "Why did the coffee file a police report?": " It got mugged.",
        "What do you call a bear in the rain?": " A drizzly bear.",
        "What did the grape do when it got stepped on?": " It let out a little wine.",
        "I used to be a baker,": " but I couldn't make enough dough.",
        "What did one snowman say to the other?": ' "Do you smell carrots?"',
        "I'm terrified of elevators,": " so I'm taking steps to avoid them.",
        "I'm trying to organize a hide and seek competition,": " but good players are really hard to find.",
        "What do you call an alligator detective?": " An investi-gator.",
        "Why did the bicycle fall over?": " It was two-tired.",
        "What do you call a pile of cats?": " A meowtain.",
        "I'm reading a book on the history of glue.": " I just can't seem to put it down.",
        "Why did the coffee file a police report?": " It got mugged.",
        "What's the best thing about Switzerland?": "I don't know, but the flag is a big plus.",
        "I invented a new word;": " Plagiarism!",
    }
    random_joke_index = random.randint(0, len(jokes) - 1)
    first_line_of_random_joke = list(jokes.keys())[random_joke_index]
    second_line_of_random_joke = jokes[first_line_of_random_joke]
    return [first_line_of_random_joke, second_line_of_random_joke]

barrier = threading.Barrier(2)
event = threading.Event()
def say_and_write_joke(first_line: str, second_line: str, event: threading.Event):
    t1 = threading.Thread(target=say_jokes, args=(first_line,))
    t2 = threading.Thread(target=write_with_animation, args=(first_line, 0.05))
    t1.start()
    start_t1 = time.perf_counter()
    t2.start()
    start_t2 = time.perf_counter()
    # event.wait() 
    # time.sleep(1)
    t1.join()
    end_t1 = time.perf_counter()
    time.sleep(end_t1 - start_t2)
    t2.join()
    end_t2 = time.perf_counter()
    time.sleep(end_t2 - start_t2)
    t1.join()
    t2.join()
    t1 = threading.Thread(target=say_jokes, args=(second_line,))
    t2 = threading.Thread(target=write_with_animation, args=(second_line, 0.05))
    # event.wait()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
event.set()

def make_a_joke(event):
    joke = joke_selector()
    say_and_write_joke(joke[0], joke[1], event)

if __name__ == '__main__':
    make_a_joke(event)
    
# HAS A THREAD ISSUE!!!

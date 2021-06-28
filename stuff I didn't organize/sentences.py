import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter 
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns =["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 0:
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 1 and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 1 and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 2:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity, random=False):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.

    FOR EXTRA WORK - added a random paramenter set to false so it doesn't screw with any of the
    old code but I can set it to true and don't have to get a whole new program for adding an ajective. 
    I should've done this with the adverbs and verbs but o well.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()

    if random == False:
        prepositional_phrase = f'{preposition} {determiner} {noun}'
    if random:
        prepositional_phrase = f'{preposition} {determiner} {adjective} {noun}'
    return prepositional_phrase

def get_proper_noun():
    proper_nouns = ['Spencer Damiano', 'Walt Disney', 'Joe Rogan', 'Hilary Clinton', 'Kim Kardashin West', 'President Kayne West', 'Joe Mama', 'Donald Trump', 'Elon Musk', 'President Russel M Nelson', 'Aberham Lincon', 'Joseph Stalin']
    proper_noun = random.choice(proper_nouns)
    return proper_noun

def get_adverb():
    adverbs = ['quickly', 'loudly', 'passively', 'unapologetically', 'unfairly', 'understandably', 'suprisingly', 'uncharacteristically', 'stupidly']
    adverb = random.choice(adverbs)
    return adverb

def get_adjective():
    adjectives = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fat', 'skinny', 'tall', 'short', 'pretty', 'handsome', 'ugly', 'religous', 'hairy', 'hairless', 'rightous', 'wicked']
    adjective = random.choice(adjectives)
    return adjective

def do_homework():
    """
    this function runs the requirements for the prove assignment
    """
    noun_quantity = 1
    verb_tense = 0

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')


    noun_quantity = 0
    verb_tense = 0

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')
    
    
    noun_quantity = 1
    verb_tense = 1

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')
    
    
    
    noun_quantity = 0
    verb_tense = 1

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')
    
    
    noun_quantity = 1
    verb_tense = 2

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')
    
    
    noun_quantity = 0
    verb_tense = 2

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    print(f'{determiner} {noun} {verb}.')

    print()
    print('now with prepositional phrases')
    print()

    noun_quantity = 1
    verb_tense = 0

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

    noun_quantity = 0
    verb_tense = 0

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

    noun_quantity = 1
    verb_tense = 1

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

    noun_quantity = 0
    verb_tense = 1

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

    noun_quantity = 1
    verb_tense = 2

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

    noun_quantity = 0
    verb_tense = 2

    determiner = get_determiner(noun_quantity)
    noun = get_noun(noun_quantity)
    verb = get_verb(noun_quantity, verb_tense)
    prepositional_phrase = get_prepositional_phrase(noun_quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.')

def main():
    """
    single = 1
    plural = 0
    past = 0
    present = 1
    future = 2
    """
    print('hello and welcome to senteneces.py')


    # the do homework function runs the required code for the prove asignment
    homework_or_play = input('do you want to do homeowrk or madlib? h/m? ')

    if homework_or_play == 'h':
        print('lame')
        do_homework()
    elif homework_or_play == 'm':
        print('that\'s what\s up')
        run_madlib()
    elif homework_or_play == 'easter egg':
        run_random_homework()



def run_madlib():
    """
    I think this solves everything base on no good information
    """
    print('INSTRUCTIONS - you can pick v for verbs, n for nouns, pn for proper noun, av for adverbs, and aj for ajectives, or q to quit')
    print()
    print('when you have filled out your madlib read it back to me. our yourself. honestly if you are doing a madlib by yourself that is knida a low point')

    response = None
    fail_safe = 0
    quantities = [0 , 1]
    tenses = [0, 1, 2]

    while response != 'q' or fail_safe >= 1000:
        response = input('what word do you need next? v, n, pn, av, aj, or q to quit - ')
        if response == 'v':
            quantity = random.choice(quantities)
            tense = random.choice(tenses)
            verb = get_verb(quantity, tense)
            print(f'your verb is: {verb}')
        elif response == 'n':
            quantity = input('plural or singular, or does not matter? p/s/n')
            if quantity == 'n':
                quantity = random.choice(quantities)
            elif quantity == 'p':
                quantity = 0
            elif quantity == 's':
                quantity = 1
            else:
                quantity = random.choice(quantities)
            noun = get_noun(quantity)
            print(f'your noun is: {noun}')
        elif response == 'pn':
            pronoun = get_proper_noun()
            print(f'your pro-noun is: {pronoun}')
        elif response == 'av':
            adverb = get_adverb()
            print(f'your adverb is {adverb}')
        elif response == 'aj':
            adjective = get_adjective()
            print(f'your adjuctive is: {adjective}')
        elif response == 'q':
            print('thanks for playing')
        else:
            print('whopse that was not a valid reponse. \n')
            print('you can pick v for verbs, n for nouns, pn for proper nouns, av for adverbs, and aj for ajectives, or q to quit')
            fail_safe += 1
        


def run_random_homework():
    """
    This randomizes 12 phrases that the computer can return, hopefully to better pass the Turning Test
    """

    randomness = []

    for _ in range(33):
        random_choice = random.choice(range(100))
        randomness.append(random_choice)
    
    print(randomness)

    for _ in range(12):
        quantities = [0, 1]
        tenses = [0, 1, 2]
        quantity = random.choice(quantities)
        tense = random.choice(tenses)
        random_choice = random.choice(range(100))
        if random_choice not in randomness:
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner} {noun} {verb}.')
        elif random_choice in randomness:
            verb_quantity = 1
            noun = get_proper_noun()
            adverb = get_adverb()
            verb = get_verb(verb_quantity, tense)
            prepositional_phrase = get_prepositional_phrase(quantity, random=True)
            print(f'{noun} {adverb} {verb} {prepositional_phrase}.')

main()
    

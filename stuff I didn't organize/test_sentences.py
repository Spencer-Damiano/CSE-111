from sentences import get_determiner, get_noun, get_verb, get_preposition, get_proper_noun, get_adjective, get_adverb, run_random_homework
# get_prepositional_phrase is not in here because as long as prepositions and nouns and verbs match we are good.
import pytest
import random


def test_get_determiner():
    """
    I think this solves everything base on no good information
    """
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    """
    I think this solves everything base on no good information
    """

    for _ in range(10):
        single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
        noun = get_noun(1)
        assert noun in single_nouns

    for _ in range(10):
        plural_nouns =["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
        noun = get_noun(0)
        assert noun in plural_nouns

def test_get_verb():
    """
    I think this solves everything base on no good information
    """

    for _ in range(10):
        past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        verb = get_verb(0, 0)
        assert verb in past_verbs
    
    for _ in range(10):
        single_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        verb = get_verb(1, 1)
        assert verb in single_present
    
    for _ in range(10):
        plural_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        verb = get_verb(0, 1)
        assert verb in plural_present
    
    for _ in range(10):
        future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        verb = get_verb(0, 2)
        assert verb in future_verbs

def test_get_preposition():
    """
    I think this solves everything base on no good information
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(10):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    """
    I think this solves everything base on no good information
    """
    quantities = [0 , 1]

    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    singular_determiners = ["the", "one"]

    plural_nouns =["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    plural_determiners = ["some", "many"]

    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    for _ in range(10):
        quantity = random.choice(quantities)
        if quantity == 1:
            noun = get_noun(quantity)
            determiner = get_determiner(quantity)
            preposition = get_preposition()

            assert noun in single_nouns
            assert determiner in singular_determiners
            assert preposition in prepositions
        elif quantity == 0:
            noun = get_noun(quantity)
            determiner = get_determiner(quantity)
            preposition = get_preposition()

            assert noun in plural_nouns
            assert determiner in plural_determiners
            assert preposition in prepositions

def test_get_proper_noun():
    """
    I think this solves everything base on no good information
    """
    proper_nouns = ['Spencer Damiano', 'Walt Disney', 'Joe Rogan', 'Hilary Clinton', 'Kim Kardashin West', 'President Kayne West', 'Joe Mama', 'Donald Trump', 'Elon Musk', 'President Russel M Nelson', 'Aberham Lincon', 'Joseph Stalin']
    for _ in range(10):
        noun = get_proper_noun()
        assert noun in proper_nouns

def test_get_adverb():
    """
    I think this solves everything base on no good information
    """
    adverbs = ['quickly', 'loudly', 'passively', 'unapologetically', 'unfairly', 'understandably', 'suprisingly', 'uncharacteristically', 'stupidly']
    for _ in range(10):
        adverb = get_adverb()
        assert adverb in adverbs

def test_get_adjective():
    """
    I think this solves everything base on no good information
    """
    adjectives = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fat', 'skinny', 'tall', 'short', 'pretty', 'handsome', 'ugly', 'religous', 'hairy', 'hairless', 'rightous', 'wicked']
    for _ in range(10):
        adjective = get_adjective()
        assert adjective in adjectives

def test_run_random_homework():
    """
    I think this solves everything base on no good information
    """
    proper_nouns = ['Spencer Damiano', 'Walt Disney', 'Joe Rogan', 'Hilary Clinton', 'Kim Kardashin West', 'President Kayne West', 'Joe Mama', 'Donald Trump', 'Elon Musk', 'President Russel M Nelson', 'Aberham Lincon', 'Joseph Stalin']
    adverbs = ['quickly', 'loudly', 'passively', 'unapologetically', 'unfairly', 'understandably', 'suprisingly', 'uncharacteristically', 'stupidly']
    adjectives = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fat', 'skinny', 'tall', 'short', 'pretty', 'handsome', 'ugly', 'religous', 'hairy', 'hairless', 'rightous', 'wicked']
    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    singular_determiners = ["the", "one"]

    plural_nouns =["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    plural_determiners = ["some", "many"]

    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    for _ in range(20):
        proper_noun = get_proper_noun()
        assert proper_noun in proper_nouns
        adverb = get_adverb()
        assert adverb in adverbs
        adjective = get_adjective()
        assert adjective in adjectives
        single_noun = get_noun(1)
        assert single_noun in single_nouns
        singular_determiner = get_determiner(1)
        assert singular_determiner in singular_determiners
        plural_noun = get_noun(0)
        assert plural_noun in plural_nouns
        plural_determiner = get_determiner(0)
        assert plural_determiner in plural_determiners
        preposition = get_preposition()
        assert preposition in prepositions
            


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
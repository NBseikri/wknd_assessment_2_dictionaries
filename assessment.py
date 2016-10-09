"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count_dict = {}
    # Empty dictionary for words as keys and frequency as values
    words = phrase.split()
    # Splits the inputted string into individual words in a list
    for word in words:
    # Evaluates each word in the phrase
        word_count_dict[word] = word_count_dict.get(word,0)+1
        # Sets or adds 1 to the value of word as a key for depending on whether 
        # the key already appears in the dictionary

    return word_count_dict

def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_dict = {'Watermelon' : 2.95, 'Cantaloupe' : 2.50, 'Musk' : 3.25, 'Christmas' : 14.25}
    # Creates dictionary melons as keys and values as melon prices

    return melon_dict.get(melon_name, 'No price found')
    # Returns the value for passed-in melon_name using .get; otherwise returns
    # 'No price found'

def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    ####################################################################
    # I made it part way through this function. My attempt is below:
    ####################################################################

    # word_lengths = {}
    # # Empty dictionary to hold counts of words

    # for word in words:
    # # Evaluates each word in inputted words
    #     word_lengths[word] = word_lengths.get(word,0)+1
    #     # Sets each dictionary entry as the word as the key and count as the 
    #     # value

    # word_lengths_list = []
    # # Empty list to hold tuples of a count value followed by a list of all the 
    # # keys that appear the number of times of the count in the tuple
 
    # for key, value in word_lengths.iteritems():
    # # Evaluates each key and value in the dictionary
    #     pair = (value, [key])
    #     # Sets pair as a tuple with the value at index 0 of the tuple and the 
    #     # corresponding keys within a list at index 1 of the tuple
    #     if pair[0] not in word_lengths_list:
    #     # Evaluates whether the value of at index 0 of the pair tuple is not
    #     # already represented in the list
    #         word_lengths_list.append(pair)
    #         # If pair[0] is not represented in the list, it appends the whole 
    #         # list
    #     else:
        ####################################################################
        # Where I was unable to complete the function: 
        ####################################################################
        # Else handles when pair[0] is in the list as the first number in a
        # tuple before its adjoining list of words. I'm unsure how to access
        # an existing tuple in the list that matches pair[0], and append
        # to the list within that tuple. 


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_talk = {}
    # Created empty dictionary for pirate translations of English words

    eng = ['sir', 'hotel', 'student', 'man', 'professor', 'restaurant', 'your', 'excuse', 'students', 'are', 'restroom', 'my', 'is']
    pir = ['matey', 'fleabag inn', 'swabbie', 'matey', 'foul blaggart', 'galley', 'yer', 'arr', 'swabbles', 'be', 'head', 'me', 'be']
    # Created two parallel lists for corresponding pirate and English words
    pirate_talk = dict(zip(eng, pir))
    # Merged to the two lists into a single dictionary where the eng words are 
    # keys and the pir words are values
    
    words = phrase.split()
    # Split the inputted string into separate words
    translated_input = ''
    # Created an empty string to be developed by the code below

    for word in words:
    # Evaluates each word in the inputted phrase
        if word in pirate_talk:
        # Handles words in the dictionary
            translation = pirate_talk.get(word)
            # Sets translation as the value of the inputted word    
            translated_input = translated_input + translation + " "
            # Concatenates that value to translated_input along with a space
        else:
        # Handles words that are not in the dictionary
            translated_input = translated_input + word + " "
            # Concatenates the word as it is passed through

    return translated_input.rstrip()
    # Returns the final translated string with trailing space removed

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    ################################################################
    # I made it part way through this function. My attempt is below:
    ################################################################

    kids_dict = {}
    # Creates an empty dictionary for first letters of words in the inputted
    # list (the keys) and the corresponding words that share that first letter
    # (the values).

    for word in names:
    # Evaluates each item in the names list
        kids_dict.setdefault(word[0],[]).append(word)
        # Sets each instance of a first letter as a key and organizes
        # all words that share that letter as a list of values

    result_list = [names[0]]
    # Initializes the game result as the first word from the inputted list

    for key, value in kids_dict.iteritems():
    # Evaluates each key and value in the dictionary
        if len(value) > 1:
        # Evaluates values with more than one word in the value list
            for i in value:
            # Evaluates each word in the value list
                if i in result_list:
                # Handles a word that is already in results_list
                    pass
                    # Does nothing as we don't want duplicates
                else:
                # Handles a word that is not already in results_list
                    if i[0] == result_list[-1][-1]:
                        # Checks if the first letter of the word in the value 
                        # list matches the last letter of the result_list
                        result_list.append(i)
                        # Appends the whole word to result_list if the first 
                        # letter matches
        else:
        # Handles a value with only one word in its list
            if value[0] == result_list[-1][-1]:
            # Checks if the first letter of the word in the value 
            # list matches the last letter of the result_list
                result_list.append(value)
                # Appends the whole word to result_list if the first 
                # letter matches

    return result_list
    ####################################################################
    # Where I was unable to complete the function: 
    ####################################################################
    # This function seems to stop evaluating and appending after the
    # result_list contains ['bagon', 'nosepass']. I am having trouble making
    # the function use the same steps in a subsequent iteration to identify
    # 's': ['starly'] from the dictionary and to append as described. 

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

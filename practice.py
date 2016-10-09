"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    dupe_dict = {}
    # Empty dictionary with list words as keys and number of occurences
    # as values 

    for word in words:
    # Evaluates each word in words list
        if word not in dupe_dict:
        # Handles words that are not already in dupe_dict
            dupe_dict[word] = 0
            # Adds key to dupe_dict and initializes value at zero

        dupe_dict[word] = dupe_dict[word] + 1
        # Adds 1 to the value of a key for each time the key appears in 
        # the list

    dupe_keys = dupe_dict.keys()
    # Assigns a list of just the dictionary keys (a.k.a. the unique words
    # from the inputted list) to a new variable, dupe_keys

    return dupe_keys
    # Returns dupe_keys

    #####################################################################
    # A more concise alternative:
    #
    #   for word in words:
    #       dupe_dict[word] = dupe_dict.get(word, 0) + 1

def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    common_items = []
    # Created empty list for unique, common items

    for item in items1:
    # Evaluates numbers in the items1 list
        for diff_item in items2:
        # Evaluates numbers in the items2 list
            if item == diff_item:
            # Handles when numbers from the two lists are the same
                if item not in common_items:
                # Handles when the common number is not already in the 
                # common_items list,
                    common_items.append(item)
                    # Appends the common number to the common_items list

    return common_items
    # Returns the populated common_items list

    ###################################################################
    # I completed the function two different ways. The first way which I 
    # used below to pass the doctest, did not use a dictionary. Further, I 
    # used an "if __ not in ___" statement despite the instructions. I was 
    # unsure how to control for dupes without using "if __ not in ___".
    # 
    # For the other approach, I used a built-in method that also did not utilize 
    # dictionaries (rather it finds the intersections/unique common numbers 
    # in two lists):
    # 
    #       return list(set(items1).intersection(items2))
    #################################################################### 

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    import itertools
    # Imported itertools. Alternatively, could have used "from intertools 
    # import permutations" and omitted "intertools." below.

    no_dupe_numbers = []
    # Created empty list for deduplicated version of the passed numbers list
    for number in numbers:
    # Evaluates each number in the passed numbers
        if number not in no_dupe_numbers:
        # Handles a number not in the no_dupe_numbers list
            no_dupe_numbers.append(number)
            # Appends a number not already in no_dupe_numbers

    sum_dict = {}
    # Created empty dictionary for creating dictionary to hold
    # zero-sum pairs

    for i in range(len(no_dupe_numbers)+1):
    # Evaluates each item in the no_dupe_numbers with a wide enough range
    # to capture the number following i below 
        for subset in itertools.permutations(no_dupe_numbers, i):
        # Generates all combinations of all numbers in the no_dupe_numbers list
            if len(subset) == 2:
            # Handles only two-number combinations and excludes all other 
            # combinations (i.e. ignores three-number combinations, etc.)
                list(subset)
                # Makes the subset a list
                if subset[0] + subset[1] == 0:
                # Handles a scenario where the pair in a subset equals zero
                    sum_dict[subset[0]] = subset[1]
                    # Adds the pair to the dictionary

    zero_sum = []
    # Creates empty list to hold list of zero-sum pairs

    for key, value in sum_dict.iteritems():
    # Evaluates each key and value in the dictionary
        pair = [key, value]
        # Sets pair as a list with key, value as items
        opp_pair = [value, key]
        # Sets opp_pair variable to capture the reverse of a zero-sum
        # pair to address duplicates (i.e. [1, -1] is the pair and [-1, 1]
        # is the opp_pair)
        if opp_pair not in zero_sum:
        # Handles if the opp_pair is not already in the zero_sum list
            zero_sum.append(pair)
            # When the opposite pair is not already in the list, it appends
            # the pair to the list

    if 0 in no_dupe_numbers:
    # Handles a 0 in the no_dupe_numbers
        zero_sum.append([0,0])
        # Appends [0,0] to the zero_sum list so that 0 is represented as being
        # added to itself

    return zero_sum
    # Returns the populated zero_sum list 

def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    import operator 
    # Imported operator to use .itemgetter below
    # I could have also entered "from operator import itemgetter" and 
    # referred to it as just itemgetter below

    char_dict = {}
    # Created empty dictionary to be populated by characers (keys) and
    # their frequencies (values)

    phrase = phrase.replace(" ", "")
    # Removed spaces between words in the input string

    for word in phrase:
    # Evaluates each word in the input string
        char_dict[word] = char_dict.get(word, 0) + 1
        # Adds 1 to the value of a character key for each time that key appears
        # in the input string
    
    top_chars = max(char_dict, key=char_dict.get)
    # Set top_chars as the most frequently ocurring key by identifying the 
    # highest value in char_dict
    top_chars = (top_chars, char_dict[top_chars])
    # Resets top_chars to now also include the value for the most frequently 
    # occuring key as a pair. This does not captured tied keys with the same
    # variable. 
    tied_top_chars = []
    # Created an empty list to capture characters with tied values

    for key, value in char_dict.iteritems():
    # Evaluates key and value in each dictionary entry
        if value == top_chars[1]:
        # Handles the value of a dictionary key that matches top_chars[1].
        # top_chars represents the value for the most frequently occurring key 
        # without regard to any ties)
            tied_top_chars.append(key)
            # Appends a tied key to tied_top_chars


    if len(tied_top_chars) > len([top_chars]):
    # top_chars will never include any ties; it will necesarily only have one character.
    # tied_top_chars will necessarily include at least two characters
    # If len(tied_top_chars) > len([top_chars]), then we know there were ties
    # and we need to print the list of ties. Else, we just need the single 
    # character that occurs most frequently in top_chars
        return sorted(tied_top_chars)
        #Sorts and returns tied_top_chars
    else:
        return [top_chars[0]]
        # Returns just the most frequently ocurring character without its
        # frequency from the pair in top_chars

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

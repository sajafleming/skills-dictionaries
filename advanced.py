"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


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
    letter_counts = {}

    for letter in phrase:
        if letter == " ":
            continue
        else:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # set highest equal to the max value        
    highest = max(letter_counts.values()) 

    # use dicionary comprehension to return all keys with highest value
    return [i for i, v in letter_counts.items() if v == highest]



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
    word_dict = {}
    
    for word in words:
        letter_count = len(word)

        if letter_count in word_dict:
            word_dict[letter_count].append(word)
            word_dict[letter_count].sort()
        else:
            word_dict[letter_count] = [word]
        

    return word_dict.items()

    # same as sort_by_word_length in skills.py, only difference is that 
    # this one wanted the list of words per length sorted in alphabetical 
    # order so I added a sort to the list every time a word is added


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

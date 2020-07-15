def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #Base case
    if len(sequence) == 1:
        return [sequence]
    
    #Run the recursion
    firstchar = sequence[0]
    runninglist = []
    for sublist in get_permutations(sequence[1:]):
        wordlist = list(sublist)
        for i in range(len(wordlist)+1):
            newwordlist = wordlist.copy()
            newwordlist.insert(i, firstchar)
            newword = "".join(newwordlist)
            runninglist.append(newword)        
    return runninglist

    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ice'
    print('Input:', example_input)
    print('Expected Output:', ['ice', 'cie', 'cei', 'iec', 'eic', 'eci'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'top'
    print('Input:', example_input)
    print('Expected Output:', ['top', 'tpo', 'otp', 'pot', 'pto', 'opt'])
    print('Actual Output:', get_permutations(example_input))
    

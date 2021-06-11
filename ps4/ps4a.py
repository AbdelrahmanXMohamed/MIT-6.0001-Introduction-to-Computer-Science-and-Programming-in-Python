# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
from itertools import permutations
'''
queue=[]
l=[]
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
'''
queue=[]
n=-1
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
    global n
    n=max(n,len(sequence))
    if len(sequence)==2:
        if len(queue)== 0:
            queue.append(sequence)
            queue.append(sequence[::-1])
        else:
            q=queue[:]
            queue.clear()
            queue.append(sequence)
            queue.append(sequence[::-1])
            queue.extend(q)
        return
    for i in range(len(sequence)):
        get_permutations(sequence[:i]+sequence[i+1:])
        queue.sort(key=len)
        while len(sequence)>len(queue[0]):
            temp=''+sequence[i]+queue.pop(0)
            if temp not in queue:
                queue.append(temp)
    if len(sequence)==n:
        q=queue[:]
        queue.clear()
        n=-1
        return q
    return queue
if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

   # pass #delete this line and replace with your code here
example_input = 'nna'
print('Input:', example_input)
print('Expected Output:', ['nna', 'nan', 'ann'])
print('Actual Output:', get_permutations(example_input))
print()
    
example_input = 'aaa'
print('Input:', example_input)
print('Expected Output:', ['aaa'])
print('Actual Output:', get_permutations(example_input))
print()    
example_input = 'hat'
print('Input:', example_input)
print('Expected Output:', ['hat', 'aht', 'ath', 'hta', 'tha', 'tah'])
print('Actual Output:', get_permutations(example_input))
print()
# Author: Sylvia Young
# Date Created: January 17, 2023
# Date Modified: January 19, 2023
# Purpose: To tokenize a text file, calculate token frequencies within the text file, and print out the tokens and their frequencies.


import re
import sys


# tokenize function runs in O(n) time. 
# The re.split function runs in O(n) time and the loop runs in O(n) time. 
def tokenize(file): 
    
    tokens = []
    tokens = re.split('[^A-Za-z0-9]+', file)
    
    # Convert all alphabetic characters to lowercase for easier comparison.
    # Keep single character tokens as is.
    n = 0
    while n < len(tokens):
        tokens[n] = tokens[n].lower()
        if tokens[n] == '':
            tokens.remove(tokens[n])
        else:
            n += 1  
    
    return tokens
        
    
# calculate_word_frequencies function runs in O(n).
def calculate_word_frequencies(tokens):
    
    token_frequencies = {}
        
    # Add tokens to dictionary if it is first occurrence.
    # Otherwise, increment the frequency of that token.
    for token in tokens: 
        token_frequencies[token] = token_frequencies.get(token, 0) + 1
                    
    return token_frequencies


# print_frequencies function runs in O(nlogn).
# sorted function runs in O(nlogn) and loop runs in O(n).
def print_frequencies(token_frequencies):
    
    sorted_frequencies = {}
    
    # Sort tokens in descending order by frequency and tokens with the same frequency in alphabetical order.
    sorted_frequencies = sorted(token_frequencies.items(), key=lambda x: (-x[1], x[0]))
    
    for token in sorted_frequencies:
        print(token[0], "-", token[1])


if __name__ == "__main__":
    
    # Check for valid number of files.
    if (len(sys.argv) > 2) or (len(sys.argv) < 2):
        sys.exit("Invalid number of arguments.")
        
    try:
        with open(sys.argv[1], "r") as file:
            file = file.read()
        
        tokens = tokenize(file)
        token_frequencies = calculate_word_frequencies(tokens)
        print_frequencies(token_frequencies)
    except:
        print("Invalid file.")

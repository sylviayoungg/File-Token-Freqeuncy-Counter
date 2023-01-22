# Author: Sylvia Young
# Date Created: January 19, 2023
# Date Modified: January 19, 2023
# Purpose: To tokenize two text files, calculate token frequencies, and print out common tokens and their frequencies between the two files.


import sys
import Assignment1A as A


# print_common_frequencies function runs in O(n) time.
# The loop runs in O(n) time.
def print_common_frequencies(token_frequencies_1, token_frequencies_2):
    
    set_1 = set(token_frequencies_1)
    set_2 = set(token_frequencies_2)
    
    count = 0
    
    # Find common tokens and increment counter of common tokens.
    for token in set_1.intersection(set_2):
        print(token)
        count += 1
        
    print(count)


if __name__ == "__main__":
    
    # Check for valid number of files.
    if (len(sys.argv) > 3) or (len(sys.argv) < 3):
        sys.exit("Invalid number of arguments.")
        
    try:
        with open(sys.argv[1], "r") as file1:
            file1 = file1.read()
            
        with open(sys.argv[2], "r") as file2:
            file2 = file2.read()
        
        tokens1 = A.tokenize(file1)
        tokens2 = A.tokenize(file2)
        token_frequencies_1 = A.calculate_word_frequencies(tokens1)
        token_frequencies_2 = A.calculate_word_frequencies(tokens2)
        print_common_frequencies(token_frequencies_1, token_frequencies_2)
    except:
        print("Invalid file(s).")

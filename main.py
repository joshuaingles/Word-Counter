import sys
import os
from file_parser import file_parser
from word_counter import word_counter
import string

def main():
    args = sys.argv
    argsLen = len(args)
    outputType = "-l"

    # Command line argument parsing and validation
    # Check for minimum required number of arguments
    if argsLen == 1:
        print("ERROR : Insufficient Arguments : Please provide a File Name")
        sys.exit(1)
    # Case - One argument , Check for proper filename format
    elif argsLen == 2:
        fileName = args[1]
        if not fileName.endswith(".txt"):
            print("ERROR : Argument Format : File Name must end in .txt")
            sys.exit(2)
    # Case - Two Arguments , Check for proper filename and output type format
    elif argsLen == 3:
        fileName = args[1]
        if not fileName.endswith(".txt"):
            print("ERROR : Argument Format : File Name must end in .txt")
            sys.exit(2)
        outputType = args[2]
        if not outputType.startswith('-') and (outputType.endswith('j') or outputType.endswith('l')):
            print("ERROR : Argument Format : Output type must being with - and be j or l")
            sys.exit(3)

    # File validation
    if not os.path.exists(fileName):
        print("ERROR : File Not Found : Ensure txt is in same Directory as main.py")
        sys.exit(4)

    # Extraction of tokens from file
    fileParser = file_parser(fileName)
    tokens = fileParser.parseTokens()

    # Counting and sorting of word occurrence
    wordCounter = word_counter(tokens)
    count = wordCounter.getCount()
    sortedKeys = wordCounter.sortCount(count)

    # Output of results
    # Uses value of 1,000 to output "most common" word occurrences for list output type
    if outputType == "-l":
        for key in sortedKeys:
            if count[key] >= 1000:
                print(key + " - " + str(count[key]))
    # JSON ouput type returns dictionary of words with counts in decreasing order
    elif outputType == "-j":
        jsonOutput = {}
        for key in sortedKeys:
            jsonOutput[key] = count[key]
        print(jsonOutput)

if __name__ == "__main__":
    main()

#encoding=utf8
import string

# file_parser
# Takes in a .txt file then extracts / normalizes tokens
class file_parser:
    def __init__(self, fileName):
        self.fileName = fileName
        self.punc = string.punctuation + '‘' + '’' + '“' + '”' + '!' + '?' + '—' + '.' + ';' + '_'

    # Tokenizes text and performs normalization
    # Returns List of Tokens (str)
    def parseTokens(self):
        # Extraction and normalization of lines from text
        # Punctuation is removed and replaced with white space
        with open(self.fileName, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        parsedLines = []
        for line in lines:
            for char in self.punc:
                if char in line:
                    line = line.replace(char, ' ')
            parsedLines.append(line)

        # Lines are Tokenized and Tokens normalized
        # Tokens are first checked for digits or if they are white space
        # If Tokens pass check, they are stripped of punctuation, white space, and lowercased
        tokens = []
        for line in parsedLines:
            for token in line.split():
                if (not self.containsNum(token)) and (token != " ") and (token != ''):
                    for char in self.punc:
                        if char in token:
                            token = token.replace(char, ' ')
                    token = token.replace(' ', '')
                    token = token.lower()
                    if not len(token) < 1:
                        tokens.append(token)
        return tokens

    # Simple function to check for the presence of digits in Token
    # Returns Bool
    def containsNum(self, token):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in nums:
            if str(num) in token:
                return True
        return False

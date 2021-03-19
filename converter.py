import base64
import requests
import sys
import re

def converter(content, string):

    stringBase = string

    space = string.find(' ')

    if(space != -1):
        stringParts = string.split()
        string = stringParts[0]

    stringLength = len(string)
    encodedContent = content
    byteDecodedContent = base64.standard_b64decode(encodedContent)
    stringDecodedContent = byteDecodedContent.decode("UTF-8")

    #lowerDecoded = stringDecodedContent.lower()

    lines = stringDecodedContent.split('\n')

#    linesQtt = len(lines)

    codePosition = stringDecodedContent.find(string)

    if(codePosition):
        codeLine = [i for i, s in enumerate(lines) if string in s]
        if(codeLine):
            print('Number of ocurrences: ', len(codeLine))
            line = int(codeLine[0]) + 1
            print('First occurrence line: ', line)
        else:
            stringParts = stringBase.split(' ')
            componentsQt = len(stringParts)
            if(componentsQt > 1):
                string = stringParts[1]
                stringLength = len(string)
                codeLine = [i for i, s in enumerate(lines) if string in s]
            if(codeLine):
                print('Number of ocurrences: ', len(codeLine))
                line = int(codeLine[0]) + 1
                print('First occurrence line: ', line)
            else:
                return False
            
    stringEnd = (codePosition+stringLength-1)

    def secondBreakLineBefore(text):
        if(codeLine[0] > 2):
            linesStart = text.rfind('\n', 0, stringDecodedContent.rfind('\n', 0, codePosition)-1)
            return linesStart
        elif(codeLine[0] == 0):
            linesStart = 0
        else:
            linesStart = text.rfind('\n', 0, stringDecodedContent.rfind('\n', 0, codePosition))
            return linesStart

    def secondBreakLineAfter(text):
        if(codeLine[0] > 2):
            linesEnd = text.find('\n', stringDecodedContent.find('\n', stringEnd)+1)
            return linesEnd
        else:
            linesEnd = text.find('\n', stringDecodedContent.find('\n', stringEnd))
            return linesEnd

    startBreak = secondBreakLineBefore(stringDecodedContent)

    endBreak = secondBreakLineAfter(stringDecodedContent)

    codePart = stringDecodedContent[startBreak:endBreak]

    return codePart

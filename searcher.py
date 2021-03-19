#!/usr/bin/env python
import requests
import json
import sys
from time import sleep
#from art import text2art
import urllib.parse as urllib
from pprint import pprint
from converter import converter
from header import printHeader
from colorama import Fore, Back, Style

dorks = open('./small_dorklist.txt').read().splitlines()

printHeader()

def search(user, token, repo):

    for string in dorks:

        if(token):
            if(repo != None):
                parsedResponse = requests.get('https://api.github.com/search/code?q=%s' % urllib.quote(('user:'+user+' '+string+' '+'repo:'+' '+repo)), headers={'Authorization': 'token %s' % token})
            else:
                parsedResponse = requests.get('https://api.github.com/search/code?q=%s' % urllib.quote(('user:'+user+' '+string)), headers={'Authorization': 'token %s' % token})
        else:
            if(repo != None):
                parsedResponse = requests.get('https://api.github.com/search/code?q=%s' % urllib.quote(('user:'+user+' '+string+' '+'repo:'+' '+repo)))
            else:
                parsedResponse = requests.get('https://api.github.com/search/code?q=%s' % urllib.quote(('user:'+user+' '+string)))

        if(parsedResponse.status_code == 200 and len(parsedResponse.json()['items']) != 0):
            response = parsedResponse.json()['items']

            size = len(response)

            for i in range(size):
                class ResponseObj:
                    repository = response[i]['repository']
                    fileName = response[i]['name']
                    repoName = repository['name']
                    path = response[i]['path']
                    fileUrl = response[i]['html_url']
                    repoUrl = repository['url']
                    resultUrl = response[i]['url']

                if(token):               
                    request = requests.get(ResponseObj.resultUrl, headers={'Authorization': 'token %s' % token})
                else:
                    request = requests.get(ResponseObj.resultUrl)

                if(request.status_code == 200):
                    encodedContent = request.json()['content']
                else:
                    print('Nothing found with %s\n' % string)

                if 'filename:' not in string and 'extension:' not in string:

                    print(Fore.CYAN,"\n=================================\n",Style.RESET_ALL)
                    print("Content searched: ", string, "\nRepository: ", ResponseObj.repoName, "\nFile: ", ResponseObj.fileName, "\nUrl: ", ResponseObj.fileUrl, "\nRepo Url: ", ResponseObj.repoUrl,"\n")

                    code = converter(encodedContent, string)
                    if(code == False):
                        code = 'There was an issue searching for the code snippet.'

                    print("\nCode snippet:\n%s" % code)

                else:
                    print(Fore.CYAN,"\n=================================\n",Style.RESET_ALL)
                    print("Content searched: ", string, "\nRepository: ", ResponseObj.repoName, "\nFile: ", ResponseObj.fileName, "\nUrl: ", ResponseObj.fileUrl, "\nRepo Url: ", ResponseObj.repoUrl,"\n")            

        elif(parsedResponse.status_code == 403):
            print(Fore.GREEN+'\nLet\'s respect GitHub API Rate Limit, give me a minute to rest.')
            sleep(60)

        else:
            print(Fore.RED+'\nNothing found with %s' % string)

    print(Fore.CYAN+'\nEverything done!\n')
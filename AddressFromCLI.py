import sys, pyperclip, webbrowser

searchList = sys.argv[1:]

searchWords = ''

for i in searchList:
    searchWords += i
    searchWords += ' '


searchPref = 'https://www.google.com/maps/place/'

webbrowser.open(searchPref+searchWords)






















'''area = pyperclip.paste()

searchWord = searchPref+area

webbrowser.open(searchWord)'''

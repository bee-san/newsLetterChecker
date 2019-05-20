import re
import argparse
import errorChecker
from os import system


# arguments
# takes in -f or --file, as the newsletter .md file
parser = argparse.ArgumentParser(description='Newsletter')
parser.add_argument('-f','--file', help='Newsletter as .md file', required=True)
args = vars(parser.parse_args())

# opens the file and reads it
f = open("{}".format(args['file']), "r")
text = f.read()
f.close()

# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// followed by anything but a closing paren
url_regex = "http[s]?://[^)]+"

# regex to find the links
markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

# once a link is found, append the UTM param to the end
for match in re.findall(markup_regex, text):
    text = text.replace(match[1], match[1]+"?utm_source=technologicallyclairvoyant.com&utm_medium=email&utm_campaign=Technologically_Clairvoyant_newsletter")

# close & save the file
f = open("{}".format(args['file']), "w")
f.write(text)
errorChecker.checkLinks(text)
f.close()

# spell check using asspell
system("aspell {}".format(args['file']))
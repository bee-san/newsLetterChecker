

def checkLinks(text):
    import re
    # Anything that isn't a square closing bracket
    name_regex = "[^]]+"
    # http:// or https:// followed by anything but a closing paren
    url_regex = "http[s]?://[^)]+"

    # regex to find the links
    markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

    # once a link is found, append the UTM param to the end
    links = []
    for match in re.findall(markup_regex, text):
        links.append(match[1])

    import requests
    for link in links:
        r = requests.get(link)
        if r.status_code == 404:
            print("404 error for link " + link)

if __name__ == "__main__":
    import argparse
    # arguments
    # takes in -f or --file, as the newsletter .md file
    parser = argparse.ArgumentParser(description='Newsletter')
    parser.add_argument('-f','--file', help='Newsletter as .md file', required=True)
    args = vars(parser.parse_args())

    # opens the file and reads it
    f = open("{}".format(args['file']), "r")

    file = open("{}".format(args['file'], "r"))
    text = file.read()
    file.close()
    checkLinks(text)

import re
import string

BOB_BRAIN = {
    'question': 'Sure.',
    'yell': 'Whoa, chill out!',
    'question.yell': "Calm down, I know what I'm doing!",
    'silent': 'Fine. Be that way!',
    'else': 'Whatever.',
}


def yelly(phrase):
    ''' Naïve yelling analizer '''
    upcase = len(re.findall(r"[A-Z]", phrase))
    total = len(re.findall(r"[a-zA-Z]", phrase))
    yell_ratio = 0

    if total:
        yell_ratio = upcase / total

    return yell_ratio


def hey(phrase):
    tone = []

    phrase = phrase.strip()

    if phrase == "":
        tone.append('silent')
    else:
        if re.match(r'.*\?$', phrase):
            tone.append('question')

        if yelly(phrase) > .5:
            tone.append('yell')

        if len(tone) == 0:
            tone.append("else")

    query = '.'.join(tone)

    return BOB_BRAIN[query]


def main():

    while True:
        phrase = input("tell bob: ")
        if phrase == "x":
            break
        else:
            print(hey(phrase))


if __name__ == '__main__':
    main()

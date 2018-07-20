import string

BOB_BRAIN = {
    'question': 'Sure.',
    'yell': 'Whoa, chill out!',
    'question.yell': "Calm down, I know what I'm doing!",
    'silent': 'Fine. Be that way!',
    'else': 'Whatever.',
}


def hey(phrase):
    phrase = phrase.strip()  # normalize

    # init
    tone = []

    if phrase == "":
        tone.append('silent')
    else:
        if phrase[-1] == "?":
            tone.append('question')

        if phrase.isupper():
            tone.append('yell')

        if len(tone) == 0:
            tone.append("else")

    query = '.'.join(tone)

    return BOB_BRAIN[query]

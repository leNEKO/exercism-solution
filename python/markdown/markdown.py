import re

# another next step of refactoring would to make it OOP


def parse_head(line):
    # DRYer headers
    m = re.search(r'^(#+)(.*)', line)
    if m:
        size = len(m.group(1))
        text = m.group(2).strip()
        line = f"<h{size}>{text}</h{size}>"
    return line


def parse_text(line):
    # DRYer styles - getting rid of in_bold in_italic
    rules = [
        (r'__(.*)__', r'<strong>\1</strong>'),
        (r'_(.*)_', r'<em>\1</em>'),
        # we could add more rules here ex.:
        (r'```(.*)```', r'<pre><code>\1</pre></code>'),
    ]
    for pattern, repl in rules:
        line = re.sub(pattern, repl, line)
    return line


def parse_li(line):
    return f"<li>{line}</li>"


def parse_paragraph(line):
    if not re.match(r'^<[ulph]', line) and line != "":
        line = f"<p>{line}</p>"
    return line


def parse_markdown(markdown):
    lines = []
    lis = []  # temporary store for lis (getting rid of in_list)

    # a \n added to the markdown to assure list ends
    for line in (markdown + "\n").split("\n"):
        line = parse_head(line)
        line = parse_text(line)

        m = re.search('^\*\s*(.*)', line)
        if m is not None:
            # if is a list element
            lis.append(parse_li(m.group(1)))  # store it
        else:
            # if list ended join element in a ul
            if lis != []:
                lines.append(
                    "<ul>{}</ul>".format(
                        "".join(lis)
                    )
                )
                lis = []
            lines.append(parse_paragraph(line))

    return "".join(lines)

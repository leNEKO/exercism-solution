import re


def parse_head(line):
    # DRYer headers - works with any size
    m = re.search(r'^(#+)(.*)', line)
    if m:
        size = len(m.group(1))
        text = m.group(2).strip()
        line = f"<h{size}>{text}</h{size}>"
    return line


def parse_text(line):
    # DRYer styles - getting rid of in_bold in_italic
    #! the rules order matters
    rules = [
        # bolds
        (r'__(.*)__', r'<strong>\1</strong>'),
        # italics
        (r'_(.*)_', r'<em>\1</em>'),
        # code blockwith syntax highlighting
        (r'```(\w+)\n(.*)\s+```', r'<pre class="language-\1"><code>\2</code></pre>'),
        # code block
        (r'```\n(.*)\s+```', r'<pre class="language-\1"><code>\1</code></pre>'),
        # inline code
        (r'`(.*)`', r'<code>\1</code>'),
    ]
    for pattern, repl in rules:
        line = re.sub(pattern, repl, line, flags=re.S)
    return line


def parse_li(line):
    return f"<li>{line}</li>"


def parse_paragraph(line):
    if not re.match(r'^<[ulph]', line) and line != "":
        line = f"<p>{line}</p>"
    return line


def parse_markdown(markdown):
    lines = []
    list_items = []  # temporary store - instead of in_list boolean

    # an empty line appended to the lines list assuring list ends
    for line in (markdown).split("\n") + [""]:
        line = parse_head(line)
        line = parse_text(line)

        m = re.search('^\*\s*(.*)', line)
        if m:
            # if is a list item, store the line
            list_items.append(parse_li(m.group(1)))
        else:
            # if list ended, join list items in a unordered list
            if list_items:
                lines.append(
                    "<ul>{}</ul>".format(
                        "".join(list_items)
                    )
                )
                list_items = []
            lines.append(parse_paragraph(line))

    return "".join(lines)

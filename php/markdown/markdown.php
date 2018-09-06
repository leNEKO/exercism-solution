<?php
// DRYer headers
function parseHead($line)
{
    if (preg_match('/^(#+)(.*)/', $line, $matches)) {
        $size = strlen($matches[1]);
        $line = "<h$size>" . trim($matches[2]) . "</h$size>";
    }
    return $line;
}

// DRYer styles
function parseText($line)
{
    // we could add more rules here :)
    $rules = [
        "/__(.*)__/" => "<em>$1</em>",
        "/_(.*)_/" => "<i>$1</i>",
    ];
    return preg_replace(array_keys($rules), array_values($rules), $line);
}

// Li
function parseLi($line)
{
    // well the tests wants us to add <p> but i don't know why as plain text in <li> is totally valid
    if (!preg_match("/^</", $line)) {
        $line = "<p>" . $line . "</p>";
    }
    return "<li>" . $line . "</li>";

}

// DRYer paragraph
function parseParagraph($line)
{
    if (!preg_match("/^<[ulph]/", $line) && $line !== "") {
        $line = "<p>" . $line . "</p>";
    }
    return $line;
}

function parseMarkdown($markdown)
{
    $lines = [];
    $list = []; // temporary store for lis (getting rid of $isInList)

    foreach (explode("\n", $markdown . "\n") as $line) {
        $line = parseHead($line);
        $line = parseText($line);

        if (preg_match('/^\*\s*(.*)/', $line, $matches)) {
            // if a list
            $list[] = parseLi($matches[1]); // store it in $list
        } else {
            // if list ended implode the list and append the current line
            if (!empty($list)) {
                $lines[] = "<ul>" . implode("", $list) . "</ul>";
                $list = [];
            }
            $lines[] = parseParagraph($line);
        }

    }
    return implode("", $lines);
}

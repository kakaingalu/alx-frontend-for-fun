#!/usr/bin/python3
"""
Import necessary modules
"""
import markdown
import os
import sys


def convert_markdown_to_html(md, html):
    """
    Converts a Markdown file to HTML.

    Args:
        md (str): Path to the input Markdown file.
        html (str): Path to the output HTML file.
    """

    if not os.path.isfile(md):
        sys.stderr.write('Missing {}\n'.format(md))
        sys.exit(1)

    with open(md, 'r') as f:
        markdown_content = f.read()
    html_content = markdown.markdown(markdown_content)

    with open(html, 'w') as f:
        f.write(html_content)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
    sys.exit(1)

    sys.exit(0)

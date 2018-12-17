"""Creating a Simple Website with Python."""

from browser import document
from browser import html

nav = html.DIV('Welcome to my Python website!', Class="nav")

text = "Hello there!"

cnt = html.DIV(text, Class="content")

ftr = html.DIV('Made with luv by Machel!', Class="footer")

document <= [nav, cnt, ftr]

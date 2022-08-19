def listToString(list):
    toret = ""
    for i in range(len(list)):
        toret = toret + str(list[i])
        if not i == len(list) - 1:
            toret = toret + "; "
    return toret
def n(string):
    print(string)
def e(l, string, style=""):
    return "<" + str(l) + " style=" + '"' + listToString(style) + '"' + ">" + str(string) + "<" + "/" + str(l) + ">"
def ehref(l, string, href):
    return "<" + str(l) + ' href="' + str(href) + '">' + str(string) + "<" + "/" + str(l) + ">"
def p(string, style=None):
    return e("p", string, style)
def h1(string, style=None):
    return e("h1", string, style)
def h2(string, style=None):
    return e("h2", string, style)
def h3(string, style=None):
    return e("h3", string, style)
def h4(string, style=None):
    return e("h4", string, style)
def h5(string, style=None):
    return e("h5", string, style)
def h6(string, style=None):
    return e("h6", string, style)
def blockquote(string, style=None):
    return e("blockquote", string, style)
def hr():
    return "<hr>"
def li(string, style=None):
    return e("li", string, style)
def b(string, style=None):
    return e("b", string, style)
def br():
    return "<br>"
def em(string, style=None):
    return e("em", string, style)
def code(string, style=None):
    return e("code", string, style)
def mark(string, style=None):
    return e("mark", string, style)
def q(string, style=None):
    return e("q", string, style)
def strong(string, style=None):
    return e("strong", string, style)
def audio(string, href, style=None):
    return ehref("audio", string, href)
def img(string, href, style=None):
    return ehref("img", string, href)
def video(string, href, style=None):
    return ehref("video", string, href)
def a(href, string, style=None):
    return ehref("a", string, href)
for i in range(15):
    n(p(i, ["font-size: " + str(i + 15) + "px", "font-family: Impact"]))
    n(hr())

def n(string):
    print(string)
def e(l, string):
    return "<" + str(l) + ">" + str(string) + "<" + "/" + str(l) + ">"
def ehref(l, string, href):
    return "<" + str(l) + ' href="' + str(href) + '">' + str(string) + "<" + "/" + str(l) + ">"
def p(string):
    return e("p", string)
def h1(string):
    return e("h1", string)
def h2(string):
    return e("h2", string)
def h3(string):
    return e("h3", string)
def h4(string):
    return e("h4", string)
def h5(string):
    return e("h5", string)
def h6(string):
    return e("h6", string)
def blockquote(string):
    return e("blockquote", string)
def hr(string):
    return e("hr", string)
def li(string):
    return e("li", string)
def b(string):
    return e("b", string)
def br():
    return "<br>"
def em(string):
    return e("em", string)
def code(string):
    return e("code", string)
def mark(string):
    return e("mark", string)
def q(string):
    return e("q", string)
def strong(string):
    return e("strong", string)
def audio(string, href):
    return ehref("audio", string, href)
def img(string, href):
    return ehref("img", string, href)
def video(string, href):
    return ehref("video", string, href)
def a(href, string):
    return ehref("a", string, href)

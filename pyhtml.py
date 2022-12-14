def listToString(list):
    if not list == None:
        toret = ""
        for i in range(len(list)):
            toret = toret + str(list[i])
            if not i == len(list) - 1:
                toret = toret + "; "
        return toret
    else:
        return ""
def n(string):
    print(string)
def f(string):
    f = open("index.html", "a")
    f.write(string + "\n")
def doctype():
    f("<!DOCTYPE html>")
def end():
    f("</html>")
def e(l, string, style=""):
    return "<" + str(l) + " style=" + '"' + listToString(style) + '"' + ">" + str(string) + "<" + "/" + str(l) + ">"
def ehref(l, string, href="", style=""):
    return "<" + str(l) + " style=" + '"' + listToString(style) + '"' + " href=" + '"' + href + '"' + ">" + str(string) + "<" + "/" + str(l) + ">" 
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
def audio(string, href):
    return ehref("audio", string, href)
def img(string, href):
    return ehref("img", string, href)
def video(string, href):
    return ehref("video", string, href)
def a(href, string):
    return ehref("a", string, href)
def button(href, string):
    return ehref("button", string, href)
def address(string, style=None):
    return e("address", string, style)
def aside(string, style=None):
    return e("aside", string, style)
def footer(string, style=None):
    return e("footer", string, style)

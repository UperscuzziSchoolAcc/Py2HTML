# Py2HTML
#### About
###### Py2HTML is a project im working on after I finish my schoolwork. If it is well recieved somehow, I will start developing this ALOT more. But for now, its just basic HTML
#### Example
###### If I wanted to make an HTML file with Py2HTML, I would first make a newline:
```python
n()
```
###### I would then put HTML elements inside as if they were functions:
```python
n(p("Hello, Welcome to Py2HTML"))
```
###### Which would print this:
```html
<p>Hello, Welcome to Py2HTML</p>
```
###### The n() function prints a line of HTML in the console, but maybe that isn't perferred. Substitute n() for f(), it will now print that line to a file named index.html:
```python
f(p("Hello, Welcome to Py2HTML"))
```
###### Of course, you can concecrate elements to form *cooler* things:
```python
f(p("Hello, Welcome to Py2HTML " + b("NOW BOW TO THE GITHUB GODS!!")))
```
###### Which returns:
```html
<p>Hello, Welcome to Py2HTML <b>NOW BOW TO THE GITHUB GODS!!</b></p>
```
###### Which in HTML is:

<p> Hello, Welcome to Py2HTML <b>NOW BOW TO THE GITHUB GODS!!</b></p>

###### The module has href as well for specific elements (might add more):
```python
img(string, href)
audio(string, href)
```

####  Styling
###### In HTML with most elements you can add a "style=" argument to it
```html
<p style="font-size = 50px; font-family: Impact">haha big text go brrrr</p>
```
###### I added an optional arguement for style, to make the above HTML you would put the styles in a list:
```python
n(p("haha big text go brrrr", ["font-size: 50px" ,  "font-family: Impact"]))
```

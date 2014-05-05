#argparx
![x](http://i.imgur.com/T8BM47b.png)

I was really iritated how the argparse module works in python. Even replacements were no good, so I decided to write my own, for my own needs. 
###What is argparx?
argparx stands for **arg**ument **par**ser **x**(tra) simple

###What are pros and cons of argparx?
| Pros | Cons |
| :--: | :--: |
|SIMPLE|Can be a little tricky if you are not used to it|
|Light|You cannot use multiple values as arguments (ex. '-y' and '--yes')|
|Can be used in every needed situation|Can lack some of the features that argparse has|

###How to use it?
You need to start with initial setup
  ```python
import argparx
parser = argparx.ArgParserX()
  ```
Then you have to **take** your **arg**uments and setup your **program** **def**inition
  ```python
parser.take_args()
parser.program_def("Example")
  ```
Isn't that simple? Now you have your program definition and your args, so why don't we do some magic with our args and define some commands?
  ```python
x = parser.object_arg("-x", helparg="single letter") #1
y = parser.object_arg("--yiks", helparg="multi letter") #2
f = parser.object_arg("-f", helparg="flag", flag=1) #3
z = parser.pos_arg("FILE", pos='start')#4
parser.help_arg() #5
  ```
First two are self-explanatory. 3rd is a flag. Flags always returns True or 1 (or False if not called). 4th is a positional argument, you define argname, which displays in '--help' prompt and a <b>pos</b>ition (it can be 'start' or 'end'). 5th is initialization function of "--help" command - without it there's no "--help".

###TO-DO
[ ] Multi-command support
[ ] Rewrite pos_arg() code

###Requirements
* Python 2.7 - get it from [the official python website](https://www.python.org/download/releases/2.7.6/)

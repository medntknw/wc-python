# wc-python
https://codingchallenges.fyi/challenges/challenge-wc

# Build Your Own wc Tool

This challenge is to build your own version of the Unix command line tool wc!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.
Following these philosophies has made the simple unix command line tools some of the most widely used software engineering tools - allowing us to create very complex text data processing pipelines from simple command line tools. There’s even a Coursera course on Linux and Bash for Data Engineering.

You can read more about the Unix Philosophy in the excellent book The Art of Unix Programming.

# The Challenge - Building wc

The functional requirements for wc are concisely described by it’s man page - give it a go in your local terminal now:

man wc
The TL/DR version is: wc – word, line, character, and byte count. You can see the result in action in the video below:
https://www.youtube.com/watch?v=SGceNxdKabQ

## Step Zero

Like all good software engineering we’re zero indexed! In this step you’re going to set your environment up ready to begin developing and testing your solution.

I’ll leave you to setup your IDE / editor of choice and programming language of choice. After that here’s what I’d like you to do to be ready to test your solution.

Download the this text and save it as test.txt.

## Step One

In this step your goal is to write a simple version of wc, let’s call it ccwc (cc for Coding Challenges) that takes the command line option -c and outputs the number of bytes in a file.

If you’ve done it right your output should match this:

```
ccwc -c test.txt
  342190 test.txt
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

## Step Two

In this step your goal is to support the command line option -l that outputs the number of lines in a file.

If you’ve done it right your output should match this:

```
ccwc -l test.txt
    7145 test.txt
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

## Step Three

In this step your goal is to support the command line option -w that outputs the number of words in a file. If you’ve done it right your output should match this:

```
ccwc -w test.txt
   58164 test.txt
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

## Step Four

In this step your goal is to support the command line option -m that outputs the number of characters in a file. If the current locale does not support multibyte characters this will match the -c option.

You can learn more about programming for locales here

For this one your answer will depend on your locale, so if can, use wc itself and compare the output to your solution:
```
wc -m test.txt
  339292 test.txt
```
```
ccwc -m test.txt
  339292 test.txt
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

## Step Five

In this step your goal is to support the default option - i.e. no options are provided, which is the equivalent to the -c, -l and -w options. If you’ve done it right your output should match this:
```
ccwc test.txt
  7145   58164  342190 test.txt
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

## The Final Step

In this step your goal is to support being able to read from standard input if no filename is specified. If you’ve done it right your output should match this:
```
cat test.txt | ccwc -l
    7145
```
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! You’ve done it, pat yourself on the back, job well done!



# Learnings
1. **How to take stdin as raw bytes vs string?**

   The difference between `sys.stdin.buffer.read()` and `sys.stdin.read()` lies in how they handle input from standard input (stdin):

    1. `sys.stdin.read()`: This function reads input from stdin as a string, assuming it's text data. It reads until it encounters an end-of-file (EOF) marker or until it reaches the specified number of bytes if provided. The input is decoded using the system default encoding, typically UTF-8.
    
    2. `sys.stdin.buffer.read()`: This function reads input from stdin as raw bytes. It does not perform any decoding, so it will return the input exactly as it's received from the input stream, without any interpretation or transformation.
    
    Here's a summary of the differences:
    
    - `sys.stdin.read()`: Reads input from stdin as text, decoding it using the system default encoding.
    - `sys.stdin.buffer.read()`: Reads input from stdin as raw bytes, without decoding.
    
    When to use each:
    - Use `sys.stdin.read()` when you expect input from stdin to be text data and you want to work with it as strings.
    - Use `sys.stdin.buffer.read()` when you expect input from stdin to be binary data, such as images or other non-textual content, and you want to work with it as bytes.

2. **What are locales?**

   Locales are a mechanism used in computer systems to define and manage language, cultural, and regional settings. A locale typically includes information such as language, character encoding, date and time formatting conventions, currency symbols, and other cultural preferences.

3. **How to use locales in python?**

   We can have a standard import `locales` which provide us with functionality to interact with locales


4. **How to set defaults when using argparse?**

   `parser.set_defaults(func=default_action) is a method used to set default values for attributes of the parser.
   When you use parser.set_defaults(func=default_action), you are specifying that the default value for the attribute func of the parser (or of a specific command-line argument) should be default_action.


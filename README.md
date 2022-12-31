# python-intro
Intro python learning code

`Deep Thought - deep.py

“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.



`How to Test

Here’s how to test your code manually:

Run your program with python deep.py. Type 42 and press Enter. Your program should output:
Yes 
Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:
Yes
Run your program with python deep.py. Type forty-two and press Enter. Your program should output
Yes
Run your program with python deep.py. Type 50 and press Enter. Your program should output
No
Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.




`Indoor Voice - indoor.py

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.



`How to Test - indoor.py

Here’s how to test your code manually. At the indoor/ $ prompt in your terminal: :

Run your program with python indoor.py. Type HELLO and press Enter. Your program should output hello.
Run your program with python indoor.py. Type THIS IS CS50 and press Enter. Your program should output this is cs50.
Run your program with python indoor.py. Type 50 and press Enter. Your program should output 50.




`Playback Speed - playback.py

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).



`How to Test

Here’s how to test your code manually:

Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output:
This...is...CS50    
Run your program with python playback.py. Type This is our week on functions and press Enter. Your program should output:
This...is...our...week...on...functions
Run your program with python playback.py. Type Let's implement a function called hello and press Enter. Your program should output
Let's...implement...a...function...called...hello



`Making Faces - faces.py

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.



`How to Test

Here’s how to test your code manually:

Run your program with python faces.py. Type Hello :) and press Enter. Your program should output:
Hello 🙂
Run your program with python faces.py. Type Goodbye :( and press Enter. Your program should output:
Goodbye 🙁
Run your program with python faces.py. Type Hello :) Goodbye :( and press Enter. Your program should output
Hello 🙂 Goodbye 🙁



`Einstein - einstein.py

Even if you haven’t studied physics (recently or ever!), you might have heard that , wherein  represents energy (measured in Joules),  represents mass (measured in kilograms), and  represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.



`How to Test

Here’s how to test your code manually:

Run your program with python einstein.py. Type 1 and press Enter. Your program should output:
90000000000000000
Run your program with python einstein.py. Type 14 and press Enter. Your program should output:
1260000000000000000
Run your program with python einstein.py. Type 50 and press Enter. Your program should output
4500000000000000000




`Tip Calculator - calculator.py

And now for my Wizard tip calculator.

— Morty Seinfeld

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.



`How to Test

Here’s how to test your code manually:

Run your program with python tip.py. Type $50.00 and press Enter. Then, type 15% and press Enter. Your program should output:
Leave $7.50    
Run your program with python tip.py. Type $100.00 and press Enter. Then, type 18% and press Enter. Your program should output:
Leave $18.00
Run your program with python tip.py. Type $15.00 and press Enter. Then, type 25% and press Enter. Your program should output
Leave $3.75




`Home Federal Savings Bank - bank.py

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.



`How to Test

Here’s how to test your code manually:

Run your program with python bank.py. Type Hello and press Enter. Your program should output:
$0 
Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
$0
Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
$20
Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
$100




`File Extensions - extensions.py

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.



`How to Test

Here’s how to test your code manually:

Run your program with python extensions.py. Type happy.jpg and press Enter. Your program should output:
image/jpeg   
Run your program with python extensions.py. Type document.pdf and press Enter. Your program should output:
application/pdf
Be sure to test each of the other file formats, vary the casing of your input, and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.




`Math Interpreter - interpreter.py

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!



`How to Test

Here’s how to test your code manually:

Run your program with python interpreter.py. Type 1 + 1 and press Enter. Your program should output:
2.0 
Run your program with python interpreter.py. Type 2 - 3 and press Enter. Your program should output:
-1.0
Run your program with python interpreter.py. Type 2 * 2 and press Enter. Your program should output
4.0
Run your program with python interpreter.py. Type 50 / 5 and press Enter. Your program should output
10.0




`Meal Time - meal.py

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()



`Challenge

If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:

#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.



`How to Test

Here’s how to test your code manually:

Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
breakfast time   
Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
breakfast time
Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
lunch time
Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
dinner time
Run your program with python meal.py. Type 11:11 and press Enter. Your program should output nothing.

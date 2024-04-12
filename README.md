
In this exercise, you will develop a function named `decode(message_file)`. This function should read an encoded message from a .txt file and
return its decoded version as a string.
<div>
Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).
Your function must be able to process an input file with the following format:
</div>
<pre>
3 love
6 computers
2 dogs
4 cats
1 I
5 you
</pre>
<div>
In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers
into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than
the line above it. The smallest number is 1, and the numbers increase consecutively, like so:
</div>
<pre>
1
2 3
4 5 6
</pre>
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6).

You should ignore all the other words. So for the example input file above, the message words are:
```bash
1: I
3: love
6: computers
```
And your function should return the string `I love computers`. so Please submit the complete code for the decode function: and explain code in two or more compete sentenses.          

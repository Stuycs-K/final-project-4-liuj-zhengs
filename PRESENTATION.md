# OBFUSCATION 101

Imagine this is you writing your final project for Mr. K's cybersecurity class.

![image](https://github.com/Stuycs-K/final-project-4-liuj-zhengs/assets/124070663/2296677b-9c06-49c0-9956-083f9a049fb0)

However... disaster has struck! The person sitting behind you, has copied your code for THEIR final project and is trying to pass it off as their own.

<div align = "center">
    <img src=https://github.com/Stuycs-K/final-project-4-liuj-zhengs/assets/124070663/87222500-b059-4490-980c-b9e2377e83ad>
</div> 


Have you ever had your friend copy your code, 1 for 1, for a CS Assignment? 
Now you can expose them... with code obfuscation!

# What is Obfuscation?
Obfuscation is the process of modifying a program so that it is harder to analyze and understand, but still maintains its original functionality.

## Basic Code Obfuscation Methods
### Variable Renaming and "Encrypting"
Probably the most obvious step to encrypting code would be to change variable names as to prevent the code from being easily readable. For our tool, we replaced all variable names with a random sequence of 15 letters, to make it more difficult to follow what the variables do. For Python, we had to find all the variables by first running the file, then using regex to match the variable names and substituting them with their corresponding "scrambled" name.

### String hex representation
By taking advantage of Python's hex function, we are able to represent all strings as the hex version, but decoded (using the decode method) in UTF-8 format. This converts all strings into a human unreadable format.

### Control Flow Obfuscation
By adding control flows that will not affect the code, we can make the logic of the code a lot harder to follow. Adding statements that will never execute will make the code difficult to comprehend.

```
    x = 0
    while(x > 1):
    	if(x%2==1):
    		x=x*3+1
    	else:
    		x=x/2
    	if(x==1):
    		print("hello!") 
```

### Dummy Code Insertion
Randomly declaring variables will both make it more difficult to analyze using reverse engineering tools, and also for people to read.

# Obfuscation in the Real World

Sure, obfuscation can be used to prevent people from copying your homework.
However, on a larger scale, this IS a big reason why people obfuscate their code. Not just people per se...

![image](https://github.com/Stuycs-K/final-project-4-liuj-zhengs/assets/124070663/a3230e9f-b202-4953-b8af-3b37fe53eec7)

but COMPANIES! Companies obfuscate their software so that their competitors can't just take what they have and run with it.
Not only their software, but data and other personal information is always made hidden and out-of-reach of potential bad actors.

Obfuscation can make it way harder to reverse engineer something. This process is often used by black-hat hackers to search for vulnerabilities within a software, to gain access to critical information.
This works both ways---a government-sponsored agency trying to reverse engineer a virus like Stuxnet would need to go through potential layers of obfuscation, to prolong usage of said virus.

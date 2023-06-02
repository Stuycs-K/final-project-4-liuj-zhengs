## What is Obfuscation?
Obfuscation is the process of modifying a program so that it is harder to analyze and understand, but still maintains its original functionality.

## Basic Code Obfuscation Methods
### Variable Renaming and "Encrypting"
Probably the most obvious step to encrypting code would be to change variable names as to prevent the code from being easily readable. For our tool, we replaced all variable names with a random sequence of 15 letters, to make it more difficult to follow what the variables do. For Python, we had to find all the variables by first running the file, then using regex to match the variable names and substituting them with their corresponding "scrambled" name.

### String hex representation
By taking advantage of Python's hex function, we are able to represent all strings as the hex version, but decoded (using the decode method) in UTF-8 format. This converts all strings into a human unreadable format.

### Control Flow Obfuscation
By adding control flows that will not affect the code, we can make the logic of the code a lot harder to follow. Adding statements that will never execute will make the code difficult to comprehend.

    x = 0
    while(x > 1):
    	if(x%2==1):
    		x=x*3+1
    	else:
    		x=x/2
    	if(x==1):
    		print("hello!") 

### Dummy Code Insertion
Randomly declaring variables will both make it more difficult to analyze using reverse engineering tools, and also for people to read.


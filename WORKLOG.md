# Work Log

## GROUP MEMBER 1: Jeelin Liu

### 5/17/23

- Opened and created assignment

### 5/18/23

- Researched how to create and edit a TryHackMe room, as well as how to upload your own virtual machines to them
  - https://help.tryhackme.com/en/articles/6495821-uploading-interactive-materials
  - https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html
- Researched VM safety
  - https://superuser.com/questions/289054/is-my-host-machine-completely-isolated-from-a-virus-infected-virtual-machine

### 5/22/23

- Researched code obfuscation basic techniques and their applications
  - https://www.guardsquare.com/what-is-code-obfuscation
- Researched reverse engineering---Why we need code obfuscation
  - https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/malware-reverse-engineering/
  - Plan is now: Focus on making a code obfuscator, and make a tryhackme room on reverse engineering to demonstrate the use of our product
- Started work on code_obfuscator.java

### 5/23/23

- We are going to work both in python instead of making one in java and one in python.
- Plan is: 
  - Changed variable names
  - Strings are encrypted/hidden by changing them to hex (non-human-readable)
  - Inserting dummy code, statements that go nowhere, stuff that makes the code longer/more confusing but doesn't actually change the functionality 

### 5/25/23

- Began working on methods to add dummy code and scramble/make messy existing code in obfuscator
- Some common ways that dead code can be created
  - if statements that don't actually run... ex: a if (false) in a while (true)
  - conditionals work well to provide an alternate option but not actually being an option.

## GROUP MEMBER 2: Stanley Zheng

### 5/17/23

- Researched TryHackMe rooms that are feasible for the malware analysis
  - https://tryhackme.com/room/basicdynamicanalysis
  - https://tryhackme.com/room/basicmalwarere

### 5/22/23
- Began working on basic code obfuscator in python
  - Get and change variable names
  - add dummy code
 
### 5/23/23
- Wrote up some rules for determing where variables were in the code
  - has a .,)]= after it?

### 5/24/23
- finished variable name replacement
- added some dummy code adders

### 5/25/23
- convert all strings to hex, but have a method to convert it back (not affect code

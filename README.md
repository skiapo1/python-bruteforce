# python-bruteforce
This project creates a wordlist with 13 attempts (more than 13 attempts the Facebook blocks the next attempts) with a combination of name, birthdate and last name.

## Installation

Use pip to install mechanize

```bash
pip install mechanize
```

## How to use

You need to know the id or username, the birthdate, the name and the last name. 
In the addwl.txt you put all the information like this: id-firstname/lastname//birthdate/// 
Example: skiapo-ysmaili/freitas//24092002///
After changing the addwl.txt file you need to put the user in the users.txt file

## Bash

```bash
python3 addwordlist.py
python3 bruteforce.py
```

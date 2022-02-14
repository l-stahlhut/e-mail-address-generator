# Email address generator

This script generates e-mail addresses from names on the basis of some rules. 



## How to use the script
The script can either be used with a text file with names or with a single name in the terminal. 
1) List of names (txt-file)
```python
$ python3 email_address_generator.py data/names.txt
```
2) Single name (terminal)
```python
$ python3 email_address_generator.py "Michael Richards"
```

## Rules after which to generate the e-mail adresses
- if the name contains umlauts ö, ä, ü, they should be replaced by oe, ae, ue.
- if the name contains vowels with an accent, replace them with the same vowel but without accent
- the first part of the e-mail address should consist of the first name and the last name seperated by a dot. 
- if someone has a middle name, it should be attached to the first name. If first and middle name exceed 8 characters, only the consonants should be used. 
- if the domain is 'stu', the e-mail address should end in @uzh
- if the domain is not stu, the e-mail address should include the domain, e.g. @cl.uzh.ch
- When a name is given via the command line, no domain needs to be given and the output should default to a student e-mail address. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
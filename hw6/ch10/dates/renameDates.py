#! python



import shutil, os, re



#Create a regex that matches files wih American date format

datePattern = re.compile(r"""^(.*?)# all text before the date
    ((0|1)?\d)-                 #one or two difgits for the month
    ((0|1|2|3)?\d)-             # one or two digits for the day
    ((19|20)\d\d)               # four digits for the year
    (.*?)$                      # all text after the date
    """, re.VERBOSE)
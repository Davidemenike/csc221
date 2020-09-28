 1. for the one, copy shuffled words text into the new version which we will change. i.e cp shuffled-words.txt shuffled-words-sorted.txt. Then simply get into the vim of the new file. and :sort which will aautomatically save it for you. After that just save and quit 'wq!'


 2. This one might be a bit trickier. Obviously first copy paste the file into the same directory and change the name of the file. thene using the sort, uniq -c and head-11 with [n\*] which gets us the common numbers tht appear as well as [:alnum:] which is a command that gives us the number alphanumeric digit with it,we get out answer. problem was i couldn't save what i cut out, i could only view it.

 3. Same as the last one, the exact same code as the last one gives an answer.

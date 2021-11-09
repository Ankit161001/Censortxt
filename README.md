# Censortxt
A python package which censors parts of text.
<br>
### About the package
The package works alongside a database of words which contains the words meant to be censored from the text. The words in the database can be edited as per a user's choice.
<br>
### Usage
After the `pip install` command, include the following lines in your python code. <br>
`from censortxt import censor_text` <br>
It imports the components of the package. <br>
Then execute the following code to create a database in the local directory. <br>
`censor_text.create()` <br>
Note: use this code just once as only one instance of the database is needed.

### Documentation
Here are the functionalities available with the following package:
1) `censor(--text passed here--)` this function censors the text passed along with it and prints the censored text.
2) `add_words(word1 word2 ---)` this funtion adds new words into the database. The words passed should be separated by a space.
3) `add_word(word)` this funciton adds a new word into the database.
4) `remove_words(word1 word2 ---)` this funtion removes/deletes words from the database. The words passed should be separated by a space.
5) `remove_word(word)` this funciton removes/deletes a word from the database.
6) `show_words()` this function prints all the words present in the database along with their ID.
7) `query(--query passed here--)` this function is for users to explicitely run queries on the database.
8) `default()` this funciton reverts all the changes made in the database and the database returns to its initial state. it also deletes any custom words added.
9) `text_toxicity(--text passed here--)` this funciton return the toxicity percentage (censored words / total words * 100) of the text passed into it.
<br>

### Requirements
Python 3.6 or above must be installed in the system.

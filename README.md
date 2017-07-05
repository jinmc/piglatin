# piglatin


Pig Latin is a "secret" language used by children, often in the belief that their parents won't understand them. The rules are simple:

If a word begins with a vowel, add "hay" to the end. Example: "apple" → "applehay".
If a word begins with one or more consonants, move those consonants to the end, and add "ay". Example: "string" → "ingstray".
The innocent-sounding words "vowel" and "word" are not easy to define precisely. For the purposes of this assignment:
Letters are whatever the method isalpha says they are. (This includes the 26 uppercase and 26 lowercase letters in the English alphabet).
The vowels are a e i o u and their uppercase variants, but never y or w.
You can assume that every word contains at least one of the above vowels.
The words are non-empty strings that you find by applying the following rules:
Spaces go between words. Use spaces to break a "sentence" into word-like chunks.
Hint: sentence.split(' ') will give return a list of strings, but some of those strings will be the empty string, and those you need to get rid of.
Each word-like chunk will consist of a word followed by zero or more non-letters.
Example: The string "Hello," consists of the word (by our rules) Hello and the non-letter , (comma).
Hint: my_string.isalpha() will return True if my_string contains nothing but letters. (Note that my_string could be a single character.)
We will not handle:
Punctuation at the beginning of a word: "--Dave"
Groups of characters not containing a vowel: "$500", "  --  ", "cwm"
You may handle the above if you like, but we won't test for them.


def is_vowel(ch)
Return True if ch is a vowel, False if it isn't.

def cut(word)
Given a word (as defined above), return a 2-tuple. The first element of the tuple is the string of consonants at the beginning of the word (could be the empty string), and the second element is a string of all the remaining characters. For example, cut("String") should return the tuple ("Str", "ing").

def piggify_word(word)
Returns the Pig Latin version of a single word. (Hint: Use the cut function.)

def clean_word(raw_word)
"Cleans" the given "raw" word by removing any non-letter characters from the end, and returning a 2-tuple of the cleaned word and the removed characters. For example, clean_word("Wow!") should return ("Wow", "!").

def get_raw_words(sentence)
Uses the space character (' ') to separate the sentence into a list of word-like chunks ("raw" words), and returns that list of chunks. For example, get_raw_words("Madam, I'm Adam.") should return the list ["Madam,", "I'm", "Adam."].

def piggify_pairs(pair_list)
Takes a list of (word, punctuation) pairs and returns the corresponding list of ("piggified" word, punctuation) pairs. For example, piggify_pairs([("hi", ""), ("there", "!")]) should return [("ihay", ""), ("erethay", "!")].

def reassemble(pair_list)
Reassembles a list of (word, punctuation) pairs into a sentence. The word and its associated punctuation are concatenated, and the words are assembled into a sentence, with spaces between words (but no space at the beginning or at the end). For example, reassemble([("ihay", ""), ("erethay", "!")]) should return "ihay erethay!".

def piggify_sentence(sentence)
Takes a sentence, turns each word in the sentence into the corresponding Pig Latin version, then returns the altered sentence. Punctuation is preserved.

def main()
Ask the user to type in sentences. For each line that is read in, the function prints out the corresponding Pig Latin version. Quits the program (by reaching the end of the main method) when the user enters a blank line. This is the only function that does input/output, and is the only function that does not require a unit test.

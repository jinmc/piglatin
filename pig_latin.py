#import string


def is_vowel(ch):
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:    
        return True
    else:
        return False
    
def cut(word):
    for n in range(len(word)):
        if is_vowel(word[n]):
            return (word[0:n], word[n:len(word)])
# ex) cut('word') becomes ('w', 'ord')
                    
def piggify_word(word):
    for n in range(len(word)):
        if is_vowel(word[n]):
            if n == 0:
                return word + "hay"
            else:
                return cut(word)[1] + cut(word)[0] + "ay"

def clean_word(raw_word):
	if str.isalpha(raw_word[len(raw_word) - 1]):
		return (raw_word, "")
	else:
		return (raw_word[0:len(raw_word) - 1], raw_word[len(raw_word) - 1])
#def clean_word(raw_word):
#    if raw_word[len(raw_word) - 1] not in list(string.ascii_letters):
#        return (raw_word[0:len(raw_word) - 1], raw_word[len(raw_word) - 1])
#    else:
#        return (raw_word, "")
# ex) clean_word("Wow!") becomes ("Wow", "!") 

def get_raw_words(sentence):
    a = []
    b = ""
    for n in range(len(sentence)):
        if sentence[n] != " ":
            b += sentence[n]
        else:
            a.append(b)
            b = ""
    a.append(b)
    return a

# ex) get_raw_words("This, is good.") becomes ("This,", "is", "good.")
            
def piggify_pairs(pair_list):
    new_list = []
    for n in range(len(pair_list)):
        new_list.append((piggify_word(pair_list[n][0]), pair_list[n][1]))
    return new_list

# ex) piggify_pairs([("hi", ""), ("there", "!")]) becomes [('ihay', ''), ('erethay', '!')]                      

def reassemble(pair_list):          # making piggify_pairs into sentence
    sentence = ""
    for n in range(len(pair_list)):
        sentence += pair_list[n][0] + pair_list[n][1] + " "
    return sentence.rstrip()

def piggify_sentence(sentence):
    pigpair = []
    for n in range(len(get_raw_words(sentence))):
        pigpair.append(clean_word(get_raw_words(sentence)[n]))
    return reassemble(piggify_pairs(pigpair))


def main():
    sentence = input("Enter the sentence:")
    print("piggified sentence:", piggify_sentence(sentence))
    


if __name__ == "__main__":
    main()

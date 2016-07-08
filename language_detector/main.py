"""This is the entry point of the program."""

from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    '''makes the paragraph break into a list'''
    word_list = text.split()

    # How many languages do we have?
    lang_count = len(LANGUAGES) 
    
    # We will now create a dictionary. Key name will be
    # language name, and value (initially 0) will be the count of words
    # in word_list that were found in our paragraph
    lang_list = {}
    for l in LANGUAGES:
        tmp_lang = l["name"]
        lang_list[tmp_lang] = 0 #Eg: lang_list["Chinese"] = 0
        
    # OK, now we have initialised our dictionary, it's time to count...
    '''this will take each word from the word_list and test it with our group
    of words'''
    for x in word_list:
    
        '''this will take the find out how many languages we have and put them 
        in a range'''
        for y in range(lang_count):
            
            '''Stands for current language:''' 
            current_lang = LANGUAGES[y]
            
            '''calls in the external list lang_list'''
            #global lang_list
          
            '''this if staement makes a loop passing the word into the groups 
            of languages'''
            if x in current_lang['common_words']:
                
                '''once it matches they add the count of the of the language'''
                lang_list[current_lang['name']] += 1 # Eg: lang_list["Spanish"] += 1
                
    # Now we have a list of languages and a count of the number of times their
    # common word were found in our lang_list dictionary
    
    # Time to figure out which language has the highest value
    ranking = sorted(lang_list, key=lang_list.get, reverse=True)
    # We should now have a list of ranked languages
    
    return ranking[0]
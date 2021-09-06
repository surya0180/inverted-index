def tokenizeFile(file, delimiters, stop_words, docId):
    # Removing all the stop words from the document
    # for i in stop_words:
    #     file = str(file).replace(" "+i+" ", ' ')

    # Removing all the delimiters from the document and replacing them with whitespace
    # Because by doing like that, we can split the document very easily.
    for i in delimiters:
        file = str(file).replace(i, ' ')

    # Splitting the document into terms
    step_1 = str(file).split(' ')
    finalised_words = []

    # Storing all the tokenized words in the "finalised_words" list
    for i in step_1:
        if(i.lower() not in stop_words and i != ''):
            finalised_words.append({'term': i.lower(), 'docId': docId})
    return finalised_words # Returning the final tokenized words as a list

if __name__ == '__main__':
    # Opening the text files required for the tokenizing ( Stop words and the output of the final tokenized words )
    sw = open('./stop_words.txt', 'r+', encoding='utf8')
    output = open('./output.txt', 'w', encoding='utf8')

    # Delimiters used in the tokenized process which includes all the necessary special charachters
    delimiters = ['.', ',', '“', '”', '-', "’s","'s", "\n", "\t", "'", "’", "‘", '—', '/', 
                  '(', ')', "!", "&", "~", "@", "#", "$", "%", "^", "*", "_", "₹", '\\',
                  "+", "=", "`", "<", ">", "?", "|", "[", "]", "{", "}", ":", ";", "\xa0"]

    stop_words = sw.read().split('\n') # Stop words used for tokenizing the terms
    dictionary = []  # Initialising the universal dictionary of words as an empty list

    # An iterator which iterates through all the documents and retrieves all the terms and stores them in a dictionary
    for number in range(101, 282):
        document = open('./th-dataset/{}.txt'.format(number), 'r+', encoding='utf8') # Opening the appropriate document w.r.t the iterator
        tokenized_words = tokenizeFile(document.read().lower(), delimiters, stop_words, number) # Retrieving the terms after the tokeniziation process
        dictionary = dictionary + tokenized_words # Adding the retrieved terms to the universal dictionary
        document.close() # Closing the opened document
    sw.close() # Closing the opened Stop words file

    dictionary = sorted(dictionary, key=lambda k: k['term'])  # Arranging the universal dictionary in alphabetical order

    # Outputting the universal dictionary to the output.txt
    for i in dictionary:
        output.write(i['term']+" "+str(i['docId'])+"\n")
    output.close() # Closing the opened output file
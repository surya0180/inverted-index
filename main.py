import termtables as tt

# Function used to tokenize the file
def tokenizeFile(file, delimiters, after_delimiters, stop_words, docId):
    # Removing all the delimiters from the document and replacing them with whitespace
    # Because by doing like that, we can split the document very easily.
    for i in delimiters:
        file = str(file).replace(i, ' ')
    # print(file)

    # Removing all the stop words from the document
    for i in stop_words:
        file = str(file).replace(" "+i+" ", ' ')
    # print(file)

    # Removing the delimiters which must be removed after removing the stop words
    for i in after_delimiters:
        file = str(file).replace(i, ' ')
    # print(file)

    # Splitting the document into terms
    step_1 = str(file).split(' ')
    finalised_words = []

    # Storing all the tokenized words in the "finalised_words" list
    for i in step_1:
        if(i.lower() not in stop_words and i != ''):
            finalised_words.append({'term': i.lower(), 'docId': docId})
    return finalised_words # Returning the final tokenized words as a list

# Function used to create the main inverted index
def prepareInvertedIndex(dictionary):
    inverted_index = {} # Initialising an empty dictionary

    for i in dictionary: # looping through the vocabulary we created and passed to this function

        if inverted_index.get(i['term']) == None: # Basically checks if the term exists or not
            inverted_index[i['term']] = {'frequency': 0, 'posting_list': []} # Initialising the dictionary with empty posting list and 0 frequency

        if i['docId'] not in inverted_index[i['term']]['posting_list']: # Checking whether the document id is present or not in the posting list of respective term
            inverted_index[i['term']]['posting_list'].append(i['docId']) # Appending the document id here
        inverted_index[i['term']]['frequency'] = inverted_index[i['term']]['frequency'] + 1 # Increasing the frequency of the term

    return inverted_index # Returning the complete inverted index

if __name__ == '__main__':
    # Opening the text files required for the tokenizing ( Stop words and the output of the final tokenized words )
    sw = open('./stop_words.txt', 'r+', encoding='utf8')
    output = open('./output.txt', 'w', encoding='utf8')

    # Delimiters used in the tokenized process which includes all the necessary special charachters
    delimiters = ['.', ',', '“', '”', '-', "’s","'s", "\n", "\t", '—', '/', 
                  '(', ')', "!", "&", "~", "@", "#", "$", "%", "^", "*", "_", "₹", '\\',
                  "+", "=", "`", "<", ">", "?", "|", "[", "]", "{", "}", ":", ";", "\xa0"]
    # Delimiters used to remove after removing the stop words
    after_delimiters = ["'", "’", "‘"]

    stop_words = sw.read().split('\n') # Stop words used for tokenizing the terms
    dictionary = []  # Initialising the universal dictionary of words as an empty list

    # An iterator which iterates through all the documents and retrieves all the terms and stores them in a dictionary
    for number in range(101, 282):
        document = open('./th-dataset/{}.txt'.format(number), 'r+', encoding='utf8') # Opening the appropriate document w.r.t the iterator
        tokenized_words = tokenizeFile(document.read().lower(), delimiters, after_delimiters, stop_words, number) # Retrieving the terms after the tokeniziation process
        dictionary = dictionary + tokenized_words # Adding the retrieved terms to the universal dictionary
        document.close() # Closing the opened document
    sw.close() # Closing the opened Stop words file

    dictionary = sorted(dictionary, key=lambda k: k['term'])  # Arranging the universal dictionary in alphabetical order
    
    # Below code will print the vocabulary stored in the main memory.

    # # Print the Vocabulary in the terminal by uncommenting this code
    # dictionary_data = []
    # for i in dictionary:
    #     dictionary_data.append([i['term'], str(i['docId'])])
    # print(tt.to_string(
    #     dictionary_data,
    #     header = ["Term", "Document ID"],
    #     style = tt.styles.ascii_thin_double,
    # ))

    inverted_index = prepareInvertedIndex(dictionary) # Creating the inverted index by passing the vocabulary to the function

    # # Generating the table ui to print it the the output.txt. 
    # # Please make sure that you install the necessary library before running this code.
    # # If you dont want this fancy way of printing the table, you can comment the code from line 89 to 97, and uncomment line 100 and 101.

    tabulate_data = []
    for i in inverted_index:
        tabulate_data.append([i , str(inverted_index[i]['frequency']) , " ".join(str(i) for i in inverted_index[i]['posting_list'])])
    string = tt.to_string(
        tabulate_data,
        header=["Term", "Frequency", "Posting List"],
        style=tt.styles.ascii_thin_double,
    )
    output.write(string)

    # # Storing the Posting lists( Inverted Index ) in the secondary memory ( Hard drive, SSD )

    # for i in inverted_index:
    #     output.write("Word: " + i + "\tFrequency: " + str(inverted_index[i]['frequency']) + "\tPosting List: " + " ".join(str(i) for i in inverted_index[i]['posting_list']) + "\n")

    output.close()
About the Data Structure:-

Delimiters: Used a basic python list to store all the required delimiters in it.

Stop Words: Used a basic python list to store all the required stop words in it.

Vocabulary: Used a list of dictionaries with terms and document id's as key value pairs.
            Example: [
                        {
                            "term": "advocate",
                            "docId": 103
                        }
                    ]

Posting Lists: Used a basic python list to store all the required document ids in it.

Inverted Index: The entire data structure is as follows:

                1.) A dictionary is used to store all the terms as keys.
                2.) The values for these keys will be another dictionaries.
                3.) Now these dictionaries contains two key value pairs namely "frequency" and "posting list".
                4.) Where frequency is the total number of occurences of a word in all documents.
                5.) Posting list consists of all the document id's in which the word is present.

            Example: {
                "advocate": {
                    "frequency": 28,
                    "posting_list": [103, 105, 112, 118, 196, 225, 268]
                }
            }


Time Complexity:-

1.) It takes O(k) to iterate through the delimiters where k is the length of the delimiter list which is a constant, 
therefore we can ignore it. Same goes for the stop words.

2.) All the documents will be iterated which takes O(m) where m is the total number of documents.

3.) For each document the tokenization process will take the order of O(n) where n is the total number of tokens generated.

4.) After all the documents are tokenized, the total time complexity would be in the order of O(m)*O(n) = O(m*n),
where m is the total number of documents and n is the total number of tokens on an average generated per file.

5.) Sorting the tokens and generating the vocabulary will take the order of O(m*n) where n is the number of tokens generated per 
document and m is the total number of documents.

6.) Generating the posting lists from the vocabulary will take another O(m*n) where n is the number of tokens generated per 
document and m is the total number of documents.

7.) If we sum up all the complexities we got, we will get O(m*n)



Space Complexity:-

We will be storing all the n terms generated from all the documents in the form of a dictionary where the posting list 
takes the number of documents the particular term occured. So, for all the m documents the space complexity in worst 
possible case would be O(m*n), where m is the total number of documents stored in the posting list, and n is the 
total number of terms.


In Short:

Time-Complexity:-  O(m*n) where m is the total number of documents and n is the number of tokens generated per document.
Space-Complexity:- O(m*n) where m is the total number of documents stored in the posting list, and n is the  
                   total number of terms.



Some points regarding my implemetation:

1.) I considered all the possible delimiters to be used for tokenization and stored them in an array, same with the
stop words aswell

2.) Firstly i remove all the delimiters by replacing them simply with white spaces and then remove all the stop words.

3.) Important thing that should be noted here is that the stop words list is not a fixed one in this assignment. 
After searching the internet, I have chosen the best possible list of stop words which I thought would be sufficient 
for this assignment. Replacing the stop words will simply change the outcomes of the result completely.

4.) After removing the stop words there are few delimiters which are left, removing them will complete the tokenization 
process and we can return the generated terms.

5.) Storing all of them in a list of dictionaries will give us the vocabulary.

6.) Passing the vocabulary to the function, we are generating the inverted index with the frequencies and posting 
lists of each word.

7.) Here the frequencies are the total number of times a word has occured in all the document. For example:
    if advocate occured: 
        3 times in doc 1
        5 times in doc 2
        8 times in doc 3
    the frequency of the word "advocate" is 16 for the 3 documents.

Note:-

1.) Please make sure you download the library (termtables [ pip install termtables(windows) ]) before you run the code.
2.) To print the vocabulary which is stored in the main memory, simply uncomment the code from line (74, 81).
3.) Please change the path of the dataset in the code before you run it. Same with all the output files and stop words.
4.) I have listed all the stop words in a seperate text file ( Assign012019174-stopwords.txt ) because the list of stop 
    words is too huge to include it in the code. 


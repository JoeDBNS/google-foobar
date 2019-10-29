'''
Spy Snippets
============

You've been recruited by the team building Spy4Rabbits, a highly advanced 
search engine used to help fellow agents discover files and intel needed 
to continue the operations against Dr. Boolean's evil experiments. The team 
is known for recruiting only the brightest rabbit engineers, so there's 
no surprise they brought you on board. While you're elbow deep in some 
important encryption algorithm, a high-ranking rabbit official requests 
a nice aesthetic feature for the tool called "Snippet Search."  While you 
really wanted to tell him how such a feature is a waste of time in this 
intense, fast-paced spy organization, you also wouldn't mind getting kudos 
from a leader. How hard could it be, anyway?

When someone makes a search, Spy4Rabbits shows the title of the page. 
Your commander would also like it to show a short snippet of the page 
containing the terms that were searched for. 

Write a function called answer(document, searchTerms) which returns the 
shortest snippet of the document, containing all of the given search terms. 
The search terms can appear in any order.

The length of a snippet is the number of words in the snippet. For example, 
the length of the snippet "tastiest color of carrot" is 4. (Who doesn't like 
a delicious snack!)

The document will be a string consisting only of lower-case letters [a-z] 
and spaces. Words in the string will be separated by a single space. A word 
could appear multiple times in the document.
searchTerms will be a list of words, each word comprised only of lower-case 
letters [a-z]. All the search terms will be distinct.

Search terms must match words exactly, so "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. For example, 
if the document is "world there hello hello where world" and the search terms 
are ["hello", "world"], you must return "world there hello".

The document will be guaranteed to contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, 
and each word will be 1 to 10 letters long. Repeat words in the document are 
considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, 
and each word will not be more than 10 letters long.


Test cases
==========

Inputs:
    (string) document = "many google employees can program"
    (string list) searchTerms = ["google", "program"]
Output:
    (string) "google employees can program"

Inputs:
    (string) document = "a b c d a"
    (string list) searchTerms = ["a", "c", "d"]
Output:
    (string) "c d a"
'''


# Fails Secret Test Case #5
def answer1(document, searchTerms):
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippits = []
    snippitValues = []
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    for item in srcTermsDict[searchTerms[0]]:
        depth = 1
        termList = [item]
        while depth < len(searchTerms):
            termList.append(min(srcTermsDict[searchTerms[depth]], key = lambda x:abs(x - max(termList))))
            depth += 1
        snippits.append(termList)
    for string in snippits:
        snippitValues.append(max(string) - min(string))
    minIndex = min(snippits[snippitValues.index(min(snippitValues))])
    maxIndex = max(snippits[snippitValues.index(min(snippitValues))]) + 1
    return ' '.join(docTerms[minIndex:maxIndex])


# Fails Secret Test Case #5
def answer2(document, searchTerms):
    searchTerms = sorted(set(searchTerms))
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippits = []
    snippitValues = []
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    for item in srcTermsDict[searchTerms[0]]:
        depth = 1
        termList = [item]
        while depth < len(searchTerms):
            termList.append(min(srcTermsDict[searchTerms[depth]], key = lambda x:abs(x - max(termList))))
            depth += 1
        snippits.append(termList)
    for string in snippits:
        snippitValues.append(max(string) - min(string))
    minIndex = min(snippits[snippitValues.index(min(snippitValues))])
    maxIndex = max(snippits[snippitValues.index(min(snippitValues))]) + 1
    return ' '.join(docTerms[minIndex:maxIndex])


def answer3(document, searchTerms):
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippits = []
    snippitValues = []
    
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    
    for i in range(0, len(searchTerms)):
        for item in srcTermsDict[searchTerms[i]]:
            depth = 1
            termList = [item]
            while depth < len(searchTerms):
                print(sorted(termList))
                print(sum(termList)/len(termList))
                termList.append(min(srcTermsDict[searchTerms[depth]], key = lambda x:abs(x - sum(termList)/len(termList)-1)))
                depth += 1
            
            snippits.append(termList)
    
    for string in snippits:
        snippitValues.append(max(string) - min(string))
    
    minIndex = min(snippits[snippitValues.index(min(snippitValues))])
    maxIndex = max(snippits[snippitValues.index(min(snippitValues))]) + 1
    
    return ' '.join(docTerms[minIndex:maxIndex])

''' VVV WORKS BUT SLOW VVV '''
def answer4(document, searchTerms):
    searchTerms = list(set(searchTerms))
    docTerms = document.split()
    usedTerms = []
    snip = []
    bestSnippits = docTerms
    docTermPos = 0
    
    while docTermPos != len(docTerms):
        num = docTermPos
        while len(usedTerms) != len(searchTerms) and num < len(docTerms):
            if docTerms[num] in searchTerms or len(usedTerms) > 0:
                snip.append(docTerms[num])
                
                if docTerms[num] in searchTerms and docTerms[num] not in usedTerms:
                    usedTerms.append(docTerms[num])
            
            num += 1
        
        usedTerms = []
        
        isIn = dict()
        if len(snip) < len(bestSnippits):
            for term in searchTerms:
                if term in snip:
                    isIn[term] = True
                else:
                    isIn[term] = False
                
            if False not in isIn.values():
                bestSnippits = snip
        
        snip = []
        docTermPos += 1
    
    return ' '.join(bestSnippits)


# Fails Secret Test Case #5
def answer5(document, searchTerms):
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippets = []
    snippetValues = []
    
    usedValue = []
    srcTermIndxValues = []
    
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    
    for term in searchTerms:
        for item in srcTermsDict[term]:
            depth = 1
            termList = [item]
            
            while depth < len(searchTerms):
                minVal = min(srcTermsDict[searchTerms[depth]], key = lambda x:abs(x - min(termList)))
                maxVal = min(srcTermsDict[searchTerms[depth]], key = lambda x:abs(x - max(termList)))
                
                if abs(minVal - min(termList)) < abs(maxVal - max(termList)):
                    termList.append(minVal)
                else:
                    termList.append(maxVal)
                    
                depth += 1
                
            if len(list(set(termList))) >= len(searchTerms):
                snippets.append(termList)
    
    for string in snippets:
        snippetValues.append(max(string) - min(string))
    
    minSnipVal = min(snippetValues)
    bestVal = [len(docTerms)]
    
    
    for indx, item in enumerate(snippets):
        if snippetValues[indx] == minSnipVal and min(item) < min(bestVal):
            bestVal = item
    
    return ' '.join(docTerms[min(bestVal):max(bestVal)+1])


# Fails Secret Test Case #5
def answer6(document, searchTerms):
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippets = []
    
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    
    for term in searchTerms:
        for srcTerm in srcTermsDict[term]:
            snip = []
            for nxtSrcTerm in srcTermsDict.keys():
                indxDist = [abs(srcTerm - x) for x in srcTermsDict[nxtSrcTerm]]
                snip.append(srcTermsDict[nxtSrcTerm][indxDist.index(min(indxDist))])
            snippets.append(snip)
    
    winSnip = snippets[0]
    
    for snip in snippets:
        if max(snip) - min(snip) < max(winSnip) - min(winSnip):
            winSnip = snip
    
    return ' '.join(docTerms[min(winSnip):max(winSnip)+1])


def answer7(document, searchTerms):
    docTerms = document.split()
    srcTermsDict = {term: [] for term in searchTerms}
    snippets = []
    
    # find all instances of all terms and keep track with dictionary
    for term in searchTerms:
        for x in range(0, docTerms.count(term)):
            srcTermsDict[term].append([i for i, n in enumerate(docTerms) if n == term][x])
    
    # build list of possible snippet lists
    for term in searchTerms:
        for srcVal in srcTermsDict[term]:
            snip = []
            # build snip by finding closest values spanning all searchTerms
            for srcTerm in srcTermsDict.keys():
                indxDist = [abs(srcVal - x) for x in srcTermsDict[srcTerm]]
                snip.append(srcTermsDict[srcTerm][indxDist.index(min(indxDist))])
            snippets.append(snip)
    
    winSnip = snippets[0]
    
    for snip in snippets:
        if max(snip) - min(snip) < max(winSnip) - min(winSnip):
            winSnip = snip
    
    return ' '.join(docTerms[min(winSnip):max(winSnip) + 1])




def Test_Answer(testCase, document, searchTerms):
    retVal = answer7(document, searchTerms)
    goodVal = answer4(document, searchTerms)
    if retVal == goodVal:
        print('Test Case', testCase, ':\tPass\t', retVal)
    else:
        print('\nTest Case', testCase, ':\tFail')
        print('Correct:', goodVal)
        print('Actual:\t', retVal, '\n')


testCase = 0


testCase += 1
document = 'can many google employees can not ever google not program can never google sometimes google employees because google is a technology google can program google company that google writes google program can programs'
searchTerms = ['google', 'can', 'program']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'many google employees can program can google employees because google is a technology company that writes programs'
searchTerms = ['google', 'program', 'can']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'many google employees can program'
searchTerms = ['google', 'program']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'many google employees can program'
searchTerms = ['many', 'program']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b d a c a c c d a'
searchTerms = ['a', 'c', 'd']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c d a'
searchTerms = ['a', 'c', 'd']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world there hello hello where world'
searchTerms = ['hello', 'world']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world there tester test test  tester a test hello hello tester test where world tester world a there test hello hello test test where world world a there test hello hello test test where world world there test hello hello test test where world'
searchTerms = ['hello', 'test', 'a', 'world']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world there hello hello where world'
searchTerms = ['hello', 'world']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world test          test where hello a test test                     where world'
searchTerms = ['world', 'test', 'where']
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c d a'
searchTerms = ["c", "d", "a"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c d a'
searchTerms = ["d", "a", "c"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c d a'
searchTerms = ["c", "d", "a"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'the'
searchTerms = ["the"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'the cats run very fast in the rain'
searchTerms = ["cats"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c r z q d a c b a a a a a d d d'
searchTerms = ["c", "d", "a"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c r z q d a c b q a a a a a q d d d'
searchTerms = ["a"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a b c r z q d a c b q a a a a a q d d d'
searchTerms = ["a", "q"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world there hello hello hello where world'
searchTerms = ["hello"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'world there hello hello where world'
searchTerms = ["hello", "world"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'a sad dog walks along the path where he was walked last week he says that he is a sad dog because he is hungry and does not get to play a lot the dog wants to walk and be playful all day long an other dog would sometimes play in the same area but he would walk somewhere else as this dog was not a fan of the path'
searchTerms = ["walk", "a", "dog", "path"]
Test_Answer(testCase, document, searchTerms)


testCase += 1
document = 'can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google'
searchTerms = ['writes', 'can', 'many', 'ever', 'not', 'sometimes', 'google', 'employees', 'programs', 'that', 'company', 'technology', 'is', 'a']
Test_Answer(testCase, document, searchTerms)
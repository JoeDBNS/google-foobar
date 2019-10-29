# spy_snippets



def answer(document, searchTerms):
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





document = 'can many google employees can not ever google not program can never google sometimes google employees because google is a technology google can program google company that google writes google program can programs'
searchTerms = ['google', 'can', 'program']
print(answer(document, searchTerms))


document = 'many google employees can program can google employees because google is a technology company that writes programs'
searchTerms = ['google', 'program', 'can']
print(answer(document, searchTerms))


document = 'many google employees can program'
searchTerms = ['google', 'program']
print(answer(document, searchTerms))


document = 'many google employees can program'
searchTerms = ['many', 'program']
print(answer(document, searchTerms))


document = 'a b d a c a c c d a'
searchTerms = ['a', 'c', 'd']
print(answer(document, searchTerms))


document = 'a b c d a'
searchTerms = ['a', 'c', 'd']
print(answer(document, searchTerms))


document = 'world there hello hello where world'
searchTerms = ['hello', 'world']
print(answer(document, searchTerms))


document = 'world there tester test test  tester a test hello hello tester test where world tester world a there test hello hello test test where world world a there test hello hello test test where world world there test hello hello test test where world'
searchTerms = ['hello', 'test', 'a', 'world']
print(answer(document, searchTerms))


document = 'world there hello hello where world'
searchTerms = ['hello', 'world']
print(answer(document, searchTerms))


document = 'world test          test where hello a test test                     where world'
searchTerms = ['world', 'test', 'where']
print(answer(document, searchTerms))


document = 'a b c d a'
searchTerms = ["c", "d", "a"]
print(answer(document, searchTerms))


document = 'a b c d a'
searchTerms = ["d", "a", "c"]
print(answer(document, searchTerms))


document = 'a b c d a'
searchTerms = ["c", "d", "a"]
print(answer(document, searchTerms))


document = 'the'
searchTerms = ["the"]
print(answer(document, searchTerms))


document = 'the cats run very fast in the rain'
searchTerms = ["cats"]
print(answer(document, searchTerms))


document = 'a b c r z q d a c b a a a a a d d d'
searchTerms = ["c", "d", "a"]
print(answer(document, searchTerms))


document = 'a b c r z q d a c b q a a a a a q d d d'
searchTerms = ["a"]
print(answer(document, searchTerms))


document = 'a b c r z q d a c b q a a a a a q d d d'
searchTerms = ["a", "q"]
print(answer(document, searchTerms))


document = 'world there hello hello hello where world'
searchTerms = ["hello"]
print(answer(document, searchTerms))


document = 'world there hello hello where world'
searchTerms = ["hello", "world"]
print(answer(document, searchTerms))


document = 'a sad dog walks along the path where he was walked last week he says that he is a sad dog because he is hungry and does not get to play a lot the dog wants to walk and be playful all day long an other dog would sometimes play in the same area but he would walk somewhere else as this dog was not a fan of the path'
searchTerms = ["walk", "a", "dog", "path"]
print(answer(document, searchTerms))


document = 'can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs can many google employees can not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google writes google program can programs not ever google not program can never google sometimes google employees because google is a technology google google can program google company that google'
searchTerms = ['writes', 'can', 'many', 'ever', 'not', 'sometimes', 'google', 'employees', 'programs', 'that', 'company', 'technology', 'is', 'a']
print(answer(document, searchTerms))
from text_analyzer import *

#The following two functions are examples of the above functions being called
#on a text file containing Alice In Wonderland

def printAlice(top_number):
    top = TopList('alice_in_wonderland.txt', top_number)
    freq = TopFrequencies('alice_in_wonderland.txt', top_number)
    multi = MergeTop(top, freq)
    PrintList(multi)

def Alice():
    while True:
        which = raw_input("Hello! For couting all words, type 1; for giving the top words, type 2; for searching for a term, type 3:\n")
        print "\n"
        if which == "1":
            specify = raw_input("Type 1 for occurences, 2 for frequencies")
            print "\n"
            if specify == "1":
                print "Here you go, all the unique words: \n"
                print CountWord('alice_in_wonderland.txt')
                print "\n"
            else:
                print "Here you go, all the unique words: \n"
                print AllFrequencies('alice_in_wonderland.txt')
                print "\n"
        elif which == "2":
            how_many = int(raw_input("A top list of how many words?:"))
            print "\n"
            printAlice(how_many)
            print "{}. Total Unique Words: {}".format(how_many+1, len(CountWord('alice_in_wonderland.txt')))
            print "{}. Total Words: {}".format(how_many+2, GetTotal('alice_in_wonderland.txt'))
            print "\n"*2
        elif which == "3":
            print "\n"
            term = raw_input("What term would you like to find?: ")
            print "\n"
            print SearchWord('alice_in_wonderland.txt', term)
            print "\n"
        else:
            break
Alice()

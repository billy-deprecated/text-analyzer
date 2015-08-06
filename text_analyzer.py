#Analyzes a body of text.

def EliminatePunctuation(text):
    #eliminates punctuation from a string
    puncuation = [",", ".", "!", "?", "(", ")", "-", "/", "\"", ";"]
    new_text = text
    for point in puncuation:
        new_text = new_text.replace(point, "")
    return new_text

def OpenBook(file_name):
    #converts text file into a string
    with open(file_name) as book:
        text = book.read()
    return text

def GetUniqueWords(text):
    #returns list of all the unique words in a string
    new_text = EliminatePunctuation(text)
    all_words = new_text.split()
    unique_words = []
    for word in all_words:
        lower_word = word.lower()
        if lower_word not in unique_words:
            unique_words.append(lower_word)
    return unique_words

def CountWord(file_name):
    #returns dictionary of each unique word defined by how many times it occurs
    text = OpenBook(file_name)
    new_text = EliminatePunctuation(text)
    all_words = new_text.split()
    hashmap = {}
    unique_words = GetUniqueWords(text)
    for word in unique_words:
        hashmap.update({word: 0}) #hashmap[word] = 0
    for word in all_words:
        lower_word = word.lower()
        hashmap[lower_word] = hashmap[lower_word] + 1
    return hashmap

def Getoccurrences(multi_list):
    #given a multidimensional list, returns the second term in each list element
    #used to return the occurrences in a list that shows [[word, occurrences]]
    numbers = []
    length = len(multi_list)
    for i in range(length):
        numbers.append(multi_list[i][1])
    return numbers

def SortList(multi_list):
    #sorts a multi-dimensional list, i.e [[string, int], [string, int]]
    length = len(multi_list)
    for i in range(length -1, 0, -1):
        for j in range(1, i+1):
            if multi_list[j-1][1] > multi_list[j][1]:
                temp =  multi_list[j-1]
                multi_list[j-1] = multi_list[j]
                multi_list[j] = temp
    return multi_list


def GetTotal(file_name):
    #returns total number of words in a text file
    text = OpenBook(file_name)
    all_words = text.split()
    return len(all_words)


def TopList(file_name, top_number):
    #returns a list of the (top_number) most used words in a text file
    #list is in this format: [[word1, occurrences1], [word2, occurrences2]]
    hashmap = CountWord(file_name)
    greatest_list = [['', 0]] * top_number  #['', 0] for x in range(top_number)
    count = 0
    for word in hashmap:
        occurrences = hashmap[word]
        if count < top_number:
            greatest_list[count][0] = word
            greatest_list[count][1] = occurrences
        else:
            numbers = Getoccurrences(greatest_list)
            smallest = min(numbers)
            smallest_index = numbers.index(smallest)
            if occurrences > smallest:
                del greatest_list[smallest_index]
                greatest_list.append([word, occurrences])
        count += 1
    SortList(greatest_list)
    greatest_list.append(['TOTAL UNIQUE WORDS', count])
    greatest_list.append(['TOTAL WORDS', GetTotal(file_name)])
    return greatest_list

def AllFrequencies(file_name):
    #returns dictionary of each unique word's frequency
    hashmap = CountWord(file_name)
    new_hash = {}
    total = float(GetTotal(file_name))
    for word in hashmap:
        freq = hashmap[word]/total
        new_hash.update({word: freq})
    return new_hash


def TopFrequencies(file_name, top_number):
    #returns a multi dimensional list of the top frequencies
    greatest_list = TopList(file_name, top_number)
    freq_list = []
    total = float(GetTotal(file_name))
    for index in range(top_number):
        freq = (greatest_list[index][1]/total)*100
        new = greatest_list[index]
        new[1] = freq
        freq_list.append(new)
    return freq_list



def MergeTop(top_list, freq_list):
    #returns a multi dimensional list of the top occurrences and frequencies
    length = len(top_list) - 2 #The last two elements are total unique, and total words (not needed)
    both = []
    for index in range(length):
        new = top_list[index]
        freq = str(freq_list[index][1]) + "%"
        new.append(freq)
        both.append(new)
    return both

def PrintList(multi_list):
    #prints a formatted top list of occurrences and frequencies
    length = len(multi_list)
    multi_list.reverse()
    top = ""
    for index in range(length):
        word = multi_list[index][0]
        occurrences = multi_list[index][1]
        freq = multi_list[index][2]
        top += "{}. {}: {} occurrences, {} of total words \n".format(index+1, word, occurrences, freq)
    print top

def SearchWord(file_name, term):
    #searches for any single term in a file and returns how many times it occurs
    hashmap = CountWord(file_name)
    term = term.lower()
    if term not in hashmap:
        return "Actually, {} does not appear at all".format(term)
    else:
        return "{} appears {} times.".format(term, hashmap[term])

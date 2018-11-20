def main():
    # filename = input('Enter the name of the file:')
    filename = "trees"
    
    #make all uppercase
    temp=open('temp.txt', 'w+')
    names=open((filename+'.txt'),'r')
    temp.write(names.read().upper())

    #remove apostrophes
    abbrev=open('names_abbrev.txt', 'w+')
    temp=open('temp.txt', 'r')
    abbrev.write(temp.read().replace("'",""))

    #remove '\n' with ',' to easily turn into a list later
    temp=open('temp.txt', 'w+')
    abbrev=open('names_abbrev.txt', 'r')
    temp.write(abbrev.read().replace('\n',',').replace(' ',''))

    #remove all other non-letter characters and replace with space
    import re
    abbrev=open('names_abbrev.txt', 'w+')
    temp=open('temp.txt', 'r')
    abbrev.write(re.sub(r'[^a-zA-Z,]','',temp.read()))

    #turn text into list of words
    abbrev=open('names_abbrev.txt', 'r')
    wlist = abbrev.read().split(',')
    #remove last comma
    wlist=wlist[:-1]
    #print(wlist)
    abbreviations = abbrev_list(wlist)
    print(abbreviations)
    #print(abbreviations)
    without_repeats=remove_repeats(abbreviations)
    # print(without_repeats)
    
#abbrev_dict creates the dictionary 'd' with names from wlist as keys and
#all possible abbreviations as values
def abbrev_list(list_of_words):
    abbrev_list = list()
      
    for i in range(0,len(list_of_words)):
        f=list_of_words[i][0]
        for j in range(1,(len(list_of_words[i])-1)):
            s=list_of_words [i][j]
            for k in range(j+1,len(list_of_words[i])):
                t=list_of_words [i][k]
                abbrev_list.append(f+s+t)

    return abbrev_list

'''def abbrev_dict(list_of_words):
    abbrev_dict = {}
  
    for i in range(0,len(list_of_words)):
        f=list_of_words[i][0]
        for j in range(1,(len(list_of_words[i])-1)):
            s=list_of_words [i][j]
            for k in range(j+1,len(list_of_words[i])):
                t=list_of_words [i][k]
                abbrev_dict.setdefault(list_of_words[i], []).append(f+s+t)

    return abbrev_dict

def remove_repeats(dictionary):
    print(dictionary)
    print("==================================================")
    updatedDictionary = dict()
    for key, value in dictionary.items():
        updatedAbbreviation = set(value)
        updatedAbbreviation = list(updatedAbbreviation)
        updatedDictionary[key] = updatedAbbreviation
    print(updatedDictionary)    
    # s=set(dictionary.values())
    return updatedDictionary'''

if __name__ == "__main__":
    main()
    
 #a=['anna','sasha']
 #b=[['marek'],['tar']]
 #dictionary=dict(zip(a,b))
#>>> list_of_words={}
#>>> list_of_words.setdefault('ALDER', []).append('ALD')
#>>> print(list_of_words)
#{'ALDER': ['ALD']}

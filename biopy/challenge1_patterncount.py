
bioText = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
bioPattern = "TGT"

def PatternCount(pat, txt):
    count = 0
    for i in range(0,len(txt)-len(pat)+1):
        #print txt[i:i+len(pat)]
        if pat==txt[i:i+len(pat)] :
            count+=1
    return count


def FrequentWords(Text, k):
    FrequentPatterns = set()
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.add(Text[i:i+k])
    return FrequentPatterns

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count
           
           
def reverseComplement(dnatxt):
    rev = ""
    c=''
    strand = dnatxt.upper()
    for n in strand[::-1]:
        if  n == 'A': 
            c = 'T'
        elif n == 'T':
            c = 'A'
        elif n == 'G':
            c = 'C'
        elif n == 'C':
            c = 'G'
        else :
            c = '-'
        rev += str(c)
    return rev




FrequentWords("GATCCAGATCCCCATAC", 2)
print PatternCount(bioPattern, bioText)
print reverseComplement("GCTAGCT")
exit

import os.path
with open(os.path.normpath("C:\Users\IBM_ADMIN\Downloads\lol.txt")) as f:
    lines = f.read().splitlines() 
    
print (lines[0])
print "===================="
print reverseComplement(lines[0])

bioText = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k=10
bioPattern = "TGT"

def PatternCount(pat, txt):
    count = 0
    for i in range(0,len(txt)-len(pat)+1):
        #print txt[i:i+len(pat)]
        if pat==txt[i:i+len(pat)] :
            count+=1
    return count

def PatternCount2(pat, txt):
    count = 0
    positions = []
    for i in range(0,len(txt)-len(pat)+1):
        #print txt[i:i+len(pat)]
        if pat==txt[i:i+len(pat)] :
            count+=1
            positions.append(i)
    return positions

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
           
           
def ReverseComplement(dnatxt):
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


def SymbolArray(Genome, symbol):
    n = len(Genome)
    array = {}
    ExtendedGenome = Genome + Genome[0:n//2]
    print ExtendedGenome
    array[0] = PatternCount(symbol, ExtendedGenome[0:n//2] )
    for i in range( 1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1]==symbol:
            array[i] -= 1
        if ExtendedGenome[i+n//2]==symbol:
            array[i] += 1
        
    return array
    

def Skew(Genome):
    s = {}
    s[0]=0
    for i in range(1,len(Genome)+1):
        if Genome[i-1]=="G":
            s[i] = s[i-1]+1
        elif Genome[i-1]=="C":
            s[i] = s[i-1]-1
        else:
            s[i] = s[i-1]
    return s

def MinimumSkew(Genome):
    s = Skew(Genome)
    m = s.get(min(s, key=s.get))
    minarray = []
    for k in s:
        if s[k]==m:
            minarray.append(k)
    return minarray

    
def HammingDistance(p, q):
    if len(p)!=len(q):
        return -1
    dist = 0
    for i in range(0, len(p)):
        if p[i]!=q[i]:
            dist += 1
    return dist


def ApproximatePatternCount(pat, txt, distance):
    count = 0
    positions = []
    for i in range(0,len(txt)-len(pat)+1):
        #print txt[i:i+len(pat)]
        if HammingDistance(pat, txt[i:i+len(pat)])<=distance :
            count+=1
            positions.append(i)
    return positions

def ApproximatePatternMatching(pat, txt, distance):
    count = 0
    positions = []
    for i in range(0,len(txt)-len(pat)+1):
        #print txt[i:i+len(pat)]
        if HammingDistance(pat, txt[i:i+len(pat)])<=distance :
            count+=1
            positions.append(i)
    return len(positions)

print (HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))
print ApproximatePatternMatching("GAGG", "TTTAGAGCCTTCAGAGG", 2)
print ReverseComplement("TTATCCACA")
print ReverseComplement("GGATCCTGG")
print ReverseComplement("GATCCCAGC")

#print MinimumSkew("CCATGGGCATCGGCCATACGC")
#print SymbolArray("AAAAGGGG", "A")
#print FrequentWords(bioText, 10)
#print PatternCount(bioPattern, bioText)
#print reverseComplement("GCTAGCT")
import sys
sys.exit(0)





#import os.path
#with open(os.path.normpath("C:\Users\IBM_ADMIN\Downloads\lol.txt")) as f:
#    lines = f.read().splitlines() 
    

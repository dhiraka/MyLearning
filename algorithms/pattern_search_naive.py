# Python program for Naive Pattern Searching
def search(pat, txt):
    pattern_len = len(pat)
    txt_len = len(txt)
 
    # A loop to slide pat[] one by one
    for i in xrange(txt_len-pattern_len+1):
        # For current index i, check for pattern match
        for j in xrange(pattern_len):
            if txt[i+j] != pat[j]:
                break
        if j == pattern_len-1: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)
 
# Driver program to test the above function
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search (pat, txt)
class Solution(object):
    def sortSentence(self, s):
        store = s.split()
        string = []
        for i in range(1,len(store)+1):
            for j in range(len(store)):
                if i == int(store[j][-1]):
                    string.append(store[j])
                    break
        
        for j in string:
            index = int(j[-1]) - 1
            string[index] = j[:-1]
        return " ".join(string)
            
                
        
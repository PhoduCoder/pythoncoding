#Maximum words in sentence

#A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#Return the maximum number of words that appear in a single sentence.

class Solution:
    def findCount(self, sentence: str)  -> int:
        return len(sentence.split(' '))
    
    def mostWordsFound(self, sentences: List[str]) -> int:
        sen_word_count=[]
        for i in range(len(sentences)):
            #print (sentences[i])
            words_list=self.findCount(sentences[i])
            print (words_list)
            sen_word_count.append(words_list)
        #print (send_word_count)
        return max(sen_word_count)


from nltk import bigrams
from nltk.probability import ELEProbDist, FreqDist
from nltk import NaiveBayesClassifier

import csv
import string
import nltk

import nltk
from nltk.tokenize import word_tokenize

newline="\n"
fp=open("positive-words.txt","r+")
pos1 = fp.read()
pos=word_tokenize(pos1)
positive=[]
for i in range(1000):
 positive.append([])
 positive[i].append(pos[i])
 positive[i].append("positive")
#print positive

fn=open("negative-words.txt","r+")
neg1 = fn.read()
neg=word_tokenize(neg1)
negative=[]
for i in range(1000):
 negative.append([])
 negative[i].append(neg[i])
 negative[i].append("negative")
#print negative
#print newline
comments = []
for (words, sentiment) in positive + negative:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    comments.append((words_filtered, sentiment))
#print comments
#print newline


def get_words_in_comments(comments):
    all_words = []
    for (words, sentiment) in comments:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words_in_comments(comments))

#print word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, comments)
#print newline
#print training_set

classifier = nltk.NaiveBayesClassifier.train(training_set)
#print newline
#print classifier



def train(labeled_featuresets, estimator=ELEProbDist):
    label_probdist = estimator(label_freqdist)
    feature_probdist = {}
    return NaiveBayesClassifier(label_probdist, feature_probdist)

#print label_probdist.prob('positive')
#print label_probdist.prob('negative')

#print feature_probdist
#print feature_probdist[('negative', 'contains(best)')].prob(True)

#print classifier.show_most_informative_features(32)
 
new="\n\n"

output = open("statistics.csv", "wb")
writer = csv.writer(output)
Customer_id=[]
label=[]

Customer_id.append("Customer_id")
label.append("positive/negative")

for i in range(19):
    filename = '12%d.txt'%(i,)
    f=open(filename,"r")
    comment=f.read()
    comment= string.replace(comment, '.', ' .')
    print classifier.classify(extract_features(comment.split()))
    t1=classifier.classify(extract_features(comment.split()))
    print comment
    if (t1=="positive"):
      flag=1
    else:
      flag=0
    Customer_id.append(i+1)
    label.append(flag)

print Customer_id
print label
stat=[]

print i

for j in range(i+2):
  stat.append([])
  stat[j].append(Customer_id[j])
  stat[j].append(label[j])
 
print stat

writer.writerows(stat)

    
     

 



   



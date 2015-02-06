import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import bigrams
from nltk.probability import ELEProbDist, FreqDist
from nltk import NaiveBayesClassifier
 

newline="\n"

fp=open("catering.txt","r+")
cater=word_tokenize(fp.read())
catering=[]
for i in range(1142):
  catering.append([])
  catering[i].append(cater[i])
  catering[i].append("catering")

fp=open("music.txt","r+")
mus=word_tokenize(fp.read())
music=[]
for i in range(6):
  music.append([])
  music[i].append(mus[i])
  music[i].append("music")

fp=open("seating.txt","r+")
seat=word_tokenize(fp.read())
seats=[]
for i in range(6):
  seats.append([])
  seats[i].append(seat[i])
  seats[i].append("seating")

print catering
print newline
print music
print newline

comments = []
for (words, sentiment) in catering + music + seats:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    comments.append((words_filtered, sentiment))
print comments
print newline


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
print newline
print training_set

classifier = nltk.NaiveBayesClassifier.train(training_set)
print newline
print classifier



def train(labeled_featuresets, estimator=ELEProbDist):
    label_probdist = estimator(label_freqdist)
    feature_probdist = {}
    return NaiveBayesClassifier(label_probdist, feature_probdist)

#print label_probdist.prob('catering')
#print label_probdist.prob('music')

#print feature_probdist
#print feature_probdist[('music', 'contains(best)')].prob(True)

print classifier.show_most_informative_features(32)


comment="the chicken is good. Music is bad. seats are bad. The salt is not tasty ."
comment=sent_tokenize(comment)

seat_lab=[]
cater_lab=[]
music_lab=[]

for a in comment:
  print a
  print classifier.classify(extract_features((a.lower()).split()))
  label=classifier.classify(extract_features((a.lower()).split()))
  if (str(label)=="seating"):
    seat_lab.append(a)
  if (str(label)=="catering"):
    cater_lab.append(a)
  if (str(label)=="music"):
    music_lab.append(a)

print "seating comments"
print seat_lab

print "music comments"
print music_lab

print "catering comments"
print cater_lab
# Spam Detection in SMS using SVM
'''
To implement data preprocessing (SVM for SMS spam detection)

Authors: Abinaya M (MT2012007), Vika Verma (MT2012162)
'''

#!/usr/bin/python
import re
from sklearn import preprocessing
import numpy as np
import csv
import pylab as pl


# Function to return the frequency of occurance of words in the specified file
def readData(filename):

        wordFrequency = {}
        words = []

	# Open the file to read the words
        fopen = open(filename,"r")
        p = re.compile('[ |\n|\t]+')
        lines = fopen.read().lower()
        fopen.close()
        rawWords = p.split(lines)
        #print len(words)

        # Pre-process the words
        for word in rawWords:
                words.append(word.rstrip('.|!|?|;|,'))

        # Words contain the dictionary of words along with its frequency
        wordFrequency = frequency(words)
        return wordFrequency
        

# Function to return the frequency of words in a list
def frequency(words):

        frequencyDict = {}
        count = 1

        # Add the words to dictionary along with its occurance
        for word in words:
                if word not in frequencyDict:
                    frequencyDict[word] = count
                else:
                        frequencyDict[word] += 1
        return frequencyDict
	#print words


# Function to return the top occuring words in the dictionary and writes it into a file
def topWords(tokens, fileOpen):
        keys = {}
        counter = 500
        for a,b in sorted(tokens.iteritems(), key=lambda item: -item[1]):
                if counter > 0:
                        print str(a),str(b)+"\n"
                        fileOpen.write(str(a)+ " " + str(b)+"\n")
                        counter-=1
                        keys[a] = b
        fileOpen.close()
        return keys
        

# Function to find the feature vector
def features(hamTokens,spamTokens,fileOpen):
        hamKeys = hamTokens.keys()
        spamKeys = spamTokens.keys()
        #print hamKeys
        #print spamKeys
        #featureVector = [i for i, j in zip(hamKeys, spamKeys) if i != j]
        featureVector = hamKeys + spamKeys
        print featureVector
        for features in featureVector:
                fileOpen.write(str(features)+"\n")
        fileOpen.close()
        return featureVector
        
# Function related to ham messages
def ham():
        hamFile = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\ham.txt";
        fileOpen = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\hamStatistics.txt","w")
        hamTokens = {}
        hamTokens = readData(hamFile)
        topHamTokens = topWords(hamTokens,fileOpen)
        fileOpen.close()
        return topHamTokens
        
        #with fileOpen as handle:
                #pickle.dump(topHamTokens, handle)

# Function related to spam messages
def spam():
        spamFile = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\spam.txt";
        fileOpen = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\spamStatistics.txt","w")
        spamTokens = {}
        spamTokens = readData(spamFile)
        topSpamTokens = topWords(spamTokens, fileOpen)
        fileOpen.close()
        return topSpamTokens


# Function related to the data set
def dataSet():
        dataFile = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\SMSSpamCollection";
        fileOpen = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\dataSetStatistics.txt","w")
        totalTokens = {}
        totalTokens = readData(dataFile)
        topTotalTokens = topWords(totalTokens, fileOpen)
        fileOpen.close()
        return topTotalTokens


# Function related to input conversion to matrix
def inputConversion(featureVector, fileName):
        # Open the file to read the words
        X = []
        finalInput = []
        fopen = open(fileName,"r")
        corpus = fopen.read().split('\n')
        fopen.close()
        p = re.compile('[ ]+')

        # Conversion of input text to array of words
        for lines in corpus:
                inputs = []
                string = lines.lower()
                words = p.split(string)
                for word in words:
                        inputs.append(word.rstrip('.|!|?|;|,'))
                X.append(inputs)
        

        # Comparing the input vector and the feature vector
        finalInput = [ [ (1 if entry in features else 0) for entry in featureVector ] for features in X ]
        return finalInput


# Function to convert the output token to 1 and 0
# Spam - 1 ham - 0
def convert():
        outputFile = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\SMSSpamCollection"
        output = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\output.txt", "w")
        tokens = []
        fileOpen = open(outputFile, "r");
        lines = fileOpen.readlines()
        for line in lines:
            tokens.append(line[:max(line.find('\t'), 0) or None])
        #tokens = fileOpen.read().split('\n');
        fileOpen.close()
        #print tokens
        for token in tokens:
                if token == 'ham':
                        token = 0
                        output.write(str(token)+"\n")
                elif token == 'spam':
                        token = 1
                        output.write(str(token)+"\n")
        output.close()
        tokens = readOutput()
        return tokens

# Function to read from the output file
def readOutput():
        outputFile = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\output.txt","r")
        output = outputFile.read().split('\n')
        result = []
        output = output[:-1]
        outputFile.close()
        for i in output:
            result.append(int(i))
        return result
              

    
# Main module
# Call to all the relevant functions

# Ham
print "Statistics related to HAM Messages:\n"
hamDict = ham()

# Spam
print "Statistics related to SPAM Messages:\n"
spamDict = spam()

# Data set
print "Statistics related to the Data Set:\n"
dtaDict = dataSet()

# Output conversion
print "Output conversion is done!\n"
output = convert()
#print len(output)


# Feature selection
print "The features are :\n"
fileOpen = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\outputFeature.txt","w")
featureVector = features(hamDict,spamDict,fileOpen)
#print featureVector

# Input conversion
# For the total file
fileName = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\SMSSpamCollectionFull.txt"
totalInput = inputConversion(featureVector, fileName)
# For the ham messages
fileName = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\hamFull.txt"
hamInput = inputConversion(featureVector, fileName)
# For the spam messages
fileName = "C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\spamFull.txt"
spamInput = inputConversion(featureVector, fileName)
print "\n\nThe input is converted to matrix!!"
#print X

# Write the input and output to a file
fileInput = open("C:\Personal\IIITB\Third Semester\Machine Learning\Project\Data Set\inputWeka.csv","w")
with fileInput as f:
    writer = csv.writer(f)
    writer.writerows(totalInput)
    



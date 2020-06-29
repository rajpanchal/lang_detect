import numpy as np
import pandas as pd
import csv

def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word) #helpful
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec +str(0)*26*excess
        new_list.append(vec)
    print(len(new_list))
    return new_list

def create_output_vector(tag_index, number_of_languages):
    out = str(0)*tag_index + str(1) + str(0)*(number_of_languages-1-tag_index)
    return out
en=[]
fr=[]
cs=[]
de=[]
sv=[]
tags=[
    ['en',en],
    ['fr',fr],
    ['cs',cs],
    ['de',de],
    ['sv',sv]]
max_letters = 12
with open('en.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
    
for i in range(len(your_list)):
    en.append(your_list[i][0])

with open('fr.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
    
for i in range(len(your_list)):
    fr.append(your_list[i][0])

with open('cs.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
    
for i in range(len(your_list)):
    cs.append(your_list[i][0])

with open('de.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
    
for i in range(len(your_list)):
    de.append(your_list[i][0])

with open('sv.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
    
for i in range(len(your_list)):
    sv.append(your_list[i][0])
               
word_data = []
language_data = []
master_dic = []


for i in range(5):
    tag = tags[i][0]
    dic = tags[i][1]
    print('generating dictionary for ' + tag)
    #dic = functions.generate_dictionary(tag, max_letters)
    #print(dic)
    #print(len(dic))
    #dic = np.array(dic)
    #df=pd.DataFrame(dic)
    #name = tag+'.csv'
    #df.to_csv(name)
    count=12
    for word in dic:
        master_dic.append(word)
    vct = convert_dic_to_vector(dic, max_letters)
    for vector in vct:
        word_data.append(vector)
    output_vct = create_output_vector(count, len(tags))
    for i in range(len(vct)):
        language_data.append(output_vct)

arr = []
for i in range(len(word_data)):
    entry = []
    entry.append(master_dic[i])   # word : output_vec : word_data
    for digit in language_data[i]:
        entry.append(float(digit))
    for digit in word_data[i]:
        entry.append(float(digit))
    arr.append(entry)


arr = np.array(arr)
np.save('arr.npy', arr)
df=pd.DataFrame(arr)
df.to_csv('data.csv')

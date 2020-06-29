from keras.models import Sequential
from keras.layers import Dense
import numpy as np

max_letters = 12

def convert_dic_to_vector(lst, max_word_length):
    new_list = []
    for item in lst:
        vec = ''
        n = len(item)
        for x in range(n):
            current_letter = item[x]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec + str(0)*26*excess
        new_list.append(vec)
    # print(len(new_list))
    return new_list


network = Sequential()
network.add(Dense(200, input_dim=26*max_letters, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(5, activation='softmax'))
network.load_weights('weights.hdf5')
network.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

while True:
    dic = []
    valid = False
    while not valid:
        word = input('Enter word to predict:\n')
        if len(word) <= max_letters:
            word = word.lower()
            valid = True
        else:
            print('Word must be less than 12 letters long')
    dic.append(word)
    vct_str = convert_dic_to_vector(dic, max_letters)
    vct = np.zeros((1, 26 * max_letters))
    count = 0
    for digit in vct_str[0]:
        vct[0,count] = int(digit)
        count += 1
    prediction_vct = network.predict(vct)

    langs = ['en','cs','fr','de','sv']
    for i in range(5):
        lang = langs[i]
        score = prediction_vct[0][i]
        print(lang + ': ' + str(round(100*score, 2)) + '%')
    print('\n')



en -> ENGLISH
fr -> FRENCH
cs -> CZECH
de -> GERMAN
sv -> SWEDISHw
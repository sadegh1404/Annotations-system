#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import hazm

import pandas as pd 

dt = pd.read_csv('world.csv')

sent = dt['title'][0].decode('utf-8')


def write_utf(content,mode='a',file_name='def.txt'):
    import codecs
    f = codecs.open('output/'+file_name,mode,'utf-8')
    f.write(content+'\n')
    f.close()
    


res = hazm.sent_tokenize(sent)
for i in res:
    write_utf(i,mode='w',file_name='tokenize')


words = hazm.word_tokenize(sent)
for i in words:
    write_utf(i,file_name='words.txt')

tagger = hazm.POSTagger(model='resources/postagger.model')
for i in tagger.tag(words):
	write_utf(i[0]+'  '+i[1],file_name='postagger.txt')

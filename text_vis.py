#!/usr/bin/env python2

from wordcloud import WordCloud
import fileinput
from PIL import Image
import os
from os.path import join, getsize
import sys
import re

corpus_text = ""
for root, dirs, files in os.walk(sys.argv[1]):
  for fn in files:
    with open(os.path.join(root, fn),"r") as f:
      text = ""
      for l in f.readlines():
        text = text + l
      if text:
        try:
          wordcloud = WordCloud().generate(text)
          wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
          wordcloud.to_file(os.path.join(sys.argv[2], \
            root.replace("/","-") + '-' + fn + "-wordcloud.png"))
          corpus_text = corpus_text + text
        except:
          pass

if corpus_text:
  try:
    wordcloud = WordCloud().generate(corpus_text)
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(corpus_text)
    wordcloud.to_file(os.path.join(sys.argv[2], "ALL-wordcloud.png"))
  except:
    pass

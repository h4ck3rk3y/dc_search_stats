#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

with open('log.csv') as log:
	words = []
	for line in log:
		word = line[line.rfind(":")+1:]
		words.append(word)


	# Read the whole text.
	text = ' '.join(words)
	print text
	# Generate a word cloud image
	wordcloud = WordCloud().generate(text)

	# Display the generated image:
	# the matplotlib way:
	import matplotlib.pyplot as plt
	plt.imshow(wordcloud)
	plt.axis("off")

	# lower max_font_size
	wordcloud = WordCloud(max_font_size=40).generate(text)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

	# The pil way (if you don't have matplotlib)
	#image = wordcloud.to_image()
	#image.show()
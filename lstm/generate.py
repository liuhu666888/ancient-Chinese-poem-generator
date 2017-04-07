#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import *
import os
import argparse
import json

def main():
	parser = argparse.ArgumentParser(description='Ancient Chinese poetry generator.')
	parser.add_argument('-p','--prime',type = str,help = "Initial Chinese characters for each sentence.",default = "")
	parser.add_argument('-s','--sentence',type = str,help = "First sentence for the poem.",default = "")
	parser.add_argument('-v','--voc',type = str,help = "Vocabulary file path.",default = "../model/weights/vocabulary.json")
	parser.add_argument('-m','--model',type = str,help = "Model weights to be loaded.",default = "../model/weights/weights-improvement-29-5.1411-1.hdf5")

	args = parser.parse_args()

	# check
	if args.prime != '' and args.sentence != '' and args.sentence[0] != args.prime[0]:
		print("First character should be same!")
		return

	voc_t = open(args.voc,'r',encoding = 'utf-8')
	[voc,voc_count] = json.loads(voc_t.read())
	voc_t.close()

	char_to_int = dict((c, i) for i, c in enumerate(voc))
	int_to_char = dict((i, c) for i, c in enumerate(voc))

	fs = ''
	if args.sentence == '':
		fs = first_sentence(args.prime)
	else:
		fs = args.sentence

	p = generate(args.model,char_to_int,int_to_char,args.prime,args.sentence)

	for s in p:
		print(s)


if __name__ == "__main__":
	main()
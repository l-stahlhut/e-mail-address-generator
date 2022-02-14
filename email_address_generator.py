#!usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Laura Stahlhut
# Date: 12.11.2021


import re
import sys


def normalize(name):
	# function to normalize umlauts and accents
	d_umlaut = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ë': 'e', 'é': 'e'}

	for letter in name:
		for k, v in d_umlaut.items():
			if letter == k:
				name = re.sub(k, v, name)   # replace dictionary keys with dictionary values if a dictionary key is found in the name

	return name


def get_consonants(name):
	# function to return just the consonants in a given name
	consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

	for letter in name:
		if letter not in consonants:
			name = re.sub(letter, "", name)

	return name


def parse_name(name):
	# function to return first and last names and mail extension according to all rules
	name = normalize(name)  # take normalized name as input

	full_name = ' '.join(re.findall(r'^.+\t', name)) 			# delete domain from line; re.findall returns list with name --> convert to str
	last_name = ' '.join(re.findall(r'\w+\t$', full_name)) 		# take the last word
	first_name = ''.join(re.sub(r'\s\w+\t$', '', full_name))	# delete last name and domain
	first_name = ''.join(re.sub(r'\s', '', first_name))  		# delete space between first and middle name

	if len(first_name) > 8:
		first_name = get_consonants(first_name)   # apply consonants function if first name is too long

	extension = ''.join(re.findall(r'\w+$', name))

	if extension == "stu":
		domain = "@uzh.ch"
	elif extension == "NA":   # artificial extension I added in case the name is given as a string
		domain = "@uzh.ch"
	else:
		domain = "@" + extension + ".uzh.ch"

	return first_name, last_name, domain


def create_email_address(first_name, last_name, domain):

	address = first_name + "." + last_name.rstrip() + domain

	return address


def main():
	if ".txt" in sys.argv[1]: 		# this tests if the argument given in the command line is a txt-file
		with open(sys.argv[1], 'r') as f:
			names = f.readlines()

			for line in names:      # iterate over lines in txt-file
				email = line.lower()  #lowercase so Capital letters can be normalized too

				email = parse_name(email)
				email = create_email_address(email[0], email[1], email[2])
				print(line.rstrip() + "\t->\t" + email)
	else: 							# if the argument given on the command line is not a txt-file
		line = sys.argv[1]
		email = line.lower() + "\tNA"  # give the name an artificial 'domain' so that the parser works

		email = parse_name(email)
		email = create_email_address(email[0], email[1], email[2])
		print(line.rstrip() + "\t->\t" + email)


if __name__ == '__main__':
	main()


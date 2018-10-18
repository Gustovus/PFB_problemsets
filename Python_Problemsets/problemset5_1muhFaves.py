#!/usr/bin/env


muhfaves = {'book' : 'The Martian Chronicles', 'organism' : 'Sloth', 'artist' : 'Father John Misty', 'cat' : 'Archie', 'karaoke' : 'Dreams'}

str = input("For (book, artist, organism, cat or karaoke) which is my favest: ")

print("My favest", str, "is : ", muhfaves[str])

for key in muhfaves:
	print(key, muhfaves[key])

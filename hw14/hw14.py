import os
import re

def filesearch():
	files = os.listdir()
	latinfiles = []
	latindirs = []
	for file in files:
		fname = ''.join.file.split('.')[:-1]
		if not re.search('[^a-zA-Z]', fname):
                        if os.path.isdir(file):
                                if file not in latindirs:
                                        latindirs.append(file)
                                elif os.path.isfile(file):
                                        if file not in latinfiles:
                                                latinfiles.append(file)
	latin = []
	latin.append(latinfiles, latindirs)
	return latin

def main():
	results = filesearch()
	print('В этой папке найдено', len(results[0]) + len(results[1]), 'файлов и папок с названиями только из латиницы.')
	print(results[0], '\n', results[1])

main()

#вариант 4
# у меня не было доступа к своему компьютеру на этой неделе, поэтому код я писала по сути на бумажке и не смогла отладить.
# наверное, он даже не запускается. посмотрите его все равно, пожалуйста, может там хоть что-то правильно

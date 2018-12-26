import string
import sys
from urllib.request import urlopen
def wcount(lines, topn):
    text1 = lines.decode()
    for c in string.punctuation:
        text2 = text1.replace(c, " ")
    text3 = text2.split()
    text4 = list(set([(i,text3.count(i)) for i in text3 ]))
    text4.sort(key=lambda x: x[1],reverse = True)
    for i in text4[:topn-1]:
        print(i[0],"   ",i[1])

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    if len(sys.argv) == 2:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: {} of the txt file to analyze '.format(sys.argv[1]))
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        text = urlopen(sys.argv[1])
        text0 = text.read()
        text.close()
        wcount(text0, 10)


    if  3 <= len(sys.argv) <= len(text4) :
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: {} of the txt file to analyze '.format(sys.argv[1]))
        print('  topn: {}(words count) to output. If not given, will output top 10 words'.format(sys.argv[2]))
        text = urlopen(sys.argv[1])
        text0 = text.read()
        text.close()
        wcount(text0, int(sys.argv[2]))
    if len(sys.argv) > len(text4):
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: {} of the txt file to analyze '.format(sys.argv[1]))
        print('  topn: {}(words count) to output. If not given, will output top 10 words'.format(sys.argv[2]))
        text = urlopen(sys.argv[1])
        text0 = text.read()
        text.close()
        wcount(text0, len(text4))

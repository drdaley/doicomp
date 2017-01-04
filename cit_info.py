#printcitation info
import re
import os
regex = r"\{[^\}]*\}"
pattern = re.compile(regex)
def findvalue(l, iv, d, p):
  if l[:l.find(' ')] in iv:
    d[l[:l.find(' ')]] = p.search(l).group().strip('{}')

interesting_values = ('author','title','journal','pages','year','doi')
ci = dict()
filepath = input('What is the doi? ').split('/')
#print('..\literature\{0}\{1}\{1}_info.txt'.format(filepath[0],filepath[1]))
with open(r'..\literature\{0}\{1}\{1}_info.txt'.format(filepath[0],filepath[1])) as file:
#with open(r'C:\Users\DRD\literature_container\literature\10.1021\ja405354x\ja405354x_info.txt') as file:
  info = file.read().splitlines()
  for l in info:
    findvalue(l, interesting_values, ci, pattern)
#    if i.startswith('author'):
#      ci['author'] = pattern.search(i).group().strip('{}')#.encode('utf-8')
#    elif i.startswith('title'):
#      ci['title'] = pattern.search(i).group().strip('{}')#.encode('utf-8')
#      #print(ci['title'])
#    elif i.startswith('journal'):
#      ci['journal'] = pattern.search(i).group().strip('{}')     
#    elif i.startswith('page'):
#      ci['page'] = pattern.search(i).group().strip('{}')
#    elif i.startswith('year'):
#      ci['year'] = pattern.search(i).group().strip('{}')
#    elif i.startswith('doi'):
#      ci['doi'] = pattern.search(i).group().strip('{}')
#    else: pass
  print('{0} \n{1} \n{2} \n{3} \n{4} \n{5}'.format(ci['author'], ci['title'],ci['journal'],ci['pages'],ci['year'],ci['doi']))
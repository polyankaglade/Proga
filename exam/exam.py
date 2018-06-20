import re
import os
from collections import Counter
import zipfile

def get_files():
  file_list = []
  z = zipfile.ZipFile('news.zip', 'r')
  z.extractall()
  for filename in os.listdir('./news'):
    if filename.endswith('.xhtml'):
      file_list.append(filename)
  return file_list
 
def find_words(text):
  catch = re.findall('lex="([А-ЯЁ][а-яЁ\-]+?)"', text)
  return catch
 
def read_file(file_list):
  words_list = []
  dirname = './news'
  for filename in file_list:
    filepath = os.path.join(dirname, filename)
    with open(filepath, encoding='windows-1251') as f:
      text = f.read()
    catch = find_words(text)
    for i in catch:
      words_list.append(i)
  return words_list
 
def count_words(words_list):
  c = Counter(sorted(words_list))
  with open('result.csv','w', encoding='windows-1251') as f:
    for key,value in c.items():            
      result = '{}{:\t>2}\n'.format(key,value)
      f.write(result)
      print(result)
 
def main():
  count_words(read_file(get_files()))
 
if __name__ == '__main__':
  main()

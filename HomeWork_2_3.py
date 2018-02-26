import chardet
import json
from collections import Counter
import string


def word_top(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        s = data.decode(result['encoding'])
        movie = json.loads(s)
        list_temp = []
        for movie_item in movie["rss"]["channel"]["items"]:
            list_temp = list_temp + movie_item["description"].strip().split(' ')
            list_temp = list_temp + movie_item["title"].strip().split(' ')
        kol_str = 0
        frequencies = Counter(word.translate(string.punctuation) for word in list_temp)
        print("Файле:", filename, ', кодировка:', result['encoding'])
        for word, count in frequencies.most_common():
            if len(word) > 6:
                print(word, ' - ', count)
                kol_str += 1
                if kol_str == 6:
                    break
        print('-----------------------------------------------------------')


list_file = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.')
for file_name in list_file:
    word_top(file_name)

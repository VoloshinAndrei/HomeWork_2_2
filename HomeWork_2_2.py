import chardet
from collections import Counter
import string


def word_top(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        list_temp = s.strip().split(' ')
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


list_file = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']
print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.')
for file_name in list_file:
    word_top(file_name)

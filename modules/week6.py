import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class TextComparer:
    
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames= []
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.filenames is not None:
            return self.filenames
        raise StopIteration
        
    def download(self, url):
        r = requests.get(url)
        if r.status_code == 404:
            raise Exception('URL NOT FOUND')
        filename = './Files/' + url.split('/')[5]
        self.filenames.append(filename)
        with open(filename, 'wb') as f:
            f.write(r.content)
    
    def multi_download(self, workers=5):
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(self.download, self.url_list)
        
    def urllist_generator(self):
        yield self.url_list
        
    def avg_vowels(self, filename):
        vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowel_count= 0
        f = open(filename, 'r')
        for char in f.read():
            if char in vowel_list:
                vowel_count += 1
        return vowel_count
        
    def hardest_read(self, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, self.filenames)
        x = sorted(list(res))
        return x[-1]
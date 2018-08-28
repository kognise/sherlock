import sherlock

path   = input('Path to search: ')
string = input('Search for: ')

searcher = new sherlock.Sherlock(path, 10)
searcher.search(string)

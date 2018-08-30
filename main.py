import sherlock

path   = input('Path to search: ')
string = input('Search for: ')

searcher = sherlock.Sherlock(path, 4096)
searcher.start(string)

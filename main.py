import sherlock

path   = input('Path to search: ')
string = input('Search for: ')

searcher = sherlock.Sherlock(path, 2046)
searcher.start(string)

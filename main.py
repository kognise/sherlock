import sherlock
import independent

print('Sherlock on Python %s' % independent.version_full)
print('----------------------')

path   = independent.input('Path to search: ')
string = independent.input('Search for:     ')

# TODO: FIX ON PYTHON 2!!!
searcher = sherlock.Sherlock(path, 4096)
searcher.start(string)

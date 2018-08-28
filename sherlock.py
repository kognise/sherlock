import os
import time

class Sherlock():
    # Initialization function
    def __init__(this, search_path='', max_threads=1024, match_case=False, search_file_names=True, search_file_contents=True):
        this.unique_id    = this._get_unique_id()
        this.open_threads = 0

        this.search_path = search_path
        this.max_threads = max_threads

        this.match_case           = match_case
        this.search_file_names    = search_file_names
        this.search_file_contents = search_file_contents

    # Main functions
    def start(this):
        if (search_path == '' or max_threads <= 0 or (search_file_names == false and search_file_contents == false)):
            this.log('Nothing to do.')
            return
            
        if (not os.path.exists(search_path)):
            this.log('Search path doesn\'t exist.')
            return

        # Do things.

    def log(this, message):
        string = '[%s] %s' % (this._get_time(), message)
        file = open('sherlock-%s.log' % this.unique_id, 'a')
        file.write(string)
        file.close()
        print(string)

    # Helper functions
    def _get_unique_id(this):
        format_string = '%Y%m%d%H%M%S'
        output_string = time.strftime(format_string)

        return output_string

    def _get_time(this):
        format_string = '%H:%M:%S'
        output_string = time.strftime(format_string)

        return output_string

    def _file_get_contents(this, path):
        try:
            file = open(path, 'rb')
            contents = file.read()
            file.close()
        except:
            contents = ''

        return contents

    def _search_string(this, search_for, search_in):
        if not this.match_case:
            search_for = search_for.lower()
            search_in  = search_in.lower()

        return search_in.find(search_for) >= 0

    def _start_thread(this, function, arguments):
        thread = threading.Thread(target=_really_start_thread, args=(function, arguments))
        thread.start()

    def _really_start_thread(this, function, arguments):
        thread = threading.Thread(target=function, args=arguments)
        thread.start()
        this.open_threads += 1
        thread.join()
        this.open_threads -= 1
        print('[*] Thread done!')
        return

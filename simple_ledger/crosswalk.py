import os
import json


def main():
    a = Crosswalk()

    # a.crosswalk['Net'] = 'amount'
    # a.crosswalk['AcctNum'] = 'gl_account_number'
    # a.crosswalk['Date'] = 'effective_date'
    #
    # a.save_crosswalk('sample')

    xwalkfiles = a.list_crosswalks()
    print('Available crosswalks are: {}'.format(xwalkfiles))
    a.load_crosswalk(xwalkfiles[0])
    print('Crosswalks are {}'.format(a.crosswalk))



class Crosswalk:
    def __init__(self, filename=None):
        self.base_folder = os.path.abspath(os.path.dirname(__file__))
        self.crosswalks_path = os.path.join(self.base_folder, 'crosswalks')
        self.crosswalk = {}
        self.filename = filename
        if self.filename:
            self.load_crosswalk(self.filename)

    def list_crosswalks(self):
        folder_items = os.walk(self.crosswalks_path)
        filenames = [x for x in folder_items][0][-1]
        return [x.replace('.json', '') for x in filenames]

    def load_crosswalk(self, filename):
        self.filename = filename
        filepath = self.get_file_path(self.filename)
        if not os.path.isfile(filepath):
            print('Error: Crosswalk file named "{}" does not exist'.format(self.filename))
            return

        with open(filepath, 'r') as fin:
            self.crosswalk = json.load(fin)

        print('Loaded crosswalk file {}'.format(filepath))

    def save_crosswalk(self, filename):
        self.filename = filename
        filepath = self.get_file_path(self.filename)

        with open(filepath, 'w') as fout:
            json.dump(self.crosswalk, fout)

        print('crosswalk file saved at {}'.format(filepath))

    def get_file_path(self, filename):
        return os.path.join(self.crosswalks_path, filename + '.json')

if __name__ == '__main__':
    main()
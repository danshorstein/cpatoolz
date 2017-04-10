import os
import pandas as pd

FOLDER = 'data'
FILENAME = 'gl.csv'
COLUMNS = ['GL_Account', 'GL_Description', 'Amount']

class GeneralLedger():
    def __init__(self, folder=FOLDER, filename=FILENAME, columns=COLUMNS):
        base_folder = os.path.abspath(os.path.dirname(__file__))
        self.columns = columns
        self.filename = filename
        self.full_path = os.path.join(base_folder, folder)
        self.file_path = os.path.join(self.full_path, self.filename)

        if not os.path.exists(self.full_path) or not os.path.isdir(self.full_path):
            os.mkdir(self.full_path)

        if os.path.isfile(self.file_path):
            try:
                self.df = pd.read_csv(os.path.join(self.full_path, self.filename), index_col=0)

            except Exception as e:
                print('WARNING! Found gl file but could not load. {}. Creating empty gl.'.format(e))
                self.df = pd.DataFrame()
        else:
            self.df = pd.DataFrame()

    def __repr__(self):
        return str(self.df)

    def save(self):
        self.df.to_csv(self.file_path)

    def record(self, new_row):
        self.df = self.df.append(pd.DataFrame([new_row], columns=self.columns), ignore_index=True)


if __name__ == '__main__':
    gl = GeneralLedger()

    gl.record(['1010', 'Cash', 5000])
    gl.record(['2110', 'AP', -5000])

    print(gl)

    gl.save()

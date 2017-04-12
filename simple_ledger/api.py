# from simple_ledger.general_ledger import GeneralLedger
import pandas as pd
import os


class GeneralLedgerService:
    def __init__(self, user='sample_gl'):
        # TODO - for now the user is the filename of the csv. This should be updated if a database is implemented...
        self.user = user
        self.acct = 'Acct'  # TODO - update this to properly include the name of the account column
        self.net = 'Net'
        self.error = None

    def load_detail(self):
        base_folder = os.path.abspath(os.path.dirname(__file__))
        csv_path = os.path.join(base_folder, 'data', '{}.csv'.format(self.user))
        self.gl = pd.read_csv(csv_path)
        print('Loaded gl detail from {}'.format(csv_path))

    def summary(self):
        summary = pd.pivot_table(self.gl, values=self.net, index=self.acct, aggfunc='sum')
        return summary

    def validate(self):  # TODO - implement validations below
        # no null values
        # required columns exist
        # correct format in each column's data
        net_sum = round(self.gl[self.net].sum(), 2)
        if net_sum != 0:
            self.error = "GL detail doesn't net to 0! Balance is {}".format(net_sum)
        return self.error

    def filter_detail(self, acct_number=None, beginning_date=None, ending_date=None):
        pass

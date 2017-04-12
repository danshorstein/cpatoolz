# from simple_ledger.general_ledger import GeneralLedger
import pandas as pd
import os


class GeneralLedgerService:
    def __init__(self, user='sample_gl'):
        # TODO - for now the user is the filename of the csv. This should be updated if a database is implemented...
        self.fs_group = 'FS_Group'
        self.user = user
        self.acct_number = "AcctNum"
        self.acct_name = 'Acct'  # TODO - update this to properly include the name of the account column
        self.net = 'Net'
        self.validation = {'validation_issues': 0}
        self.base_folder = os.path.abspath(os.path.dirname(__file__))
        self.csv_path = os.path.join(self.base_folder, 'data', '{}.csv'.format(self.user))
        self.gl = pd.DataFrame()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.gl)

    def load_detail(self):
        self.gl = pd.read_csv(self.csv_path)
        print('Loaded gl detail from {}'.format(self.csv_path))

    def summary(self, beg_date = None, end_date = None):
        summary = pd.pivot_table(self.gl, values=self.net, index=[self.acct_number, self.acct_name], aggfunc='sum')
        return summary

    def fs_summary(self, beg_date = None, end_date = None):
        summary = pd.pivot_table(self.gl, values=self.net, index=self.fs_group, aggfunc='sum')
        return summary

    def validate(self):  # TODO - implement validations below
        # no null values
        # required columns exist
        # correct format in each column's data
        net_sum = round(self.gl[self.net].sum(), 2)
        if net_sum != 0:
            self.validation['validation_issues'] += 1
            self.validation['net_sum'] = net_sum

        return self.validation

    def filter_detail(self, acct_numbers=None, beginning_date=None, ending_date=None):
        pass

    def chart_of_accts(self):
        coa = self.gl[self.acct_name].unique()  # TODO - ADD ACCT NUMBER AND ACCT DESCRIPTION
        return coa

    def save_detail(self):
        self.gl.to_csv(self.csv_path)
        print('Saved file at {}'.format(self.csv_path))


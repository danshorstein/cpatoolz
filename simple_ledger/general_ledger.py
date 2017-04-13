import pandas as pd
import os


# TODO - big todo list; need to reformat structure
"""TODOs:
GL Detail
Order of actions by users:
1. Upload csv general ledger file (get info on fiscal year end, client name?)
** DO we want to retain original csv, plus save the crosswalked file as a new name? Save as json/pickel? **
2. Select or create mapping file to map columns to standardized columns
3. Validate data to ensure no issues (specific validations need to be designed/implemented
**Where should data cleanup happen? Separately before uploading? As part of this process??**
4. Display GL detail 

Options for displaying details:
1. Current year 

"""


class GeneralLedger:
    def __init__(self, filename='sample_gl', crosswalk=None):
        self.df = pd.DataFrame()
        self.fs_group = 'FS_Group'
        self.filename = filename
        self.acct_number = "AcctNum"
        self.acct_name = 'Acct'  # TODO - update this to properly include the name of the account column
        self.net = 'Net'
        self.date = 'Date'
        self.validation = {'validation_issues': 0}
        self.base_folder = os.path.abspath(os.path.dirname(__file__))
        self.csv_source_path = os.path.join(self.base_folder, 'source', '{}.csv'.format(self.filename))

        self._set_columns()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.df)

    def _set_columns(self):
        self.col_acct_number = self.df.get('gl_account_number')
        print(self.col_acct_number)

    def load_source_detail(self):
        self.df = pd.read_csv(self.csv_source_path)
        self.df[self.date] = self.df[self.date].apply(pd.to_datetime)
        print('Loaded gl detail from {}'.format(self.csv_source_path))

    def sum_by_gl_account(self, accounts=None, beginning_date=None, ending_date=None):
        filter_df = self.filter_detail(accounts=accounts, beginning_date=beginning_date, ending_date=ending_date)
        summary = pd.pivot_table(filter_df, values=self.net, index=[self.acct_number, self.acct_name], aggfunc='sum')
        return summary

    def sum_by_fs_grouping(self, beginning_date=None, ending_date=None):
        filter_df = self.filter_detail(beginning_date=beginning_date, ending_date=ending_date)
        summary = pd.pivot_table(filter_df, values=self.net, index=self.fs_group, aggfunc='sum')
        return summary

    def validate(self):  # TODO - implement validations below
        # no null values
        # required columns exist
        # correct format in each column's data
        net_sum = round(self.df[self.net].sum(), 2)
        if net_sum != 0:
            self.validation['validation_issues'] += 1
            self.validation['net_sum'] = net_sum

        return self.validation

    def filter_detail(self, accounts=None, beginning_date=None, ending_date=None):
        if not beginning_date:
            beginning_date = min(self.df[self.date])
        if not ending_date:
            ending_date = max(self.df[self.date])
        if not accounts:
            accounts = self.df[self.acct_number].unique()

        filter_df = self.df.where(
            self.df[self.acct_number].isin(accounts)
        ).where(
            self.df[self.date] >= beginning_date
        ).where(
            self.df[self.date] <= ending_date
        ).dropna()

        return filter_df

    def chart_of_accts(self):
        coa = self.df.groupby(by=[self.acct_number, self.acct_name]).max()  # TODO - ADD ACCT NUMBER AND ACCT DESCRIPTION
        return coa[self.fs_group]

    def save_detail(self):
        self.df.to_csv(self.csv_source_path, index=False)
        print('Saved file at {}'.format(self.csv_source_path))


import pandas as pd
from datetime import datetime

###########################################################################
# Implements a GeneralLedger class that inherits from pandas DataFrame    #
# Adds some custom methods and required elements in order to better       #
# Reflect a general ledger type of object                                 #
###########################################################################

#TODO - update below to reflect calculated beginning and ending based on current date
#TODO - determine if fiscal year and adjust appropriately?
#TODO - create methods with things like 'current fiscal year', 'prior fiscal year', that create beg/end parameters
#TODO - add required columns of acctname; fsgrouping, date, amount; maybe some preset options for fs grouping?
#TODO - add a trial_balance method to GeneralLedger that runs a trial balance for certain time period...
    #Question of whether


def main():
    gl = GeneralLedger(pd.read_csv(csv_path))
    print(gl)
    gl.info()


class GeneralLedger(pd.DataFrame):
    # Subclass from pandas DataFrame

    def __str__(self):
        str_df = GeneralLedger({'testing': [1, 2, 3], 'your mom': [4, 5, 7]})
        return u'MOTHER FUCKER!!!!!!!\n' + str_df.__unicode__()


if __name__ == '__main__':
    main()
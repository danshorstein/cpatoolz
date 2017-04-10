import pandas as pd
from datetime import datetime

#TODO - update below to reflect calculated beginning and ending based on current date
#TODO - determine if fiscal year and adjust appropriately?
#TODO - create methods with things like 'current fiscal year', 'prior fiscal year', that create beg/end parameters
START_OF_YEAR = datetime(2016, 1, 1)
END_OF_YEAR = datetime(2016, 12, 31)


def main():
    gl = GeneralLedger()
    print(gl)


class GeneralLedger(pd.DataFrame):
    # Subclass from pandas DataFrame

    def __str__(self):
        rep_df = GeneralLedger({'testing': [1, 2, 3], 'your mom': [4, 5, 7]})
        return rep_df.__unicode__()


if __name__ == '__main__':
    main()
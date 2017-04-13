from simple_ledger.general_ledger import GeneralLedger
from datetime import datetime


def main():
    beg_date = datetime(2018, 1, 15)
    end_date = datetime(2018, 5, 15)
    accts = [1000, 1010, 1200, 2000, 2110, 4000, 5010]

    gl = GeneralLedger()

    gl.load_source_detail()

    gl.validate()

    print('')
    print('Chart of accounts:')
    print(gl.chart_of_accts())

    # print('')
    # print('Filtered for accts: {}'.format(accts))
    # print(gl.filter_detail(accounts=accts))

    print('')
    print('Summarized for date range {} to {} and accts {}'.format(beg_date.date(), end_date.date(), accts))
    print(gl.sum_by_gl_account(accounts=accts, beginning_date=beg_date, ending_date=end_date))

    print('')
    print('Summarized FS grouping for range {} to {}'.format(beg_date.date(), end_date.date()))
    print(gl.sum_by_fs_grouping(beginning_date=beg_date, ending_date=end_date))

    print('')
    print('Dataframe info: ')
    gl.df.info()

if __name__ == '__main__':
    main()

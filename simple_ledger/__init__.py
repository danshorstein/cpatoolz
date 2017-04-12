from simple_ledger.api import GeneralLedgerService


def main():
    gl = GeneralLedgerService()

    gl.load_detail()

    gl.validate()

    print('Chart of accounts:')
    print(gl.chart_of_accts())

    print(gl)

    print('')
    print('Filtered for XXXXX')
    print(gl.filter_detail())

    print('')
    print('Summarized for date range XXXX - XXXX')
    print(gl.summary())

    print('')
    print('Summaried FS grouping for range XXXX - XXXX')
    print(gl.fs_summary())

if __name__ == '__main__':
    main()

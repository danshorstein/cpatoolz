from simple_ledger.api import GeneralLedgerService


def main():
    gl = GeneralLedgerService()

    gl.load_detail()

    errors = gl.validate()

    if errors:
        print('Errors: {}'.format(errors))

    print(gl.chart_of_accts())


if __name__ == '__main__':
    main()

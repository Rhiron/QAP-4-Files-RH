
def Format_Currency(Amount):
    return "${:,.2f}".format(Amount)

def Format_Phone_Num(Number):
    return "({}) {}-{}".format(Number[:3], Number[3:6], Number[6:])


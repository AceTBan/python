#
# import datetime
#
# dob = datetime.date(1998, 7, 22)
#
#
# def from_dob_to_age(born):
#     today = datetime.date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#
#
# print(from_dob_to_age(dob))


# def multiliper(nbr1, nbr2):
#     return nbr1 * nbr2
#
#
# a = multiliper(2, 3)
# print(a)


import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("OK")

    else:
        print("NOK")


if __name__ == '__main__':
    email = "kqfgkihq123@gmail.com"

    check(email)

    email = "monnsite@hotmail.org"
    check(email)

    email = "kqfgkihq123.com"
    check(email)
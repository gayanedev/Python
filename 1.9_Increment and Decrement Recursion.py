def inc(a):
    return a + 1
def dec(a):
    return a - 1


""" Recursion Example"""
# inc(add1(dec(4), 5)) հաշվելու համար նախ պետք է հաշվենք add1(3, 5)-ը սա հաշվելուց հետո պետք է վերադառնա
# ու increment անի,բայց դրա համար պետք է հաշվել add1(2, 5),հետո add1(1, 5) ու այսպես շարունակ
# մինչև հասնում ենք 0 արժեքին՝երբ a == 0
# այդտեղից սկսած հետաձգված գորցողությունները սկսում են կատարվել
def add1(a, b):
    if a == 0:
        return b
    else:
        return inc(add1(dec(a), b))


# a1 = int(input("Enter a first number: "))
# b1 = int(input("Enter a second number: "))
#
# print(add1(a1, b1))

""" Tail Recursion Example"""
# Ֆունկցիան սինտաքսիսով ռեկուրսիվ է,բայց չկան հետաձգված գործողություններ՝գործողությունը կատարվում է
# ռեկուրսիայի ամեն քայլի ժամանակ։ a-ի և b-ի արժեքները բավարար են արդյունքը հաշվելու համար
def add2(a, b):
    if a == 0:
        return b
    else:
        print(add2(dec(a), inc(b)))
        return add2(dec(a), inc(b))


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

print(add2(a, b))
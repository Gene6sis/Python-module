kata = (2019, 9, 25, 3, 30)

def fonc(x) :
    return ("{:02d}".format(x))

if __name__ == '__main__':
    print(f"{fonc(kata[1])}/{fonc(kata[2])}/{kata[0]} {fonc(kata[3])}:{fonc(kata[4])}")
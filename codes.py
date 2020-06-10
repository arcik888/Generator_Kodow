#!/usr/bin/python
# -*- coding: Windows-1250 -*-

class Arkusz:
    def __init__(self, len, wid, col):
        self.len = len # 800
        self.wid = wid
        self.col = col

    def lenght(self):
        #self.len = 1200 - treba przekazać 120
        leng = self.len
        return leng

    def width(self):
        widt = self.wid[:3]
        return widt

    def color(self):
        clr = self.col
        return clr

class ArkuszPiany(Arkusz):
    def __init__(self, len, wid, col, thick, dens, anti):
        super().__init__(len, wid, col)
        self.thick = thick
        self.dens = dens
        self.anti = anti

    def thickness(self):
        thi = self.thick
        if thi in range(1,99): return str(thi)
        else: return 0

    def density(self):
        dnst = self.dens
        densList = (16, 22, 24, 27, 35, 65, 100)
        if int(dnst) in densList: return dnst
        else: return 0

    def antistatic(self):
        ast = self.anti
        if ast.lower() == 't': return True
        else: return False

class ArkuszPianyPE(ArkuszPiany):
    def __init__(self, len, wid, col, thick, dens, anti, nopa, rec, skin):
        super().__init__(len, wid, col, thick, dens, anti)
        self.nopa = nopa
        self.rec = rec
        self.skin = skin

    def nopaplank(self):
        np = self.nopa
        if np.lower() == 't': return True
        else: return False

    def recycle(self):
        rc = self.rec
        return rc

    def with_skin(self):
        skn = self.skin
        if skn.lower() == 't': return True
        else: return False

def dens_letter(dens):
    if dens == '16': return 'D', str(dens) + 'kg/m3'
    elif dens == '22': return 'F', str(dens) + 'kg/m3'
    elif dens == '24': return 'L', str(dens) + 'kg/m3'
    elif dens == '27': return 'S', str(dens) + 'kg/m3'
    elif dens == '35': return 'M', str(dens) + 'kg/m3'
    elif dens == '65': return 'H', str(dens) + 'kg/m3'
    elif dens == '100': return 'U', str(dens) + 'kg/m3'

def color_letter(clr):
    if clr.lower() == 'b': return 'W', 'Biała'
    elif clr == 'P': return 'P', 'Różowa antystatyczna'
    elif clr == 'O': return 'O', 'Pomarańczowa antystatyczna'
    elif clr.lower() == 'c': return 'B', 'Czarna'

def skin_letter(skn):
    if skn == True: return 'S', 'Ze skórą'
    else: return 'A', ''

def nopa_letter(nop):
    if nop == True: return 'N', 'NOPAPLANK'
    else: return 'L', 'Laminat'

rodzaj = ''
while rodzaj.lower() != 'exit':
    rodzaj = input("Nowy kod dla Piany czy Tektury? [P/T]")

    if rodzaj.lower() == 'p':
        lenght = input("Podaj długość: ")
        width = input("Podaj szerokość: ")
        typ = input("Jaki rodzaj piany? [PE/PU]: ")
        thickness = int(input("Podaj grubość: "))
        density = input("Podaj gęstość: [16/22/24/27/35/65/100]")
        anti = input("Czy antystatyczna? [T/N] ")
        if anti.lower() == 't':
            color = 'P'
        else:
            color = input("Kolor piany: [Biały/Czarny] ")

        if typ.lower() == 'pe':
            nopa = input("Czy Nopaplank? [T/N]: ")
            rc = input("Jaka zawartosc recyklinu? [%]: ")
            skin = input("Czy piana ze skórką? [T/N]: ")
            arkusz = ArkuszPianyPE(lenght, width, color, thickness, density, anti, nopa, rc, skin)

            kod = 'E' + dens_letter(arkusz.density())[0] + color_letter(arkusz.color())[0] + arkusz.lenght()[:3] + arkusz.width()\
               + arkusz.thickness() + skin_letter(arkusz.with_skin())[0] + arkusz.recycle()[0] + nopa_letter(arkusz.nopaplank())[0]

            opis = 'Piana Polietylenowa, ' + dens_letter(arkusz.density())[1] + ', ' + color_letter(arkusz.color())[1] + ', ' + arkusz.lenght() + 'x'\
               + arkusz.width()+ '0x' + arkusz.thickness() + ', ' + skin_letter(arkusz.with_skin())[1] + ', ' + arkusz.recycle() + '% recyklatu, '\
              + nopa_letter(arkusz.nopaplank())[1]

        elif typ.lower() == 'pu':
            arkusz = ArkuszPiany(lenght, width, color, thickness, density, anti)
            if anti.lower() == 't':
                color = 'O'
            else:
                color = input("Kolor piany: [Biały/Czarny] ")

            kod = 'U' + dens_letter(arkusz.density())[0] + color_letter(arkusz.color())[0] + arkusz.lenght()[:3] + arkusz.width()\
               + arkusz.thickness() + 'A0B' 

            opis = 'Piana Poliuretanowa, ' + dens_letter(arkusz.density())[1] + ', ' + color_letter(arkusz.color())[1] + ', ' + arkusz.lenght() + 'x'\
               + arkusz.width()+ '0x' + arkusz.thickness() + ', Blok'


        print(kod)
        print(opis)

        

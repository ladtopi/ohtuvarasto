from varasto import Varasto

def mehut():
    mehua = Varasto(100.0)

    print(f"Mehuvarasto: {mehua}")

    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")

    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print("mehua.otaVarastosta(-32.9)")
    mehua.ota_varastosta(-32.9)
    print(f"Mehuvarasto: {mehua}")


def oluet():
    olutta = Varasto(100.0, 20.2)

    print(f"Olutvarasto: {olutta}")

    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print("olutta.ota_varastosta(1000.0)")
    olutta.ota_varastosta(1000.0)
    print(f"Olutvarasto: {olutta}")

def virheet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def main():
    mehut()
    oluet()
    virheet()


if __name__ == "__main__":
    main()

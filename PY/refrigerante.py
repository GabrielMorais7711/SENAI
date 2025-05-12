latas = int(input("Latas (350ml): "))
garrafas600 = int(input("Garrafas 600ml: "))
garrafas2l = int(input("Garrafas 2L: "))
litros = (latas * 350 + garrafas600 * 600 + garrafas2l * 2000) / 1000
print(f"Total: {litros} litros")
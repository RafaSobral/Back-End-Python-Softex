# 9 enquanto o usuario digitar algo que contenha a palavra "spoiler"
# use . lower e in e peça para digitar novamente

palavra = input("digite algo que contenha a palavra spoiler: ").lower()

while "spoiler" in palavra:
    palavra = input("digite algo que contenha a palavra spoiler: ").lower()

print("palavra sem spoiler")

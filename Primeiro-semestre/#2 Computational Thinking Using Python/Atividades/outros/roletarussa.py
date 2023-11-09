import random
from time import sleep

slotBala = random.randint(1, 6)
aleatorio = random.randint(1, 6)

print("Você segura o revolver")
sleep(2)
print(f"Você aloca a munição no slot {slotBala}")
sleep(3)
print("O gatilho é puxado")
sleep(4)
print("\n...")
sleep(5)
if aleatorio == slotBala:
    print(f"\nA munição estava alocada no slot {aleatorio}")
    sleep(1)
    print("\nVocê morreu.")

else:
    print(f"\nA munição estava alocada no slot {aleatorio}")
    sleep(1)
    print("\nVocê sobreviveu!")

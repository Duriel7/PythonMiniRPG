import math

ray = int(input("Quel rayon ?\n"));

h = int(input("Quelle hauteur ?\n"));

volume = (math.pi * (ray ** 2) * h)/3;

print("Votre cône a un volume de", volume);
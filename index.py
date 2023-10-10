def charger_foret(nom_fichier):
	with open(nom_fichier) as f:
		plan = f.read().split("\n")
		if plan[-1] == "":
			plan = plan[:-1]
	return plan

plan = charger_foret("github/plan_foret.txt")

def recherche_maison_carre_opt(plan):
	largeur = len(plan[0])
	hauteur = len(plan)
	recherche = [[-1 for i in range(largeur)] for j in range(hauteur)]

	maison_max = (0, 0, 0) # (taille, i, j)

	ARBRE = "o"
	PAS_ARBRE = "."
	
	for i in range(hauteur):
		for j in range(largeur):
			if plan[i][j] == ARBRE:
				recherche[i][j] = 0
			else:
				if i==0 or j==0:
					recherche[i][j] = 1
				else:
					recherche[i][j] = 1 + min(recherche[i-1][j],
											  recherche[i-1][j-1],
											  recherche[i][j-1])

			if maison_max[0] < recherche[i][j]:
				maison_max = (recherche[i][j], i, j)
 
	return maison_max

t = recherche_maison_carre_opt(plan)
print(t)

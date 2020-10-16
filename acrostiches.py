import random

adjectifs = {
	"A": ["Adorable", "Amical.e", "Agil.e", "Arrogant.e", "Audacieux.se"],
	"B": ["Barbare", "Belle", "Brave"],
	"C": ["Cupide", "Classe", "Comique", "Cocasse" ],
	"D": ["Drole", "Dormeur.se", "Dictateur.trice"],
	"E": ["Exceptionnel.le", "Elégant.e", "Erudit.e"],
	'F': ["Fort.e", "Fantastique", "Frimeur.se"],
	"G": ["Génial", "Généreux.se", "Gentil.le"],
	"H": ["Horrible", "Hackeur.se", "Hospitalié"],
	"I": ["Irrestible", "Idiot.e", "Idilique","Invincible"],
	"J": ["Joyeu.se", "Joli.e", "Joueur.euse"],
	"K": ["Kanon", "Kamikaze"],
	"L": ["Loyal.e", "Logique", "Lourd.e"],
	"M": ["Magnifique", "Mignon.e", "Myope"],
	"N": ["Naif.ve", "Novateur.trice", "Narquois.e", "Nauseabond.e"],
	"O": ["Optimiste", "Original.e"],
	"P": ["Parfait.e", "Propre", "Purifié.e" ],
	"Q": ["Qualitatif.ve", "Qomique"],
	"R": ["Responsable", "Raisonnable", "Rigolot.e"],
	"S": ["Super", "Sympa", "Salvateur.trice"],
	"T": ["Triste", "Terrifiant.e", "Torturé.e", "Taquin.e", "Trivial.e"],
	"U": ["Unique", "Utopiste",],
	"V": ["Vrai.e", "Vénéré.e", "Vaniteux.se"],
	"W": ["Wow", "Waouw", "Wapiti" ],
	"X": ["Xylophone", "Xtra'comme les kellogs"],
	"Y": ["Youpi", "Youhou", "Yougoslave"],
	"Z": ["Zinzin", "Zébré", "Zelé"],
}

prenom = input("Tapez votre prenom : ")
prenom_maj = prenom.upper()
lettres = list(prenom_maj)

for lettre in lettres:
	accro = adjectifs.get(lettre)
	final = random.choice(accro)
	print(final)

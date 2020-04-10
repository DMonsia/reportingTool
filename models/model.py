import sqlite3 as sql
import pandas as pd


def createDB(DB_name):
	DB_name += '.db'
	connexion = sql.connect(DB_name)
	curseur = connexion.cursor()

	querry = """
	    CREATE TABLE IF NOT EXISTS "Patient" (
	    "code_patient" TEXT NOT NULL UNIQUE,
	    "poste_depistage" TEXT NOT NULL,
	    "date_depistage" TEXT,
	    "sexe" TEXT NOT NULL,
	    "age" INTEGER NOT NULL,
	    "tranche_age" TEXT NOT NULL,
	    "grandeur_age" TEXT NOT NULL,
	    "conseiller_pour_test" TEXT,
	    "effectivement_depiste"	TEXT,
	    "conseiller_depister_ayant_son_resultat" TEXT,
	    "resultat_test_depistage" TEXT,
	    "positif_ayant_recu_son_resultat" TEXT,
	    "positif_beneficiant_de_CD4" TEXT,
	    PRIMARY KEY("code_patient"))
	    """

	curseur.execute(querry)

	curseur.close()

def insert(patient,DB_name):
	connexion = sql.connect(DB_name)
	curseur = connexion.cursor()
	querry = '''INSERT INTO "Patient" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
	curseur.execute(querry,patient)
	connexion.commit()
	curseur.close()


def selectAll(DB_name):
	connexion = sql.connect(DB_name)
	curseur = connexion.cursor()

	querry = """SELECT * FROM 'Patient' """
	curseur.execute(querry)
	#recuperation des données
	d = curseur.fetchall()
	variables = [
	    "Code du patient",
	    "Poste de dépistage",
	    "Date de dépistage",
	    "Sexe du patient",
	    "Age du patient",
	    "Préciser la tranche d'age",
	    "Grandeur de l'age",
	    'Conseiller pour le test',
	    'Effectivement dépisté',
	    'Conseiller et dépister ayant reçu son résultat',
	    'Résultat du test de dépistage',
	    'Positif ayant reçu son résultat',	
	    "Positif bénéficiant d'un CD4"]

	df = pd.DataFrame(d,columns = variables)

	df.loc[df["Grandeur de l'age"].isin(["Jours","Semaines","Mois"]),"Préciser la tranche d'age"] = "<1"

	#convertion de la variable "Date de dépistage" et  des variables "dteDebut" et "dteFin" en format Date
	df["Date de dépistage"] = pd.to_datetime(df["Date de dépistage"])

	# selection des variable d'interet
	listVar = ["Date de dépistage","Poste de dépistage","Code du patient","Sexe du patient","Préciser la tranche d'age",'Conseiller pour le test', 'Effectivement dépisté', 'Conseiller et dépister ayant reçu son résultat', 'Résultat du test de dépistage', 'Positif ayant reçu son résultat', "Positif bénéficiant d'un CD4"]
	Data = df[listVar]
	curseur.close()

	return Data

import pandas as pd
from datetime import datetime as dt


def   sexSetData(data):
    df_homme = data.loc[data["Sexe du patient"] == "Masculin"]
    
    listVarb = ['Conseiller pour le test', 'Effectivement dépisté', 'Conseiller et dépister ayant reçu son résultat', 'Positif ayant reçu son résultat', "Positif bénéficiant d'un CD4"]
    listGroupeHomme= []
    for var in listVarb:
        temp = df_homme.loc[df_homme[var] =="Oui",[var,"Préciser la tranche d'age"]]
        listGroupeHomme.append(temp.groupby("Préciser la tranche d'age").count().T)

    RTD = df_homme.loc[df_homme["Résultat du test de dépistage"] =="Positif",["Préciser la tranche d'age","Résultat du test de dépistage"]]
    df_RTD = RTD.groupby("Préciser la tranche d'age").count().T
    listGroupeHomme.insert(3,df_RTD)
    RTDN = df_homme.loc[df_homme["Résultat du test de dépistage"] =="Négatif",["Préciser la tranche d'age","Résultat du test de dépistage"]]
    df_RTDN = RTDN.groupby("Préciser la tranche d'age").count().T
    listGroupeHomme.append(df_RTDN)
    
    trancheAgeHomme = {'<1':[],'1-4':[], '5-9':[], '10-14':[], '15-19':[],'20-24':[] ,'25-29':[] ,'30-34':[] ,'35-39':[] ,'40-44':[] ,'45-49':[] ,'50 +':[]}
    for i in trancheAgeHomme:
        for g in listGroupeHomme:
            try:
                trancheAgeHomme[i].append(g[i][0])
            except Exception:
                trancheAgeHomme[i].append(0)
    
    
    df_femme = data.loc[data["Sexe du patient"] == "Féminin"]
    listGroupeFemme= []
    for var in listVarb:
        temp = df_femme.loc[df_femme[var] =="Oui",[var,"Préciser la tranche d'age"]]
        listGroupeFemme.append(temp.groupby("Préciser la tranche d'age").count().T)

    RTDf = df_femme.loc[df_femme["Résultat du test de dépistage"] =="Positif",["Préciser la tranche d'age","Résultat du test de dépistage"]]
    df_RTDf = RTDf.groupby("Préciser la tranche d'age").count().T
    listGroupeFemme.insert(3,df_RTDf)
    RTDNf = df_femme.loc[df_femme["Résultat du test de dépistage"] =="Négatif",["Préciser la tranche d'age","Résultat du test de dépistage"]]
    df_RTDNf = RTDNf.groupby("Préciser la tranche d'age").count().T
    listGroupeFemme.append(df_RTDNf)
    
    trancheAgeFemme = {'<1':[],'1-4':[], '5-9':[], '10-14':[], '15-19':[],'20-24':[] ,'25-29':[] ,'30-34':[] ,'35-39':[] ,'40-44':[] ,'45-49':[] ,'50 +':[]}
    for i in trancheAgeFemme:
        for g in listGroupeFemme:
            try:
                trancheAgeFemme[i].append(g[i][0])
            except Exception:
                trancheAgeFemme[i].append(0)
    
    return trancheAgeHomme, trancheAgeFemme

def dataFilter(file):
    df = pd.read_excel(file)
    df.loc[df["Grandeur de l'age"].isin(["Jours","Semaines","Mois"]),"Préciser la tranche d'age"] = "<1"
    
    #convertion de la variable "Date de dépistage" et  des variables "dteDebut" et "dteFin" en format Date
    df["Date de dépistage"] = pd.to_datetime(df["Date de dépistage"])

    # selection des variable d'interet
    listVar = ["Date de dépistage","Poste de dépistage","Code du patient","Sexe du patient","Préciser la tranche d'age",'Conseiller pour le test', 'Effectivement dépisté', 'Conseiller et dépister ayant reçu son résultat', 'Résultat du test de dépistage', 'Positif ayant reçu son résultat', "Positif bénéficiant d'un CD4"]
    Data = df[listVar]
    return Data


def selectDataPeriode(df,dteDebut = "1700-01-01", dteFin = "2099-01-01"):
    try:
        dteDebut = pd.to_datetime(QDateToStr(dteDebut))
        dteFin = pd.to_datetime(QDateToStr(dteFin))
    except Exception:
        dteDebut = pd.to_datetime(dteDebut)
        dteFin = pd.to_datetime(dteFin)
    
    #selection de la plage de données
    DataPeriode = df.loc[(df["Date de dépistage"]>=dteDebut) & (df["Date de dépistage"]<=dteFin), : ]
    
    return DataPeriode




def generateurDataExcel(trancheAgeHomme,trancheAgeFemme, outFileName):
    matrix = []
    for i in range(7):
        row =[str(trancheAgeHomme['<1'][i]),str(trancheAgeHomme['1-4'][i]),str(trancheAgeHomme['5-9'][i]),
              str(trancheAgeHomme['10-14'][i]),str(trancheAgeHomme['15-19'][i]),str(trancheAgeHomme['20-24'][i]),
              str(trancheAgeHomme['25-29'][i]),str(trancheAgeHomme['30-34'][i]),str(trancheAgeHomme['35-39'][i]),
              str(trancheAgeHomme['40-44'][i]),str(trancheAgeHomme['45-49'][i]),str(trancheAgeHomme['50 +'][i]),
              
              str(trancheAgeFemme['<1'][i]),str(trancheAgeFemme['1-4'][i]),str(trancheAgeFemme['5-9'][i]),
              str(trancheAgeFemme['10-14'][i]),str(trancheAgeFemme['15-19'][i]),str(trancheAgeFemme['20-24'][i]),
              str(trancheAgeFemme['25-29'][i]),str(trancheAgeFemme['30-34'][i]),str(trancheAgeFemme['35-39'][i]),
              str(trancheAgeFemme['40-44'][i]),str(trancheAgeFemme['45-49'][i]),str(trancheAgeFemme['50 +'][i]),
        ]
        matrix.append(row)
        
    rowNames = [
    "Nombre de clients conseillés pour le dépistage du VIH",
    "Nombre de clients dépistés pour le VIH",
    "Nombre de clients conseillés et dépistés pour le VIH ayant reçu le resultat",
    "Nombre de clients dépistés positif au VIH",
    "Nombre de clients dépistés positif au VIH ayant reçu le résultat du test",
    "Nombre de clients dépistés VIH positif ayant bénéficié d'un CD4",
    "Nombre de clients dépistés VIH négatif",
    ]
    
    
    colNames = ['<1','1-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50 +',
                '<1','1-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50 +']
    tuples = list(zip(["Hommes"]*14 + ["Femme"]*14,colNames))
    index = pd.MultiIndex.from_tuples(tuples,names=[outFileName,outFileName])
    df = pd.DataFrame(matrix, index=rowNames, columns = index)
    
    df.to_excel(outFileName+".xlsx", sheet_name="CDIP")



def recuperData(Data):
    #liste des postes de depistage
    posteDepistage = list(set(Data["Poste de dépistage"]))

    for poste in posteDepistage:
        data = Data.loc[Data["Poste de dépistage"] == poste]
        trancheAgeHomme,trancheAgeFemme = sexSetData(data)
        generateurDataExcel(trancheAgeHomme,trancheAgeFemme, poste)


def QDateToStr(Qdate):
    return "-".join([str(d) for d in Qdate.getDate()])
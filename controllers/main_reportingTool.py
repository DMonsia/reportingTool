from PyQt5.QtWidgets	import	QMainWindow, QMessageBox, QFileDialog, QCheckBox, QTableWidgetItem
from views.ui_reportingTool_2_1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
import controllers.traitement  as trt
import os
import sqlite3 as sql
import models.model as model



class MainReportingTool(QMainWindow,Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainReportingTool, self).__init__(parent)
		self.setupUi(self)
		self.pushButtonExporter.setEnabled(False)
		self.groupBoxPeriode.setEnabled(False)
		self.groupBoxFiltre.setEnabled(False)

		self.comboBoxSource.currentIndexChanged.connect(self.oncomboBoxSourcecurrentTextChanged)

		self.filleName = None
		self.Data = None
		self.dataPeriode = None
		self.periodeSelect = False
		self.DB_name = 'depistageDB.db'
		self.pushButtonAccueil.setStyleSheet(self.buttonClickedStyle)
		self.mb = QMessageBox()
		self.mb.setIcon(QMessageBox.Information)
		self.mb.setWindowTitle('Repporting Tool')
		



#######################################################################################
########## 							 Menu de navigation	    				 ##########
#######################################################################################
## Methodes liees aux objets du nav bar 

 	############################################################
  	######       		      Accueill      	         #######
    ############################################################
	
	@pyqtSlot()
	def on_pushButtonAccueil_clicked(self):
		self.groupBoxPeriode.setEnabled(False)
		self.groupBoxFiltre.setEnabled(False)
		self.comboBoxSource.setEnabled(True)
		self.pushButtonOkPeriode.setEnabled(True)
		self.pushButtonAccueil.setStyleSheet(self.buttonClickedStyle)
		self.pushButtonEnregistrement.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonExporter.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonVisualisation.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonDonnees.setStyleSheet(self.buttonDefaultStyle)
		self.stackedWidget.setCurrentIndex(0)


	############################################################
  	######    		     Enregigstrement                 #######
    ############################################################
	
	@pyqtSlot()
	def on_pushButtonEnregistrement_clicked(self):
		self.groupBoxPeriode.setEnabled(False)
		self.groupBoxFiltre.setEnabled(False)
		self.comboBoxSource.setEnabled(False)
		self.pushButtonOkPeriode.setEnabled(True)
		self.pushButtonAccueil.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonExporter.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonVisualisation.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonDonnees.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonEnregistrement.setStyleSheet(self.buttonClickedStyle)
		self.stackedWidget.setCurrentIndex(1)


    ############################################################
  	######      		       	Exporter                 #######
    ############################################################

	@pyqtSlot()
	def on_pushButtonExporter_clicked(self):
		self.pushButtonExporter.setStyleSheet(self.buttonClickedStyle)
		self.pushButtonAccueil.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonEnregistrement.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonVisualisation.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonDonnees.setStyleSheet(self.buttonDefaultStyle)
		self.stackedWidget.setCurrentIndex(4)
		self.groupBoxFiltre.setEnabled(False)
		self.groupBoxPeriode.setEnabled(True)
		self.comboBoxSource.setEnabled(False)
		self.pushButtonOkPeriode.setEnabled(False)
		


    ############################################################
  	######                 Visualisation                 #######
    ############################################################

	@pyqtSlot()
	def on_pushButtonVisualisation_clicked(self):
		self.pushButtonVisualisation.setStyleSheet(self.buttonClickedStyle)
		self.pushButtonExporter.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonAccueil.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonEnregistrement.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonDonnees.setStyleSheet(self.buttonDefaultStyle)
		self.groupBoxPeriode.setEnabled(False)
		self.groupBoxFiltre.setEnabled(False)
		self.stackedWidget.setCurrentIndex(3)
		self.comboBoxSource.setEnabled(False)
		self.pushButtonOkPeriode.setEnabled(True)


    ############################################################
  	######                     Donnees                   #######
    ############################################################

	@pyqtSlot()
	def on_pushButtonDonnees_clicked(self):
		self.pushButtonDonnees.setStyleSheet(self.buttonClickedStyle)
		self.pushButtonExporter.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonVisualisation.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonAccueil.setStyleSheet(self.buttonDefaultStyle)
		self.pushButtonEnregistrement.setStyleSheet(self.buttonDefaultStyle)
		self.stackedWidget.setCurrentIndex(2)
		self.groupBoxPeriode.setEnabled(True)
		self.groupBoxFiltre.setEnabled(True)
		self.comboBoxSource.setEnabled(False)
		self.pushButtonOkPeriode.setEnabled(True)

#######################################################################################
########## 							 	Les Pages   	    				 ##########
#######################################################################################

	############################################################
  	######          		 Filtrage    	             #######
    ############################################################
	
	#@pyqtSlot()
	def oncomboBoxSourcecurrentTextChanged(self):
		if self.comboBoxSource.currentText() == "BD":
			self.pushButtonFichier.setEnabled(False)
			self.pushButtonAnnuler.setEnabled(False)
			self.lineEditImporterFichier.setEnabled(False)
			self.pushButtonFichier.setStyleSheet("background-color: rgba(6, 88, 47, 180);\n" "color: rgb(255, 255, 255);")
			self.pushButtonAnnuler.setStyleSheet("background-color: rgba(6, 88, 47, 180);\n" "color: rgb(255, 255, 255);")
		else:
			self.pushButtonFichier.setEnabled(True)
			self.pushButtonAnnuler.setEnabled(True)
			self.lineEditImporterFichier.setEnabled(True)
			self.pushButtonFichier.setStyleSheet("background-color: rgb(6, 88, 47);\n" "color: rgb(255, 255, 255);")
			self.pushButtonAnnuler.setStyleSheet("background-color: rgb(6, 88, 47);\n" "color: rgb(255, 255, 255);")
			


	@pyqtSlot(bool)
	def on_radioButtonAll_toggled(self): 
		if self.radioButtonAll.isChecked():
			self.dateEditDebut.setEnabled(False)
			self.dateEditFin.setEnabled(False)
		else:
			self.dateEditDebut.setEnabled(True)
			self.dateEditFin.setEnabled(True)
			


	@pyqtSlot()
	def on_pushButtonOkPeriode_clicked(self):
		if self.radioButtonAll.isChecked():
			self.periodeSelect = False
			self.fillTableWidget(self.Data, self.tableWidgetData)
		else:
			self.periodeSelect = True
			print("Qdate: ",self.dateEditDebut.date())
			self.dataPeriode = trt.selectDataPeriode(self.Data,self.dateEditDebut.date(), self.dateEditFin.date())
			self.fillTableWidget(self.dataPeriode, self.tableWidgetData)

	
	@pyqtSlot(bool)
	def on_radioButtonFiltre_toggled(self):
		if self.radioButtonFiltre.isChecked():
			self.comboBoxPoste.setCurrentIndex(0)
			self.comboBoxSexe.setCurrentIndex(0)
			self.comboBoxPoste.setEnabled(False)
			self.comboBoxSexe.setEnabled(False)
		else:
			self.comboBoxPoste.setEnabled(True)
			self.comboBoxSexe.setEnabled(True)


	@pyqtSlot()
	def on_pushButtonOkFiltre_clicked(self):
		if self.periodeSelect:
			if self.radioButtonFiltre.isChecked():
				self.fillTableWidget(self.dataPeriode, self.tableWidgetData)

			else:
				if self.comboBoxSexe.currentText() == "Tout" and self.comboBoxPoste.currentText() != "Tout":
					donnees =  self.dataPeriode.loc[self.dataPeriode["Poste de dépistage"] == self.dataPeriode.currentText(),:]
				elif self.comboBoxSexe.currentText() != "Tout" and self.comboBoxPoste.currentText() == "Tout":
					donnees =  self.dataPeriode.loc[self.dataPeriode["Sexe du patient"] == self.comboBoxSexe.currentText(),:]
				elif self.comboBoxSexe.currentText() != "Tout" and self.comboBoxPoste.currentText() != "Tout":
					donnees =  self.dataPeriode.loc[(self.dataPeriode["Sexe du patient"] == self.comboBoxSexe.currentText()) & (self.dataPeriode["Poste de dépistage"] == self.comboBoxPoste.currentText()),:]
				else:
					donnees =  self.dataPeriode
				self.fillTableWidget(donnees, self.tableWidgetData)
		else:
			
			if self.comboBoxSexe.currentText() == "Tout" and self.comboBoxPoste.currentText() != "Tout":
				donnees =  self.Data.loc[self.Data["Poste de dépistage"] == self.comboBoxPoste.currentText(),:]
			elif self.comboBoxSexe.currentText() != "Tout" and self.comboBoxPoste.currentText() == "Tout":
				donnees =  self.Data.loc[self.Data["Sexe du patient"] == self.comboBoxSexe.currentText(),:]
			elif self.comboBoxSexe.currentText() != "Tout" and self.comboBoxPoste.currentText() != "Tout":
				donnees =  self.Data.loc[(self.Data["Sexe du patient"] == self.comboBoxSexe.currentText()) & (self.Data["Poste de dépistage"] == self.comboBoxPoste.currentText()),:]
			else:
				donnees =  self.Data
			self.fillTableWidget(donnees, self.tableWidgetData)


	############################################################
  	######          		 Accueill  	                 #######
    ############################################################
	@pyqtSlot()
	def on_pushButtonFichier_clicked(self):
		(self.filleName,filtre) = QFileDialog.getOpenFileName(self, "Ouvrir fichier de données", filter="doennées (*.xls*);; Tout (*.*)")
		if self.filleName:
			self.lineEditImporterFichier.setText(self.filleName)



	@pyqtSlot()
	def on_pushButtonOK_clicked(self):
		if self.comboBoxSource.currentText()== "Excel":
			if self.filleName:
				#try:
				self.Data = trt.dataFilter(self.filleName)
				self.pushButtonExporter.setEnabled(True)
				self.groupBoxPeriode.setEnabled(True)
				self.groupBoxFiltre.setEnabled(True)
				self.on_pushButtonDonnees_clicked()
				self.pushButtonDonnees.setEnabled(True)
				self.pushButtonExporter.setEnabled(True)
				self.lineEditImporterFichier.clear()
				self.fillTableWidget(self.Data, self.tableWidgetData)

				post = list(set(self.Data["Poste de dépistage"]))
				post.insert(0,"Tout")
				self.comboBoxPoste.addItems(post)
				#except Exception:#TODO
				#	self.mb.setText ("Verifier le fichier selectionné.")
				#	self.mb.setStandardButtons (QMessageBox.Ok )
				#	self.mb.show () 

		else:
			self.Data = model.selectAll(self.DB_name)
			self.pushButtonExporter.setEnabled(True)
			self.groupBoxPeriode.setEnabled(True)
			self.groupBoxFiltre.setEnabled(True)
			self.on_pushButtonDonnees_clicked()
			self.pushButtonDonnees.setEnabled(True)
			self.pushButtonExporter.setEnabled(True)

			post = list(set(self.Data["Poste de dépistage"]))
			post.insert(0,"Tout")
			self.comboBoxPoste.addItems(post)
			self.fillTableWidget(self.Data, self.tableWidgetData)
			

	@pyqtSlot()
	def on_pushButtonAnnuler_clicked(self):
		self.lineEditImporterFichier.clear()
		


	############################################################
  	######                    Enregistrement             #######
    ############################################################

	@pyqtSlot()
	def on_pushButtonEnregistrer_clicked(self):
		if self.lineEditCodePatient.text():
			datestr = trt.QDateToStr(self.dateEditDebut.date())
			info_patient = [
				self.lineEditCodePatient.text(),
				self.comboBoxPosteEnreg.currentText(),
				datestr,
				self.comboBoxSexeEnreg.currentText(),
				self.spinBoxAge.value(),
				self.comboBoxTrancheAge.currentText(),
				self.comboBoxGandeur.currentText(),
				self.comboBoxConseilDep.currentText(),
				self.comboBoxEffectDep.currentText(),
				self.comboBoxConseilerAvResult.currentText(),
				self.comboBoxResultat.currentText(),
				self.comboBoxPositifConnaisResultat.currentText(),
				self.comboBoxBeneficiantCD4.currentText()
				]

			messageConfirmation = "resumé:\n\n\
			\nCode du patient:\t{}\
	    	\nPoste de depistage:\t{}\
	    	\nDate de depistage:\t{}\
	    	\nSexe:\t{}\
	    	\nAge:\t{}\
	    	\nTranche d'age:\t{}\
	    	\nGrandeur de l'age:\t{}\
	    	\nConseiller pour le test:\t{}\
	    	\nEffectivement depisté:\t{}\
	    	\nConseiller et depister ayant reçu son resultat:\t{}\
	    	\nResultat du test de depistage:\t{}\
	    	\nPositif ayant reçu son résultat:\t{}\
	    	\nPositif béneficiant de CD4:\t{}\
			".format(*info_patient)
			reponse = QMessageBox.question(self,"Confirmation",messageConfirmation,QMessageBox.No,QMessageBox.Yes)
			if reponse==QMessageBox.Yes:
				try:
					model.insert(info_patient,self.DB_name)
					self.pushButtonDonnees.setEnabled(False)
					self.pushButtonExporter.setEnabled(False)
				except sql.IntegrityError:
					self.mb.setText("Ce patient a deja été enregistré")
					self.mb.setStandardButtons(QMessageBox.Ok)
					self.mb.show()
				except:
					self.mb.setText("Le patient n'a pas été enregistré, verifié les informations.")
					self.mb.setStandardButtons(QMessageBox.Ok)
					self.mb.show()
		else:
			self.mb.setText ("Vous n'avez pas renseigné le code du patient")
			self.mb.setStandardButtons(QMessageBox.Ok)
			self.mb.show()



	############################################################
  	######                     Visualisation             #######
    ############################################################




    ############################################################
  	######                     Exporter        	         #######
    ############################################################


	@pyqtSlot()
	def on_pushButtonExporter2_clicked(self):
		
		nomdossier = QFileDialog.getExistingDirectoryUrl( self,"Choisir un dossier")
		if nomdossier:
			path =  os.getcwd()
			savePath = os.path.join(nomdossier.toLocalFile(),self.lineEditExporter.text())
			try:
				os.mkdir(savePath)
				self.mb.setText ("Les fichiers seront sauvegaredés dans: \n{}".format(savePath))
				self.mb.setStandardButtons(QMessageBox.Ok )
				self.mb.show() 
			except Exception:
				self.mb.setText ("Les fichiers seront sauvegaredés dans: \n{}".format(savePath))
				self.mb.setStandardButtons (QMessageBox.Ok )
				self.mb.show ()  

			os.chdir(savePath)
			if self.radioButtonAll.isChecked():
				trt.recuperData(self.Data)
			else:
				if self.dataPeriode:
					trt.recuperData(self.dataPeriode)
				else:
					trt.recuperData(self.Data)
			self.lineEditExporter.setText("")
			os.chdir(path)
		


############################################################################
######        		   		   Statiques	   						  ######
############################################################################



	buttonDefaultStyle = "QPushButton{\n"\
	"    background-color: rgb(6, 88, 47);\n"\
"    font: 87 12pt \"Segoe UI Black\";\n"\
"    color: rgb(255, 255, 255);\n"\
"    font-weight: bold;\n"\
"    text-align: left;\n"\
"    border: 0px solid;\n"\
"    font-style : italic ;\n"\
"}\n"\
"QPushButton:hover{\n"\
"    \n"\
"    background-color: rgb(19, 252, 136);\n"\
"    background-color: rgb(5, 75, 40);\n"\
"    border-left: 5px solid;\n"\
"    border-left-color: rgb(85, 255, 0);\n"\
"}"
	buttonClickedStyle = "QPushButton{\n"\
"    font: 87 12pt \"Segoe UI Black\";\n"\
"    color: rgb(255, 255, 255);\n"\
"    font-weight: bold;\n"\
"    text-align: left;\n"\
"    border: 0px solid;\n"\
"    font-style : italic ;\n"\
"    background-color: rgb(2, 42, 22);\n"\
"    border-left: 5px solid;\n"\
"    border-left-color: rgb(85, 255, 0);\n"\
"}"


	def fillTableWidget(self, data, tableWidget):
		tableWidget.setRowCount(data.shape[0])
		tableWidget.setColumnCount(data.shape[1])

		tmp = ["Date de dépistage", "Poste de dépistage", "Code du patient", "Sexe du patient",
				"Tranche d'age", "Conseiller pour le test", "Effectivement dépisté", 
				"CD ayant reçu son résultat", "Résultat du test", "Positif ayant reçu son résultat",
				"Positif bénéficiant d'un CD4"]
		header = list()
		for i,v in enumerate(tmp):
			item = QTableWidgetItem(v)
			item.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter)
			font = QFont()
			font.setPointSize(10)
			font.setBold(True)
			font.setWeight(75)
			item.setFont(font)
			header.append(item)
			tableWidget.setHorizontalHeaderItem(i, item)
	
		tableWidget.horizontalHeader().setVisible(True)

		for i in range(data.shape[0]):
			for j in range(data.shape[1]):
				tableWidget.setItem(i, j,QTableWidgetItem(str(data.iloc[i, j])) )


	    # fonction  appelé  lors de la fermeture de l'application
	def closeEvent(self,event): # TODO
		messageConfirmation = "Êtes-vous sûr de vouloir quitter ReportingTool?"
		reponse = QMessageBox.question(self,"Confirmation",messageConfirmation,QMessageBox.No,QMessageBox.Yes)
		if  reponse==QMessageBox.Yes: event.accept()
		else: event.ignore()




	
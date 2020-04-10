import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_reportingTool	import	MainReportingTool

app = QApplication(sys.argv)
MainWindow = MainReportingTool()
MainWindow.show()
sys.exit(app.exec_())

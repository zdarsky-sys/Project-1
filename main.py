import sys
from PyQt6 import QtWidgets
from gui import Ui_main_window
from logic import register_vote

class MainWindow(QtWidgets.QMainWindow):
    """
    Main app window for voting. Submits a vote, validates input, and displaying messages
    """
    def __init__(self) -> None:
        """
        Starts the main
        """
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.submit_Button.clicked.connect(self.voter_info) ##

        self.ui.submit_label.hide()
        self.ui.error_label.hide()

        self.ui.submit_label.setStyleSheet('color: green;')
        self.ui.error_label.setStyleSheet('color: red;')

    def voter_info(self) -> None: ##
        """
        Handles the vote submission: Validates voter ID info,
        checks selected person, displays success or error messages
        """
        self.ui.submit_label.hide()
        self.ui.error_label.hide()

        voter_id: str = self.ui.voter_id_input.text().strip()

        if not (voter_id.isdigit() and len(voter_id) == 6):
            self.ui.error_label.setText('Voter ID must be 6 numbers')
            self.ui.error_label.show()
            return

        candidate: str | None = None
        if self.ui.amy_radiobutton.isChecked():
            candidate = 'Amy'
        elif self.ui.frank_radiobutton.isChecked():
            candidate = 'Frank'

        result: str = register_vote(voter_id, candidate)

        if result.startswith('Error'):
            if 'already voted' in result.lower():
                self.ui.error_label.setText('Already Voted')
            elif 'no candidate' in result.lower():
                self.ui.error_label.setText('Select a Candidate')
            else:
                self.ui.error_label.setText('Error')
            self.ui.error_label.show()
        else:
            self.ui.submit_label.setText('Submitted !')
            self.ui.submit_label.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import random
import string
import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QSlider,
    QWidget,
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(480, 320))
        self.setWindowTitle('Password generator')
        
        
        primary_font = QFont('sans-serif', 12, 700)
        secondary_font = QFont('sans-serif', 10, 500)
        
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText('the generated password '
                                               'will be here...')
        self.password_field.textChanged.connect(
            self.password_field_text_changed
        )
        
        self.password_field_copy = QPushButton()
        self.password_field_copy.setText('Copy')
        self.password_field_copy.setEnabled(False)
        self.password_field_copy.clicked.connect(self.copy_password)
        
        password_field_layout = QHBoxLayout()
        password_field_layout.addWidget(self.password_field)
        password_field_layout.addWidget(self.password_field_copy)
        
        
        self.characters_label = QLabel()
        self.characters_label.setText('Characters:')
        self.characters_label.setFont(primary_font)
        
        self.lowercase = QCheckBox()
        self.lowercase.setText(string.ascii_lowercase)
        self.lowercase.setChecked(True)
        self.lowercase.stateChanged.connect(self.checkbox_state_changed)
        
        self.uppercase = QCheckBox()
        self.uppercase.setText(string.ascii_uppercase)
        self.uppercase.setChecked(True)
        self.uppercase.stateChanged.connect(self.checkbox_state_changed)
        
        self.digits = QCheckBox()
        self.digits.setText(string.digits)
        self.digits.setChecked(True)
        self.digits.stateChanged.connect(self.checkbox_state_changed)
        
        self.punctuation = QCheckBox()
        self.punctuation.setText(string.punctuation)
        self.punctuation.setChecked(False)
        self.punctuation.stateChanged.connect(self.checkbox_state_changed)
        
        characters_grid = QGridLayout()
        characters_grid.addWidget(self.lowercase, 0,0)
        characters_grid.addWidget(self.digits, 0,1)
        characters_grid.addWidget(self.uppercase, 1,0)
        characters_grid.addWidget(self.punctuation, 1,1)
        
        characters_layout = QVBoxLayout()
        characters_layout.addWidget(self.characters_label)
        characters_layout.addLayout(characters_grid)
        characters_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter
                                       | Qt.AlignmentFlag.AlignLeft)
        
        
        self.exclude_label = QLabel()
        self.exclude_label.setText('Exclude some characters:')
        self.exclude_label.setFont(secondary_font)
        
        self.exclude_characters = QLineEdit()
        self.exclude_characters.setPlaceholderText('exclude some characters')
        
        exclude_layout = QVBoxLayout()
        exclude_layout.addWidget(self.exclude_label)
        exclude_layout.addWidget(self.exclude_characters)
        exclude_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        
        self.password_lenght = QSlider()
        self.password_lenght.setMinimum(8)
        self.password_lenght.setMaximum(32)
        self.password_lenght.setValue(12)
        self.password_lenght.setOrientation(Qt.Orientation.Horizontal)
        self.password_lenght.valueChanged.connect(
            self.password_lenght_changed
        )
        
        self.password_lenght_label = QLabel()
        self.password_lenght_label.setText(
            f'Password lenght: {self.password_lenght.value()}'
        )
        self.password_lenght_label.setFont(secondary_font)
        
        password_lenght_layout = QVBoxLayout()
        password_lenght_layout.addWidget(self.password_lenght_label)
        password_lenght_layout.addWidget(self.password_lenght)
        password_lenght_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        
        self.button = QPushButton()
        self.button.setText('Generate password')
        self.button.clicked.connect(self.generate_password)
        
        
        password_layout = QVBoxLayout()
        password_layout.addLayout(password_field_layout)
        password_layout.addLayout(characters_layout)
        password_layout.addLayout(exclude_layout)
        password_layout.addLayout(password_lenght_layout)
        password_layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(password_layout)
        
        self.setCentralWidget(container)
    
    def generate_password(self):
        syms = ''
        
        if self.lowercase.isChecked():
            syms += self.lowercase.text()
        if self.uppercase.isChecked():
            syms += self.uppercase.text()
        if self.digits.isChecked():
            syms += self.digits.text()
        if self.punctuation.isChecked():
            syms += self.punctuation.text()
        
        symbols = ''
        for ch in syms:
            if ch not in self.exclude_characters.text():
                symbols += ch
        
        password = ''
        while len(password) < self.password_lenght.value():
            password += random.choice(symbols)
        
        self.password_field.setText(password)
    
    def password_lenght_changed(self):
        self.password_lenght_label.setText(
            f'Password lenght: {self.password_lenght.value()}'
        )
    
    def copy_password(self):
        text = self.password_field.text()
        
        if text:
            QApplication.clipboard().setText(text)
    
    def password_field_text_changed(self):
        text = self.password_field.text()
        
        if [x for x in text if x.replace(' ', '')]:
            self.password_field_copy.setEnabled(True)
        else:
            self.password_field_copy.setEnabled(False)
    
    def checkbox_state_changed(self):
        is_checked_lowercase = self.lowercase.isChecked()
        is_checked_uppercase = self.uppercase.isChecked()
        is_checked_digits = self.digits.isChecked()
        is_checked_punctuation = self.punctuation.isChecked()
        
        if (is_checked_lowercase or is_checked_uppercase
            or is_checked_digits or is_checked_punctuation):
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

def application():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()

if __name__ == '__main__':
    application()
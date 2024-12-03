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
        
        self.setFixedSize(QSize(480, 240))
        self.setWindowTitle('Password generator')
        
        self.primary_font = QFont('sans-serif', 12, 700)
        self.secondary_font = QFont('sans-serif', 10, 500)
        
        self.setFont(self.secondary_font)
        
        top_left_alignment = (Qt.AlignmentFlag.AlignTop
                              | Qt.AlignmentFlag.AlignLeft)
        
        
        self.characters_label = QLabel()
        self.characters_label.setText('Characters:')
        self.characters_label.setFont(self.primary_font)
        
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
        
        characters_grid_layout = QGridLayout()
        characters_grid_layout.addWidget(self.lowercase, 0,0)
        characters_grid_layout.addWidget(self.digits, 0,1)
        characters_grid_layout.addWidget(self.uppercase, 1,0)
        characters_grid_layout.addWidget(self.punctuation, 1,1)
        
        characters_layout = QVBoxLayout()
        characters_layout.addWidget(self.characters_label)
        characters_layout.addLayout(characters_grid_layout)
        characters_layout.setAlignment(top_left_alignment)
        
        
        self.password_lenght = QSlider()
        self.password_lenght.setMinimum(8)
        self.password_lenght.setMaximum(24)
        self.password_lenght.setValue(12)
        self.password_lenght.setOrientation(Qt.Orientation.Horizontal)
        self.password_lenght.valueChanged.connect(
            self.password_lenght_changed
        )
        
        self.password_lenght_label = QLabel()
        self.password_lenght_label.setText(
            f'Password lenght: {self.password_lenght.value()}'
        )
        
        password_lenght_layout = QVBoxLayout()
        password_lenght_layout.addWidget(self.password_lenght_label)
        password_lenght_layout.addWidget(self.password_lenght)
        password_lenght_layout.setAlignment(top_left_alignment)
        
        
        self.duplicate_characters = QSlider()
        self.duplicate_characters.setMinimum(1)
        self.duplicate_characters.setMaximum(4)
        self.duplicate_characters.setValue(2)
        self.duplicate_characters.setOrientation(Qt.Orientation.Horizontal)
        self.duplicate_characters.valueChanged.connect(
            self.duplicate_characters_changed
        )
        
        self.duplicate_characters_label = QLabel()
        self.duplicate_characters_label.setText(
            f'Duplicate characters: {self.duplicate_characters.value()}'
        )
        
        duplicate_characters_layout = QVBoxLayout()
        duplicate_characters_layout.addWidget(self.duplicate_characters_label)
        duplicate_characters_layout.addWidget(self.duplicate_characters)
        duplicate_characters_layout.setAlignment(top_left_alignment)
        
        
        password_settings_layout = QHBoxLayout()
        password_settings_layout.addLayout(password_lenght_layout, 1)
        password_settings_layout.addSpacing(10)
        password_settings_layout.addLayout(duplicate_characters_layout)
        
        
        self.exclude_label = QLabel()
        self.exclude_label.setText('Exclude some characters')
        
        self.exclude_characters = QLineEdit()
        self.exclude_characters.setPlaceholderText('Example: 123456QwertY')
        self.exclude_characters.textChanged.connect(self.check_the_generation)
        
        exclude_layout = QHBoxLayout()
        exclude_layout.addWidget(self.exclude_label)
        exclude_layout.addWidget(self.exclude_characters)
        exclude_layout.setAlignment(top_left_alignment)
        
        
        self.password_label = QLabel()
        self.password_label.setText('Password')
        
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText(
            'The generated password will be here...'
        )
        self.password_field.textChanged.connect(
            self.password_field_text_changed
        )
        
        self.password_field_copy = QPushButton()
        self.password_field_copy.setText('Copy')
        self.password_field_copy.setEnabled(False)
        self.password_field_copy.clicked.connect(self.copy_password)
        
        password_field_layout = QHBoxLayout()
        password_field_layout.addWidget(self.password_label)
        password_field_layout.addWidget(self.password_field)
        password_field_layout.addWidget(self.password_field_copy)
        
        
        self.gen_password_btn = QPushButton()
        self.gen_password_btn.setText('Generate password')
        self.gen_password_btn.clicked.connect(self.generate_password)
        
        
        password_layout = QVBoxLayout()
        password_layout.addLayout(characters_layout)
        password_layout.addSpacing(4)
        password_layout.addLayout(password_settings_layout)
        password_layout.addSpacing(4)
        password_layout.addLayout(exclude_layout)
        password_layout.addSpacing(8)
        password_layout.addLayout(password_field_layout)
        password_layout.addWidget(self.gen_password_btn)
        
        container = QWidget()
        container.setLayout(password_layout)
        
        self.setCentralWidget(container)
    
    def password_field_text_changed(self):
        text = self.password_field.text()
        
        if list(filter(lambda x: x != ' ', text)):
            self.password_field_copy.setEnabled(True)
        else:
            self.password_field_copy.setEnabled(False)
    
    def copy_password(self):
        password = self.password_field.text()
        
        if password:
            QApplication.clipboard().setText(password)
    
    def checkbox_state_changed(self):
        self.update_symbols()
        self.check_the_generation()
    
    def check_the_generation(self):
        self.update_symbols()
        
        gen_chars_lenght = len(self.symbols)*self.duplicate_characters.value()
        password_lenght = self.password_lenght.value()
        
        if gen_chars_lenght >= password_lenght:
            self.gen_password_btn.setEnabled(True)
            self.gen_password_btn.setText('Generate password')
            self.gen_password_btn.setStyleSheet('color: black;')
        else:
            self.gen_password_btn.setEnabled(False)
            self.gen_password_btn.setText(
                'Too many excludes / Not enough characters to generate'
            )
            self.gen_password_btn.setStyleSheet('color: red;')
        
        self.gen_password_btn.setFont(self.secondary_font)
    
    def password_lenght_changed(self):
        self.check_the_generation()
        self.password_lenght_label.setText(
            f'Password lenght: {self.password_lenght.value()}'
        )
    
    def duplicate_characters_changed(self):
        self.check_the_generation()
        self.duplicate_characters_label.setText(
            f'Duplicate characters: {self.duplicate_characters.value()}'
        )
    
    def update_symbols(self):
        all_symbols = ''
        
        if self.lowercase.isChecked():
            all_symbols += self.lowercase.text()
        if self.uppercase.isChecked():
            all_symbols += self.uppercase.text()
        if self.digits.isChecked():
            all_symbols += self.digits.text()
        if self.punctuation.isChecked():
            all_symbols += self.punctuation.text()
        
        self.symbols = ''
        
        for ch in all_symbols:
            if ch not in self.exclude_characters.text():
                self.symbols += ch
    
    def generate_password(self):
        self.update_symbols()
        
        password = ''
        while len(password) < self.password_lenght.value():
            random_symbol = random.choice(self.symbols)
            
            symbol_counts = password.lower().count(random_symbol.lower())
            duplicate_chars_count = self.duplicate_characters.value()
            
            if symbol_counts < duplicate_chars_count:
                password += random_symbol
        
        self.password_field.setText(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
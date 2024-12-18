import random
import string
import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QComboBox,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QWidget,
)



class ColorConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        font_primary = QFont('sans-serif', 11)
        
        
        color_format_list = ['rgb', 'hex']
        
        self.color_format_combobox = QComboBox()
        self.color_format_combobox.addItems(
            [x.upper() for x in color_format_list]
        )
        self.color_format_combobox.currentTextChanged.connect(
            self.color_format_changed
        )
        
        self.color_format = self.color_format_combobox.currentText()
        
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText('(171, 205, 239)')
        self.user_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_input.setMaxLength(15)
        self.user_input.textChanged.connect(self.user_input_text_changed)
        
        gen_rand_color = QPushButton()
        gen_rand_color.setText('Random color')
        gen_rand_color.clicked.connect(self.generate_random_color)
        
        self.label_convert_to = QLabel()
        self.label_convert_to.setText('HEX:')
        self.label_convert_to.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.converted_color_label = QLabel()
        self.converted_color_label.setText('#abcdef')
        self.converted_color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.converted_color_label.setContentsMargins(0,5,0,5)
        self.converted_color_label.setFont(font_primary)
        self.converted_color_label.setStyleSheet(
            'border: 1px solid gray;'
            'color: gray;'
        )
        self.converted_color_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        
        self.preview_color_label = QLabel()
        self.preview_color_label.setStyleSheet(
            'background-color: rgb(171,205,239);'
            'border: 1px solid gray;'
        )
        self.preview_color_label.setContentsMargins(30,0,0,0)
        
        copy_button = QPushButton()
        copy_button.setText('Copy')
        copy_button.clicked.connect(self.copy_color)
        
        
        layout = QGridLayout()
        layout.addWidget(self.color_format_combobox, 0,0)
        layout.addWidget(self.user_input, 0,1)
        layout.addWidget(gen_rand_color, 0,2)
        layout.addWidget(self.label_convert_to, 1,0)
        layout.addWidget(self.converted_color_label, 1,1)
        layout.addWidget(self.preview_color_label, 1,2, 3,1)
        layout.addWidget(copy_button, 2,0, 2,2)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    
    def hex_to_rgb(self, hex_color: str) -> str:
        hex_color = hex_color.lstrip('#')
        rgb_color = tuple(
            int(hex_color[i:i+2], 16) for i in range(0, len(hex_color), 2)
        )
        return f'{rgb_color}'
    
    def rgb_to_hex(self, rgb_color: str) -> str:
        r, g, b = map(int, rgb_color.split(','))
        hex_color = '#{:02x}{:02x}{:02x}'.format(r,g,b)
        return hex_color
    
    def color_format_changed(self, color_format):
        match color_format:
            case 'RGB':
                self.color_format = color_format
                self.user_input.setPlaceholderText('(171, 205, 239)')
                self.label_convert_to.setText('HEX:')
                self.converted_color_label.setText('#abcdef')
            case 'HEX':
                self.color_format = color_format
                self.user_input.setPlaceholderText('#abcdef')
                self.label_convert_to.setText('RGB:')
                self.converted_color_label.setText('(171, 205, 239)')
    
    def user_input_text_changed(self, text: str):
        color: str = None
        
        if text:
            if self.color_format == 'RGB':
                if text.startswith('(') or text.endswith(')'):
                    text = text.strip('()')
                try:
                    color = self.rgb_to_hex(text)
                    self.preview_color_label.setStyleSheet(
                        f'background-color: {color};'
                        'border: 1px solid gray;'
                    )
                    self.converted_color_label.setText(color)
                except ValueError:
                    self.preview_color_label.setStyleSheet(
                        'background-color: black;'
                        'border: 1px solid red;'
                    )
                    self.converted_color_label.setText('#???')
            elif self.color_format == 'HEX':
                try:
                    color = self.hex_to_rgb(text)
                    self.preview_color_label.setStyleSheet(
                        f'background-color: rgb{color};'
                        'border: 1px solid gray;'
                    )
                    self.converted_color_label.setText(color)
                except ValueError:
                    self.preview_color_label.setStyleSheet(
                        'background-color: black;'
                        'border: 1px solid red;'
                    )
                    self.converted_color_label.setText('(?, ?, ?)')
        else:
            if self.color_format == 'RGB':
                self.preview_color_label.setStyleSheet(
                    'background-color: rgb(171, 205, 239);'
                    'border: 1px solid gray;'
                )
                self.converted_color_label.setText('#abcdef')
            elif self.color_format == 'HEX':
                self.preview_color_label.setStyleSheet(
                    'background-color: #abcdef;'
                    'border: 1px solid gray;'
                )
                self.converted_color_label.setText('(171, 205, 239)')
    
    def generate_random_color(self):
        color: str = ''
        rgb_color_range: tuple = (0, 255)
        hex_color_symbols: str = 'abcdef' + string.digits
        
        match self.color_format:
            case 'RGB':
                r = random.randint(*rgb_color_range)
                g = random.randint(*rgb_color_range)
                b = random.randint(*rgb_color_range)
                
                color = f'({r}, {g}, {b})'
                
                self.user_input.setText(color)
            case 'HEX':
                while len(color) < 6:
                    color += random.choice(hex_color_symbols)
                
                self.user_input.setText(f'#{color}')
    
    def copy_color(self):
        color_code = self.converted_color_label.text()
        QApplication.clipboard().setText(color_code)

class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        label = QLabel()
        label.setText('Currency converter')
        
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

class UnitConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        label = QLabel()
        label.setText('Unit converter')
        
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(360, 240))
        self.setWindowTitle('Converter')
        
        
        tab = QTabWidget()
        tab.addTab(ColorConverter(), 'Color')
        tab.addTab(CurrencyConverter(), 'Currency')
        tab.addTab(UnitConverter(), 'Unit')
        tab.setTabEnabled(1, False)
        tab.setTabEnabled(2, False)
        
        
        layout = QHBoxLayout()
        layout.addWidget(tab)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
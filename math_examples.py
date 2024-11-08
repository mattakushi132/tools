import random
import sys
import time
import threading

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QLabel,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QProgressBar,
    QPushButton,
    QWidget,
)



class Separator(QFrame):
    def __init__(
            self,
            orientation: str,
            line_width: int = 1,
        ):
        super().__init__()
        
        if orientation.lower() == 'h':
            self.setFrameShape(QFrame.Shape.HLine)
        elif orientation.lower() == 'v':
            self.setFrameShape(QFrame.Shape.VLine)
        
        self.setLineWidth(line_width)
        self.setStyleSheet('color: lightgray;')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Mathematical examples')
        self.resize(QSize(560, 320))
        
        self.font_primary = QFont('sans-serif', 12)
        self.font_primary_bold = QFont('sans-serif', 12, 600)
        self.font_secondary = QFont('sans-serif', 10)
        self.setFont(self.font_secondary)
        
        
        top_left_align = (Qt.AlignmentFlag.AlignTop
                          | Qt.AlignmentFlag.AlignLeft)
        
        
        self.right_answers = 0
        self.wrong_answers = 0
        self.score = self.right_answers - self.wrong_answers
        self.result = 0
        
        self.numbers_dict = {
            'positive': {
                'easy': {
                    '+': [1, 100],
                    '-': [1, 100],
                    '*': [2, 10],
                    '/': '...',
                },
                'normal': {
                    '+': [1, 1000],
                    '-': [1, 1000],
                    '*': [2, 25],
                    '/': '...',
                },
                'hard': {
                    '+': [10, 10000],
                    '-': [10, 10000],
                    '*': [2, 50],
                    '/': '...',
                }
            },
            'negative': {
                'easy': {
                    '+': [-100, 100],
                    '-': [-100, 100],
                    '*': [-10, 10],
                    '/': '...',
                },
                'normal': {
                    '+': [-1000, 1000],
                    '-': [-1000, 1000],
                    '*': [-25, 25],
                    '/': '...',
                },
                'hard': {
                    '+': [-10000, 10000],
                    '-': [-10000, 10000],
                    '*': [-50, 50],
                    '/': '...',
                }
            }
        }
        
        self.num_state = 'negative'
        self.diff = 'normal'
        
        self.current_gen_nums_dict = {
            '+': self.numbers_dict[self.num_state][self.diff]['+'],
            '-': self.numbers_dict[self.num_state][self.diff]['-'],
            '*': self.numbers_dict[self.num_state][self.diff]['*'],
        }
        
        
        self.settings_label = QLabel()
        self.settings_label.setText('Settings:')
        self.settings_label.setFont(self.font_primary)
        
        self.logging = True
        
        self.logging_checkbox = QCheckBox()
        self.logging_checkbox.setText('logging')
        self.logging_checkbox.setChecked(self.logging)
        self.logging_checkbox.stateChanged.connect(self.logging_state_changed)
        
        logging_settings_layout = QHBoxLayout()
        logging_settings_layout.addWidget(self.settings_label)
        logging_settings_layout.addWidget(
            self.logging_checkbox,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        
        self.difficulty_label = QLabel()
        self.difficulty_label.setText('Difficulty')
        
        difficulty_list = ['Easy', 'Normal', 'Hard']
        
        self.difficulty = QComboBox()
        self.difficulty.addItems(difficulty_list)
        self.difficulty.setCurrentIndex(1)
        self.difficulty.currentTextChanged.connect(
            self.difficulty_state_changed
        )
        
        difficulty_layout = QHBoxLayout()
        difficulty_layout.addWidget(self.difficulty_label)
        difficulty_layout.addWidget(self.difficulty)
        
        
        self.countdown_checkbox = QCheckBox()
        self.countdown_checkbox.setText('Countdown (Hard)')
        self.countdown_checkbox.setEnabled(False)
        self.countdown_checkbox.stateChanged.connect(
            self.countdown_state_changed
        )
        
        self.countdown_time_list = [10, 20, 30]
        
        self.countdown_combobox = QComboBox()
        self.countdown_combobox.addItems(
            [str(s)+f's' for s in self.countdown_time_list]
        )
        self.countdown_combobox.setCurrentIndex(1)
        self.countdown_combobox.setEnabled(False)
        self.countdown_combobox.currentIndexChanged.connect(
            self.countdown_time_changed
        )
        
        countdown_layout = QHBoxLayout()
        countdown_layout.addWidget(self.countdown_checkbox)
        countdown_layout.addWidget(self.countdown_combobox,
                                   alignment=Qt.AlignmentFlag.AlignRight)

        
        self.negative_numbers = QCheckBox()
        self.negative_numbers.setText('Negative numbers')
        self.negative_numbers.setChecked(True)
        self.negative_numbers.stateChanged.connect(
            self.negative_numbers_state_changed
        )
        
        self.addition = QCheckBox()
        self.addition.setText('Addition')
        self.addition.setChecked(True)
        self.addition.stateChanged.connect(self.operators_state_changed)
        
        self.subtraction = QCheckBox()
        self.subtraction.setText('Subtraction')
        self.subtraction.setChecked(True)
        self.subtraction.stateChanged.connect(self.operators_state_changed)
        
        self.multiplication = QCheckBox()
        self.multiplication.setText('Multiplication')
        self.multiplication.stateChanged.connect(self.operators_state_changed)
        
        self.division = QCheckBox()
        self.division.setText('Division')
        self.division.setEnabled(False)
        
        self.addition_numbers_label = QLabel()
        self.addition_numbers_label.setFont(self.font_secondary)
        self.addition_numbers_label.setText(
            f'{self.numbers_dict['negative']['normal']['+']}'
        )
        self.addition_numbers_label.setStyleSheet('color: black;')
        
        self.subtraction_numbers_label = QLabel()
        self.subtraction_numbers_label.setFont(self.font_secondary)
        self.subtraction_numbers_label.setText(
            f'{self.numbers_dict['negative']['normal']['-']}'
        )
        self.subtraction_numbers_label.setStyleSheet('color: black;')
        
        self.multiplication_numbers_label = QLabel()
        self.multiplication_numbers_label.setFont(self.font_secondary)
        self.multiplication_numbers_label.setText(
            f'{self.numbers_dict['negative']['normal']['*']}'
        )
        self.multiplication_numbers_label.setStyleSheet('color: gray;')
        
        self.division_numbers_label = QLabel()
        self.division_numbers_label.setText('[...]')
        self.division_numbers_label.setStyleSheet('color: gray;')
        
        
        addition_layout = QHBoxLayout()
        addition_layout.addWidget(self.addition)
        addition_layout.addWidget(
            self.addition_numbers_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        subtraction_layout = QHBoxLayout()
        subtraction_layout.addWidget(self.subtraction)
        subtraction_layout.addWidget(
            self.subtraction_numbers_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        multiplication_layout = QHBoxLayout()
        multiplication_layout.addWidget(self.multiplication)
        multiplication_layout.addWidget(
            self.multiplication_numbers_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        division_layout = QHBoxLayout()
        division_layout.addWidget(self.division)
        division_layout.addWidget(
            self.division_numbers_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        operators_layout = QVBoxLayout()
        operators_layout.addLayout(addition_layout)
        operators_layout.addLayout(subtraction_layout)
        operators_layout.addLayout(multiplication_layout)
        operators_layout.addLayout(division_layout)
        
        self.operators = {
            '+': True,
            '-': True,
            '*': False,
            # '/': False,
        }
        self.operators_list = [k for k, v in self.operators.items() if v]
        
        
        self.generated_numbers_label = QLabel()
        self.generated_numbers_label.setText('Generated numbers:')
        
        
        settings_layout = QVBoxLayout()
        settings_layout.addLayout(logging_settings_layout)
        settings_layout.addWidget(Separator('h', 2))
        settings_layout.addLayout(difficulty_layout)
        settings_layout.addLayout(countdown_layout)
        settings_layout.addWidget(Separator('h'))
        settings_layout.addWidget(self.negative_numbers)
        settings_layout.addWidget(Separator('h'))
        settings_layout.addLayout(operators_layout)
        settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop
                                     | Qt.AlignmentFlag.AlignLeft)
        
        
        self.timer_label = QLabel()
        self.timer_label.setText('00:00')
        self.timer_label.setFont(self.font_primary)
        
        self.result_label = QLabel()
        self.result_label.setText(
            f'Result:  {self.right_answers} - {self.wrong_answers} = '
        )
        self.result_label.setFont(self.font_primary)
        
        self.score_label = QLabel()
        self.score_label.setText(f'{self.score}')
        self.score_label.setFont(self.font_primary)
        
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.score_label)
        result_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        topbar_layout = QHBoxLayout()
        topbar_layout.addLayout(result_layout)
        topbar_layout.addSpacing(20)
        topbar_layout.addWidget(self.timer_label,
                                alignment=Qt.AlignmentFlag.AlignRight)
        
        
        self.countdown = QProgressBar()
        self.countdown.setTextVisible(False)
        # self.countdown.setValue(75)
        
        self.countdown_label = QLabel()
        self.countdown_label.setFont(self.font_primary_bold)
        self.countdown_label.setText('0.00')
        self.countdown_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.countdown_label.setVisible(False)
        
        self.countdown_layout = QVBoxLayout()
        self.countdown_layout.addWidget(self.countdown)
        # self.countdown_layout.addSpacing(-28)
        self.countdown_layout.addWidget(self.countdown_label)
        # self.countdown_layout.insertSpacing(1, 28)
        
        
        self.example_label = QLabel()
        self.example_label.setText('example')
        self.example_label.setFont(self.font_primary)
        
        self.equal_label = QLabel(text=' = ')
        self.equal_label.setFont(self.font_primary)
        
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText('result')
        self.user_input.setFont(self.font_primary)
        self.user_input.setMaxLength(10)
        self.user_input.returnPressed.connect(self.check_example)
        
        example_layout = QHBoxLayout()
        example_layout.addWidget(
            self.example_label,
        )
        example_layout.addWidget(
            self.equal_label,
        )
        example_layout.addWidget(
            self.user_input,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        example_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.start_button = QPushButton()
        self.start_button.setCheckable(True)
        self.start_button.setText('Start')
        self.start_button.clicked.connect(self.start)
        
        
        self.recent_examples_label = QLabel()
        self.recent_examples_label.setText('Recent solved examples:')
        
        self.recent_examples = QListWidget()
        self.recent_examples.setMaximumWidth(240)
        
        recent_examples_layout = QVBoxLayout()
        recent_examples_layout.addWidget(
            self.recent_examples_label,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        recent_examples_layout.addWidget(
            self.recent_examples,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(topbar_layout)
        main_layout.addWidget(Separator('h', 2),
                              alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(self.countdown_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(example_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.start_button,
                              alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addSpacing(10)
        main_layout.addWidget(Separator('h', 2))
        main_layout.addLayout(recent_examples_layout)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop
                                 | Qt.AlignmentFlag.AlignHCenter)
        
        
        layout = QHBoxLayout()
        layout.addLayout(settings_layout)
        layout.addWidget(Separator('v', 2))
        layout.addLayout(main_layout)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    
    def logging_state_changed(self):
        self.logging: bool = self.logging_checkbox.isChecked()
        print(f'{self.logging = }')
    
    def update_current_gen_nums_dict(self):
        self.current_gen_nums_dict = {
            '+': self.numbers_dict[self.num_state][self.diff]['+'],
            '-': self.numbers_dict[self.num_state][self.diff]['-'],
            '*': self.numbers_dict[self.num_state][self.diff]['*'],
        }
        
        self.addition_numbers_label.setText(
            str(self.current_gen_nums_dict['+'])
        )
        self.subtraction_numbers_label.setText(
            str(self.current_gen_nums_dict['-'])
        )
        self.multiplication_numbers_label.setText(
            str(self.current_gen_nums_dict['*'])
        )
    
    def difficulty_state_changed(self, difficulty: str):
        if difficulty == 'Easy':
            self.diff = difficulty.lower()
            
            self.countdown_checkbox.setChecked(False)
            self.countdown_checkbox.setEnabled(False)
            self.countdown_checkbox.setText('Countdown (Hard)')
        
        elif difficulty == 'Normal':
            self.diff = difficulty.lower()
            
            self.countdown_checkbox.setChecked(False)
            self.countdown_checkbox.setEnabled(False)
            self.countdown_checkbox.setText('Countdown (Hard)')
        
        elif difficulty == 'Hard':
            self.diff = difficulty.lower()
            
            self.countdown_checkbox.setEnabled(True)
            self.countdown_checkbox.setText('Countdown')
        
        self.update_current_gen_nums_dict()
        
        if self.logging:
            print(f'Difficulty: {difficulty}')
    
    def countdown_state_changed(self, state: int):
        if state:
            self.countdown_combobox.setEnabled(True)
            
            self.countdown_label.setVisible(True)
            self.countdown_layout.insertSpacing(1, -28)
            
            if self.logging:
                print('Countdown: Enabled')
        else:
            self.countdown_combobox.setEnabled(False)
            
            self.countdown_label.setVisible(False)
            self.countdown_layout.insertSpacing(1, 28)
            
            if self.logging:
                print('Countdown: Disabled')
    
    def countdown_time_changed(self, index):
        if self.logging:
            print(f'Countdown time: {self.countdown_time_list[index]}s')
    
    def negative_numbers_state_changed(self, state: int):
        if state:
            self.num_state = 'negative'
            
            if self.logging:
                print('Negative numbers: ON')
        else:
            self.num_state = 'positive'
            
            if self.logging:
                print('Negative numbers: OFF')
        
        self.update_current_gen_nums_dict()
    
    def operators_state_changed(self):
        addition_state: bool = self.addition.isChecked()
        subtraction_state: bool = self.subtraction.isChecked()
        multiplication_state: bool = self.multiplication.isChecked()
        
        if addition_state:
            self.addition_numbers_label.setStyleSheet('color: black;')
            self.operators['+'] = True
        else:
            self.addition_numbers_label.setStyleSheet('color: gray;')
            self.operators['+'] = False
        
        if subtraction_state:
            self.subtraction_numbers_label.setStyleSheet('color: black;')
            self.operators['-'] = True
        else:
            self.subtraction_numbers_label.setStyleSheet('color: gray;')
            self.operators['-'] = False
        
        if multiplication_state:
            self.multiplication_numbers_label.setStyleSheet('color: black;')
            self.operators['*'] = True
        else:
            self.multiplication_numbers_label.setStyleSheet('color: gray;')
            self.operators['*'] = False
        
        self.operators_list = [k for k, v in self.operators.items() if v]
        
        if self.operators_list:
            self.start_button.setEnabled(True)
        else:
            self.start_button.setEnabled(False)
        
        if self.logging:
            print(f'{self.operators_list = }')
    
    def start(self, state):
        settings_list = [
            self.logging_checkbox,
            self.difficulty,
            self.negative_numbers,
            self.addition,
            self.subtraction,
            self.multiplication,
        ]
        
        if self.difficulty.currentText() == 'Hard':
            settings_list.append(self.countdown_checkbox)
            
            if self.countdown_checkbox.isChecked():
                settings_list.append(self.countdown_combobox)
        
        if state:
            # self.user_input.setFocus()
            # self.start_button.setText('Stop')
            
            process = threading.Thread(
                target=self.start_countdown,
                # args=[], # Для передачи аргументов в функцию
            )
            process.start()
            
            for setting in settings_list:
                setting.setEnabled(False)
            
            if self.logging:
                print(f'Test: Started')
        else:
            # self.user_input.clearFocus()
            self.start_button.setText('Start')
            
            for setting in settings_list:
                setting.setEnabled(True)
            
            if self.logging:
                print(f'Test: Stopped')
    
    def start_countdown(self):
        # for i in sorted(range(1, 4), reverse=True):
        #     if self.start_button.isChecked():
        #         self.start_button.setText(f'Stop ({i}{'.'*i})')
        #         time.sleep(0.5)
        #         QApplication.processEvents()
        #     else:
        #         break
        
        if self.start_button.isChecked():
            self.user_input.setFocus()
            self.start_button.setText('Stop')
            
            self.right_answers = 0
            self.wrong_answers = 0
            self.score = 0
            
            self.result_label.setText(
                f'Result:  {self.right_answers} - {self.wrong_answers} = '
            )
            self.score_label.setText(f'{self.score}')
            
            self.generate_examples()
    
    def generate_examples(self):
        number_1: int
        number_2: int
        operator: str = random.choice(self.operators_list)
        gen_nums_range: list
        
        if operator == '+':
            gen_nums_range = self.current_gen_nums_dict['+']
            number_1 = random.randint(*gen_nums_range)
            number_2 = random.randint(*gen_nums_range)
            self.result = number_1 + number_2
            
            if number_2 < 0:
                self.example_label.setText(f'{number_1} + ({number_2})')
            else:
                self.example_label.setText(f'{number_1} + {number_2}')
        
        elif operator == '-':
            gen_nums_range = self.current_gen_nums_dict['-']
            number_1 = random.randint(*gen_nums_range)
            number_2 = random.randint(*gen_nums_range)
            self.result = number_1 - number_2
            
            if number_2 < 0:
                self.example_label.setText(f'{number_1} - ({number_2})')
            else:
                self.example_label.setText(f'{number_1} - {number_2}')
        
        elif operator == '*':
            gen_nums_range = self.current_gen_nums_dict['*']
            number_1 = random.randint(*gen_nums_range)
            number_2 = random.randint(*gen_nums_range)
            self.result = number_1 * number_2
            
            if number_2 < 0:
                self.example_label.setText(f'{number_1} * ({number_2})')
            else:
                self.example_label.setText(f'{number_1} * {number_2}')
    
    def check_example(self):
        try:
            user_input = int(self.user_input.text())
        except ValueError as e:
            user_input = 0
        
        recent_example_text = ''
        
        if user_input == self.result:
            self.right_answers += 1
            recent_example_text = (
                f'[+] {self.example_label.text()} = {user_input}'
            )
        else:
            self.wrong_answers += 1
            recent_example_text = (
                f'[-] {self.example_label.text()} = '
                f'{user_input} ({self.result})'
            )
        
        self.score = self.right_answers - self.wrong_answers
        
        self.result_label.setText(
            f'Result:  {self.right_answers} - {self.wrong_answers} = '
        )
        self.score_label.setText(str(self.score))
        self.recent_examples.insertItem(0, recent_example_text)
        self.user_input.clear()
        
        self.generate_examples()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
QSS = '''
QWidget {
    background-color: #2b2b2b;  /* Темно-серый фон для всех виджетов */
    font-family: Arial, sans-serif;  /* Шрифт Arial */
    font-size: 14px;  /* Размер шрифта */
    color: #f0f0f0;  /* Светло-серый текст для всех виджетов */
}

QLabel {
    color: #c0c0c0;  /* Серый текст для меток */
    font-weight: bold;  /* Жирный текст */
}

QListWidget {
    background-color: #3a3a3a;  /* Темный фон для списков */
    border: 2px solid #555555;  /* Темно-серая рамка */
    padding: 5px;  /* Внутренний отступ */
    color: #e0e0e0;  /* Светло-серый цвет текста */
}

QPushButton {
    background-color: #444444;  /* Темно-серый фон для кнопок */
    color: #f0f0f0;  /* Светло-серый текст */
    border: 2px solid #666666;  /* Темная рамка */
    padding: 10px;  /* Внутренний отступ */
    border-radius: 5px;  /* Округлённые углы */
   
}

QPushButton:hover {
    background-color: #555555;  /* Более светлый серый при наведении */
 
}

QLineEdit {
    background-color: #3a3a3a;  /* Темный фон для полей ввода */
    border: 2px solid #555555;  /* Темно-серая рамка */
    padding: 5px;  /* Внутренний отступ */
    color: #f0f0f0;  /* Светло-серый текст */
    border-radius: 3px;  /* Округлённые углы */
    
}

QTextEdit {
    background-color: #3a3a3a;  /* Темный фон для многострочных полей */
    border: 2px solid #555555;  /* Темно-серая рамка */
    padding: 5px;  /* Внутренний отступ */
    color: #f0f0f0;  /* Светло-серый текст */
    border-radius: 3px;  /* Округлённые углы */
   
}

QListWidget:item {
    padding: 10px;  /* Внутренний отступ для элементов списка */
    color: #f0f0f0;  /* Светло-серый текст для элементов */
}

QListWidget:item:selected {
    background-color: #555555;  /* Светло-серый фон для выбранных элементов */
    color: #f0f0f0;  /* Светло-серый текст для выбранных элементов */
    border-radius: 3px;  /* Округлённые углы */
}
'''
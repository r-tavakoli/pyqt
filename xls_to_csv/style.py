CONVERT_BUTTON_STYLE = '''
    QPushButton {
        height: 20px;
        width: 70px;
        font-size: 14px;
        font-family: 'Fixedsys';
        transition: all .5s ease;
        color: #0f0f0f;
        border: 1px solid #22577A;
        text-transform: uppercase;
        text-align: center;
        background-color: transparent;
        padding: 5px;
        outline: none;
        border-radius: 4px;
    }
    QPushButton:hover {
        color: #001F3F;
        background-color: #93B5C6;
    }
'''

LINE_EDIT_STYLE = '''
    QLineEdit {
        font-size: 18px;
        font-family: 'Fixedsys';  
        line-height: 1;
        height: 30px;
        border: 1px solid #22577A;
        border-radius: 4px;
    }
'''

LABEL_STYLE = '''
    QLabel {
        font-size: 14px;
        font-family: 'Fixedsys';
    }    
'''

# progress bar style
progress_bar_style = '''
    QProgressBar {
        border: solid grey;
        min-height: 15px;
        max-height: 15px;
    }
    QProgressBar::chunk {
        background-color: #05B8CC;
        width: 1px
    }
'''

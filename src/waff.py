#!/usr/bin/python3
from flask import Flask
from modules import staff
import os
#################################################################################
def get_text(file_path: str) -> str:
    '''
        Get text from file complete path
    '''
    content: str = ''
    
    with open(file_path, 'r') as text:
        for line in text.readlines():
            content += line

    return content

def make_empty_musical_staff() -> str:

    render_web: str = '<style type = text/css>' + get_text('fixing.css').replace('\n', '') + '</style>'

    key_text: str = key()
    render_web += f'<span class = {key_text.partition('s/')[2][0]}-key>{key_text}</span><span class = \'lines secondLine\'>{staff.get_time_signature()}</span>'
    
    for staff_line in [5, 4, 3, 2, 1]:
        # Later Use After method with Javascript for add notes
        render_web += f'<hr id = staff_line_{staff_line}/>'
        
    return render_web

def key():
    return f'<img src = \'{staff.get_key()}\'/>'
def flag() -> str:
    '''
        Give the note ceil ~
    '''
    return f'<span class = flag><img src = \'{staff.get_restant_flag()}\'/></span>'

def note_head() -> str:
    '''
        Give head
    '''
    return f'<span class = heading>\t<img src = \'{staff.get_restant_head()}\'/></span>'

def stem() -> str:
    stems: str = ''
    
    for sign in range(0, staff.divitions + 1):
        stems += f'<span class = stem><img src = \'{staff.get_restant_stem()}\'/></span>'
        if staff.restant_time_16['note'] == 0:
            break

    return stems

def combine_second_list(repeat_second_n_times: int = 1, first: list = [0], second: list = [1]) -> list:
    '''
        Give a list with elements in first list
        with n times all elements from second list
        repeated
    '''
    combined: list = first
    
    for combine in range(1, repeat_second_n_times + 1):
        combined = combined.__add__(second)

    return combined
################################################################################
waff_app = Flask(__name__)
@waff_app.route('/')
def main_section() -> str:
    '''
        Initial page of app
    '''
    page: str = '<script type = "text/javascript">'
    seconds: int = 1
    for step in combine_second_list(4, [make_empty_musical_staff], [note_head, stem, flag]):
        # Load to JavaScript timeout function adding more seconds to last function
        page += f'\nsetTimeout(() => \u007B document.write("{step()}"); \u007D, {seconds}000);'
        # Each second more execute next step
        seconds += 1
    
    page += '\n</script>'
    
    return page

os.system('rm -R ./__pycache__ && rm -R ./modules/__pycache__')
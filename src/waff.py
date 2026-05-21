#!/usr/bin/python3
from flask import Flask
from modules import staff
import os
#################################################################################
def make_empty_musical_staff() -> str:

    render_web: str = '<style type = text/css>body {padding: 5em;} div {margin-left: -1.5em;} .flag {margin-top: -2.7em;} .stem {margin-top: -3em;} .heading {margin-top: -1em;}</style>'

    for staff_line in [5, 4, 3, 2, 1]:
        # Later Use After method with Javascript for add notes
        render_web += f'<hr id = staff_line_{staff_line}/>'
        
    return render_web

def flag() -> str:
    '''
        Give the note ceil ~
    '''
    return f'<p class = flag><img src = {staff.get_restant_flag()} alt = FLAG></img></p>'

def note_head() -> str:
    '''
        Give head
    '''
    return f'{staff.get_time_signature()}<p class = heading><img src = {staff.get_restant_head()} alt = HEAD></img></p>'

def stem() -> str:
    return f'<p class = stem><img src = {staff.get_restant_stem()} alt = STEM></img></p>'
################################################################################
waff_app = Flask(__name__)
@waff_app.route('/')
def main_section() -> str:
    '''
        Initial page of app
    '''
    page: str = '<script type = "text/javascript">'
    seconds: int = 1
    
    for step in [make_empty_musical_staff, note_head, stem, flag]:
        # Load to JavaScript timeout function adding more seconds to last function
        page += f'\nsetTimeout(() => \u007B document.write("{step()}"); \u007D, {seconds}000);'
        # Each second more execute next step
        seconds += 1
    
    page += '\n</script>'
    
    return page

os.system('rm -R ./__pycache__ && rm -R ./modules/__pycache__')
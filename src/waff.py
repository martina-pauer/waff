#!/usr/bin/python3
from flask import Flask

waff_app = Flask(__name__)

@waff_app.route('/')
def make_empty_musical_staff() -> str:

    render_web: str = '<style type = "text/css">body {padding: 5em;} </style>'

    for staff_line in [5, 4, 3, 2, 1]:
        # Later Use After method with Javascript for add notes
        render_web += f'<hr id = staff_line_{staff_line}/>'

    return render_web
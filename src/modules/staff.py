def get_note_text() -> str:
    '''
        Implement steps from 1 to 3
        in the algorithm.
    '''
    import random

    natural_notes: list[str] = [
                        'D3', 'E3', 'F3',
                        'G3', 'A3', 'B3',
                        'C4', 'D4', 'E4',
                        'F4', 'G4', 'A4',
                        'B4', 'C5', 'D5'
                        'E5', 'F5', 'G5',
                        'A5', 'B5',
                        'C5', 'D6'
                    ]

    natural_note = random.choice(natural_notes)  

    del natural_notes, random     

    natural_note += ' '

    return natural_note         
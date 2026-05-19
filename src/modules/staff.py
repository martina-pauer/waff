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

def get_interval_note(grade: str, first_note: str) -> str:
    '''
        From Grade in Roman Numbers and type with the first interval note get the following using distances.
    '''
    distances: dict[str, str] = {
                        'IIm': '1st', 
                        'IIM': '2st', 
                        'IIIm': '3st', 
                        'IIIM': '4st', 
                        'IVJ': '5st', 
                        'Vdim': '6st', 
                        'VJ': '7st', 
                        'Vaug': '8st'
                    }
    natural_notes: list[str] = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
	# Use only note name, not the pitch
    second_note: str = first_note[0]
	# Calc Semitones to Use
    semitones: str = distances[grade]
    # Save the pitch for modify
    octave: int = int(first_note[1])
    
    for note in range(natural_notes.index(first_note[0]), natural_notes + 1):
         # Use next note until get the note after all semitones
         second_note = natural_notes[note]
         # Discount notes, when get zero restart for loop
         if semitones == '0st':
            second_note = f'{natural_notes[note]}{octave}'
            break
         elif ['C', 'D', 'F', 'G', 'A'].__contains__(natural_notes[note]):
             semitones = f'{int(semitones[0]) - 2}st'
         elif second_note == 'E':
             semitones = f'{int(semitones[0] - 1)}st'
         else:
           # Restart loop
           note = natural_notes.index(first_note[0])
           # Count one octave more
           octave += 1
    # Only work for ascendent intervals       
    return second_note
# Define Global variables for use for get rhythm patterns image paths
time: int = 4
divitions: int = 4
prefix: str = 'https://github.com/martina-pauer/waff/raw/e07d16474810f6deb36066c7091ee308a0142f08/images/'
# Define Global Functions
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

def get_time_signature() -> str:
    '''
       Get fraction that indicate
       the kind of rhythm
    '''
    import random
    # First select pulse four or eight in the floor
    options: list[int] = [4, 8]
    time: int = random.choice(options)
    # Second Use Divitions valid for pulse time
    if (time == 4):
        # 3 Simple time signature & one Compound (Binary + Ternary)
        options: list[int] = [2, 3, 4, 12]
    else:
        # Compound time signature (Ternary)
        options: list[int] = [6, 9, 12]
            
    divitions: int = random.choice(options)
    del options
    # Give divitions over time in musical time signature web format
    return f'<div>{divitions}<br />{time}</div>'

def get_restant_head() -> str:
    heads: list[str] =      [
                                f'{prefix}note_head_2_1.svg',
                                f'{prefix}note_head_4.svg'
                            ]

    import random
    
    head: str = random.choice(heads)

    return head

def get_restant_flag() -> str:
    options: list[str] =    [
                                f'{prefix}8_flag.svg',
                                f'{prefix}16_flag.svg',
                                f'{prefix}group_8.svg',
                                f'{prefix}group_16.svg'
                            ]
    
    import random
    
    choosen: str = random.choice(options)
    del options, random
    
    return choosen

def get_restant_stem() -> str:
    return f'{prefix}stem.svg'    
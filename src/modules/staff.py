# Define variables for use for get rhythm patterns image paths
time: int = 4
divitions: int = 4
restant_time_16: dict[str, int] = {'note': divitions * 4}
prefix: str = 'https://github.com/martina-pauer/waff/raw/dd9ea7879db24a52ea121996936deda48a987b64/'
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
            
    divs: int = random.choice(options)
    del options
    # When get divitions get pattern duration in 16 note
    if (time == 8):
        # each 8 note time divition has two 16 notes
        restant_time_16['note'] = divitions * 2
    else:
        # each 4 note has four 16 notes
        restant_time_16['note'] = divs * 4    
    # Give divitions over time in musical time signature web format
    return f'<div>{divitions}<br />{time}</div>'

def get_restant_head() -> str:
    heads: list[str] =      [
                                f'{prefix}images/note_head_2_1.svg',
                                f'{prefix}images/note_head_4.svg'
                            ]

    import random
    
    head: str = random.choice(heads)
    # Fix Mistakes of ryhthm space
    if (head.__contains__('2') and (restant_time_16['note'] <= 2)):
        head = f'{prefix}images/note_head_4.svg'
    # Discount time used in 16 note unit
    if (head.__contains__('4') and (restant_time_16['note'] >= 4)):
        # Each 4 note decrease four 16 note
        restant_time_16['note'] -= 4
    elif (restant_time_16['note'] >= 8):
        # Each 2 note decrease eight 16 note
        restant_time_16['note'] -= 8
        
    return head

def get_restant_flag() -> str:
    options: list[str] =    [
                                f'{prefix}images/8_flag.svg',
                                f'{prefix}images/16_flag.svg',
                                f'{prefix}images/group_8.svg',
                                f'{prefix}images/group_16.svg'
                            ]
    
    import random
    
    choosen: str = random.choice(options)
    # Select options that fit in time
    if ((choosen.__contains__('8')) and (restant_time_16['note'] < 4)):
        choosen = options[0]    
        del options, random
    elif ((choosen == '8_flag.svg') and (restant_time_16['note'] >= 2)):
        # Discount two 16 notes
        restant_time_16['note'] -= 2
    elif ((choosen == '16_flag.svg') and (restant_time_16['note'] >= 1)):
        # each 16 note decrease one 16 note
        restant_time_16['note'] -= 1    
    elif ((choosen == 'group_8.svg') and (restant_time_16['note'] >= 4)):
        # two 8 notes decrease four 16 notes
        restant_time_16['note'] -= 4
    elif (restant_time_16['note'] >= 2):
        # each two 16 notes decrease four 16 notes
        restant_time_16['note'] -= 4       
        
    return choosen

def get_restant_stem() -> str:
    return f'{prefix}images/stem.svg'

def get_key() -> str:
    '''
        Give the random musical
        key signatur
    '''
    import random

    sigantures: list[str] = [
                                f'{prefix}images/C-third_line-key.svg',
                                f'{prefix}images/F-fourth_line-key.svg',
                                f'{prefix}images/G-second_line-key.svg'
                            ]

    return random.choice(sigantures)
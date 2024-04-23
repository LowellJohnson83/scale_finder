input_prog = "Am E"

# ------------------------------------------------------------------------------------------------

note_names = [
    "C" , "C♯", "D♭", "D" , "D♯",
    "E♭", "E" , "F" , "F♯", "G♭",
    "G" , "G♯", "A♭", "A" , "A♯",
    "B♭", "B" 
]

dict_note_to_chrom = {
    "C" : 0, "C♯": 1,
    "D♭": 1, "D" : 2, "D♯": 3,
    "E♭": 3, "E" : 4,
    "F" : 5, "F♯": 6,
    "G♭": 6, "G" : 7, "G♯": 8,
    "A♭": 8, "A" : 9, "A♯":10,
    "B♭" :10, "B" :11
}

dict_modes_to_chroms = {
    "Major": [0,2,4,5,7,9,11], "Ionian": [0,2,4,5,7,9,11], "Dorian": [0,2,3,5,7,9,10],
    "Phrygian": [0,1,3,5,7,8,10], "Lydian": [0,2,4,6,7,9,11], "Mixolydian": [0,2,4,5,7,9,10],
    "Natural Minor": [0,2,3,5,7,8,10], "Aeolian": [0,2,3,5,7,8,10], "Locrian": [0,1,3,5,6,8,10],

    "Harmonic Minor": [0,2,3,5,7,8,11], "Locrian ♮6": [0,1,3,5,6,9,10],
    "Major Augmented": [0,2,4,5,8,9,11], "Dorian ♯4 ('Romanian Minor')": [0,2,3,6,7,9,10],
    "Phrygian Dominant": [0,1,4,5,7,8,10], "Lydian ♯2": [0,3,4,6,7,9,11],
    "Ultralocrian (or 'Altered Diminished Scale')": [0,1,3,4,6,8,9],

    "Melodic Minor (or 'Jazz Minor')": [0,2,3,5,7,9,11], "Dorian ♭2": [0,1,3,5,7,9,10],
    "Lydian Augmented": [0,2,4,6,8,9,11], "Lydian Dominant (or 'Acoustic Scale')": [0,2,4,6,7,9,10],
    "Mixolydian ♭2 (or 'Aeolian Dominant')": [0,2,4,5,7,8,10], "Locrian ♮2": [0,2,3,5,6,8,10],
    "Superlocrian (or 'Altered Scale')": [0,1,3,4,6,8,9],

    "Harmonic Major": [0,2,4,5,7,8,11], "Dorian Diminished": [1,2,3,4,6,9,10],
    "Phrygian Altered": [0,1,3,4,6,8,10], "Lydian Minor": [0,2,3,6,7,9,11],
    "Mixolydian ♭2": [0,1,4,5,7,9,10], "Lydian Augmented ♯2": [0,3,4,6,8,9,11],
    "Locrian ♭♭7": [0,1,3,5,6,8,9],
}

dict_qual_to_chroms = {
    " "     : [ 0,  4,  7], "maj"   : [ 0,  4,  7], "M"     : [ 0,  4,  7], 
    "m"     : [ 0,  3,  7], "min"   : [ 0,  3,  7], "-"     : [ 0,  3,  7],
    "dim"   : [ 0,  3,  6], "°"     : [ 0,  3,  6], "aug"   : [ 0,  4,  8], "+"     : [ 0,  4,  8],
    "maj7"  : [0, 4, 7,11], "m7"    : [0, 3, 7,10], "min7"  : [0, 3, 7,10], "7"     : [0, 4, 7,10],
    "maj7+" : [0, 4, 8,11], "M7+"   : [0, 4, 8,11],
    "mmaj7" : [0, 3, 7,11], "mM7"   : [0, 3, 7,11], "mM7"   : [0, 3, 7,11], 
    "7"     : [0, 4, 7,10], "dom7"  : [0, 4, 7,10],
    "m7b5"  : [0, 3, 6,10], "ø"     : [0, 3, 6,10], 
    "dim7"  : [0, 3, 6, 9], "°7"    : [0, 3, 6, 9],
}

# Convert input string ('input_progression') into list of strings for chords ('list_progression') 
input_prog = input_prog.replace(",", " ").replace("/", " ").replace(".", "").replace("b", "♭").replace("#", "♯")
list_prog = input_prog.split(" ")

# Remove zero-length elements in list
while ("" in list_prog):
    list_prog.remove("")

print(f"'list_progression':\t{list_prog}")

# Add an extra space after letter if letter (A to G) is on its own (Major chord)
for chord in range(len(list_prog)):
    print(f"'list_progression[chord]' is:\t'{list_prog[chord]}'")
    # if "♭" or "♯" in str(list_prog[chord]):
    if list_prog[chord][0] in note_names:
        if len(list_prog[chord]) == 1:
            # print(f"length of {list_prog[chord]} is:\t1")
            # print(f"'list_progression' before adding space:\t {list_prog}")
            str_chord = list_prog[chord][0] + " "
            # print(f"'str_chord' is:\t'{str_chord}'")
            # print(f"'list_progression' after adding space:\t {list_prog}")
            list_prog[chord] = str_chord
        elif list_prog[chord][1] in ["♭", "♯"]:
            # print(f"length of {list_prog[chord]} is:\t2")
            # print(f"'list_progression' before adding space:\t {list_prog}")
            str_chord = list_prog[chord][0] + " "
            # print(f"'str_chord' is:\t'{str_chord}'")
            # print(f"'list_progression' after adding space:\t {list_prog}")
            list_prog[chord] = str_chord

print(f"'list_progression':\t{list_prog}")
print(f"'list_progression[0]' is:\t'{list_prog[0]}'")

# Create a list for int notation
list_int_notation = []
int_first_note = int(dict_note_to_chrom[str(list_prog[0]).replace(" ", "")])

# print(f"'int_first_note':\t{int_first_note}")

# (For each string chord in 'list_prgression')
for chord in list_prog:
    # Split into note and quality
    if chord[1] in ["♭", "♯"]: 
        note = str(chord)[:2]
        if len(chord) >= 2:
            quality = str(chord)[2:]
        else:
            quality = " "
    else:
        note = str(chord)[:1]
        if len(chord) >= 1:
            quality = chord[1:]
        else:
            quality = " "
    # print(f"'chord':\t'{chord}'\t'note':\t'{note}'\t'quality':\t'{quality}'")
    chord_int_notation = [(i + dict_note_to_chrom[note] - int_first_note) % 12 for i in dict_qual_to_chroms[quality]]
    list_int_notation.append(chord_int_notation)
    
print(f"'list_int_notation' is:\t{list_int_notation}")

str_int_notation = str(list_int_notation).replace("[", "").replace("]", "").replace(",", "")

# print(f"'str_int_notation' is:\t{str_int_notation}")
# print(f"'type(str_int_notation)' is:\t{type(str_int_notation)}")

# Compile a list with all integeres of chromatic notes notes present in chord progression
ints_present = []
for sublist in list_int_notation:
    for chrom in sublist:
        print(f"'chrom':\t{chrom}")
        if chrom in range(12):
            if chrom not in ints_present:
                ints_present.append(chrom)
ints_present.sort()

print(f"'ints_present' (integers present) in chord progression:\t{ints_present}")

# Relat values to Scale Keys
matching_modes = []
for key, value in dict_modes_to_chroms.items():
    correct_count = 0
    for integer in ints_present:
        if integer in value:
            correct_count += 1
    if correct_count == len(ints_present):
        matching_modes.append(key)
        # print(f"Key is:\t{key}")

print(f"Matching Modes:\t{matching_modes}")
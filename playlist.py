
def ternary_search_song(playlist, song, offset=0):
    if not playlist:
        return -1
    n = len(playlist)
    third = n // 3

    left_part = playlist[:third]
    middle_part = playlist[third:2*third]
    right_part = playlist[2*third:]

    mid1_index = third - 1 if third > 0 else 0
    mid2_index = 2 * third - 1 if 2 * third > 0 else n - 1

    if playlist[mid1_index] == song:
        return offset + mid1_index
    if playlist[mid2_index] == song:
        return offset + mid2_index

    if song < playlist[mid1_index]:
        return ternary_search_song(left_part, song, offset)
    elif song > playlist[mid2_index]:
        return ternary_search_song(right_part, song, offset + 2 * third)
    else:
        return ternary_search_song(middle_part, song, offset + third)
playlist = [
    "A Sky Full of Stars",
    "Believer",
    "Blinding Lights",
    "Counting Stars",
    "Dance Monkey",
    "Happier",
    "Shape of You",
    "Someone Like You",
    "Uptown Funk",
    "Viva La Vida"
]

song_to_find = "Someone Like You"

index = ternary_search_song(playlist, song_to_find)
if index != -1:
    print(f"'{song_to_find}' found at index {index}.")
else:
    print(f"'{song_to_find}' not found in the playlist.")

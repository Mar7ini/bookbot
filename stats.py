#stats.py



def get_number_of_words(file_contents):
    word_count = file_contents.split()
    count = len(word_count)
    return count

def char_counter(file_contents):
    char_dict = {}
    lowered = file_contents.lower()
    for a in lowered:
        if a not in char_dict:
            char_dict[a] = 1
        else:
            char_dict[a] += 1    
    return char_dict

def sort_on(items):
    return items["num"]



def sorting_dict(char_dict):
    sortedd = []

    for ch in char_dict:
        if  ch.isalpha():
            ch_num = char_dict[ch]
            sortedd.append({"char": ch, "num": ch_num})
    sortedd.sort(reverse=True, key=sort_on)
    return sortedd
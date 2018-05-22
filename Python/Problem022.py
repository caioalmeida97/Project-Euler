letter_score = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':26,
}

def name_score(name_s):
    score = 0;
    for letter in name_s:
        score += letter_score[letter]
        # print(letter, letter_score[letter])
    return score;

def split_names(names):
    ret = [];
    for name in names.split(','):
        ret.append(name.strip("\""));
    return ret;

def calculate_score(names_file):
    names_list = split_names(names_file)
    names_list.sort();
    scores = [];
    final_score = 0;
    for element in names_list:
        score = name_score(element);
        final_score = score * (names_list.index(element) + 1);
        scores.append(final_score);
        print(element, score, final_score);
    return scores;

file = open("p022_names.txt", "r").read();
print(sum(calculate_score(file)));
# ;
# calculate_score(names);
# names2 = "\"CAIO\",\"ANDRE\",\"DOBERMANN\",\"BREAO\"";
# names3 = split_names(names2);
# calculate_score(names3);
# print(names)

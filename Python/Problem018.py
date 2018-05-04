class Element:
    def __init__(self, i, j, value):
        self.i = i;
        self.j = j;
        self.value = value;

def options(indexI, indexJ):
    return [indexI + 1, indexJ], [indexI + 1, indexJ + 1]

def nextElement(element):
    auxI, auxJ = element.i, element.j;
    opt = options(auxI, auxJ);
    opt2 = [getElement(opt[0][0], opt[0][1]), getElement(opt[1][0], opt[1][1])];
    return opt2[0] if opt2[0].value > opt2[1].value else opt2[1];
    # max(opt2[0].value, opt2[1].value);
    # options(i, j)[0][0] -> pos i of the first option
    # options(i, j)[0][1] -> pos j of the first option
    # options(i, j)[1][0] -> pos i of the second option
    # options(i, j)[1][1] -> pos j of the second option

def getElement(indexI, indexJ):
    for i in range(len(elements)):
        aux = elements[i];
        if aux.i == indexI and aux.j == indexJ:
            return aux;

triangle = [];
string = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.strip();

for line in string.splitlines():
    triangle.append([int(number) for number in line.split()]);

elements = [];
for row in range(len(triangle) - 1):
    for column in range(len(triangle[row])):
        elements.append(Element(row, column, triangle[row][column]))

# biggestSum = 0;
# sum = 0;
# actualPath = [];

# sum, actualPath = reverseSum(triangle, 0, 0);

# for i, j in enumerate(triangle[14]):
#     print(i, j)
# opt = options(0, 0);
# print(nextElement(elements[0]));h
print(nextElement(nextElement(elements[0])).value)

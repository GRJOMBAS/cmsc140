majorCourses = [
    "BIOL 130",
    "BIOL 150",
    "BIOL 280",
    "PHYS 141",
    "PHYS 151",
    "GEOL 110",
    "GEOS 210",
    "BIOL 650"
]
bioCourses = []

def courseToCode(listFrom):
    newList = []
    for item in range(len(listFrom)):
        curClass = listFrom[item].split()
        for code in curClass:
            if code.isnumeric():
                newList.append(int(code))
    return newList


bioCourses = courseToCode(majorCourses)
print(bioCourses)

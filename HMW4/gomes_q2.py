courses = {
    "CMSC 140": {
        "- Course Name:": "INTRO TO PYTHON PROGRAMMING",
        "- Proffesor:": "Acacia Ackles",
        "- Units:": 6,
        "- Meets:": ["M 9:50 - 11:00", "W 9:50 - 11:00", "R 10:25 - 12:10"] },

    "CMSC 150": {
        "Course Name:": "INTRO TO COMPUTER SCIENCE",
        "- Proffesor:": "Kurt Krebsbach",
        "- Units:": 6,
        "- Meets:": ["M 13:50 - 15:00", "T 10:25 - 12:10", "W 13:50 - 15:00"] },
    
    "FRST 100": {
        "- Course Name:": "FIRST YEAR STUDIES",
        "- Proffesor:": "Rose Theisen",
        "- Units:": 6,
        "- Meets:": ["M 11:10 - 12:20", "W 11:10 - 12:20", "F 11:10 - 12:20"]
    }
}
# isinstance()
for course, info in courses.items():
    print("Course Code:", course)
    for key, val in info.items():
        if isinstance(val, list):
            print(key)
            for time in val:
                print("\t-",time)
        else:
            print(key, val)
    print("---\n")
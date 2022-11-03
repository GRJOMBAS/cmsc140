student_grades = [
    [89, 90, 77],
    [58, 77, 80],
    [99, 100, 94],
    [29, 9, 0],
    [100, 88, 92],
    [82, 84, 87],
    [74, 68, 88]
]
students = {"Anna": [89, 90, 77],
    "Betsy": [58, 77, 80],
    "Carol": [99, 100, 94],
    "Delilah": [29, 9, 0],
    "Emily": [100, 88, 92],
    "Francesca": [82, 84, 87],
    "Gemini": [74, 68, 88]
    }

student_names = ["Anna",
    "Betsy",
    "Carol",
    "Delilah",
    "Emily",
    "Francesca",
    "Gemini"
    ]

student_averages = {"Anna": [],
    "Betsy": [],
    "Carol": [],
    "Delilah": [],
    "Emily": [],
    "Francesca": [],
    "Gemini": []}

for name, grades in students.items():    
    avg = sum(grades)/len(grades)
    students[name] = avg

print(students)
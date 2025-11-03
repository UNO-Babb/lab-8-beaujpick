#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def year_abbrev(year):
    return {
        "Freshman": "FR",
        "Sophomore": "SO",
        "Junior": "JR",
        "Senior": "SR"
    }.get(year, "")

def create_userid(first, last, student_id):
    # Last 3 digits of ID
    last3 = ''.join([c for c in student_id if c.isdigit()])[-3:]
    # Add X if last name shorter than 5
    if len(last) < 5:
        last += "X"
    return f"{first[0].lower()}{last.lower()}{last3}"

def major_code(major, year):
    code = major[:3].upper()
    return f"{code}-{year_abbrev(year)}"

input_file = "names.dat"
output_file = "StudentList.csv"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    outfile.write("Last Name,First Name,UserID,Major-Year\n")
    
    for line in infile:
        parts = line.strip().split()
        if len(parts) < 6:
            continue

        first = parts[0]
        last = parts[1]
        student_id = parts[3]  # Example: 443-13-3556
        year = parts[-2]       # Example: Freshman
        major = " ".join(parts[-1:])  # May be multiple words

        # Adjust for multi-word majors
        if year not in ["Freshman", "Sophomore", "Junior", "Senior"]:
            continue  # Skip invalid lines

        major_index = parts.index(year) + 1
        major = " ".join(parts[major_index:])

        userid = create_userid(first, last, student_id)
        major_year = major_code(major, year)
        
        outfile.write(f"{last},{first},{userid},{major_year}\n")

print("✅ StudentList.csv created successfully!")

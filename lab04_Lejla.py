#Ime:Lejla Kadusic
#Datum:29.3.2026
#Lab 4 --- Python za FastAPI

#zadatak 1
student = {"ime": "Amina",
           "godina": 3, 
           "email": "ime.prezime@untz.ba",
           "prosjek": 8.5} 

print("Cijeli rječnik:", student)
print("Ime  studenta:",student["ime"])
student["aktivan"] = True
print("Rječnik nakon dodavanja  'aktivan':", student)

studenti = [
    {
        "ime": "Amina",
        "godina": 3,
        "email": "amina@gmail.com",
        "prosjek": 8.7,
        "aktivan": True
    },
    {
        "ime": "Emir",
        "godina": 2,
        "email": "emir@gmail.com",
        "prosjek": 7.5,
        "aktivan": True
    },
    {
        "ime": "Lejla",
        "godina": 1,
        "email": "lejla@gmail.com",
        "prosjek": 9.2,
        "aktivan": True
    }
]
"----------------------------------------------------------------"
#zadatak 2
# Definicija funkcije koja prima ime, godinu i  vraća rječnik
def get_student_info(name: str, year: int , email: str ):
    return {
         # ključ "name" dobija vrijednost parametra name
        "name": name,
         # ključ "year" dobija vrijednost parametra year
        "year": year,
         
        "email": email, #dodaato bez copilota
         # kreira poruku koristeći f-string sa imenom i godinom
        "greeting": f"Zdravo {name}, vi ste {year} godina studija"
    }

# Example usage
student_info = get_student_info("Amina", 3,  "amina@gmail.com" ) #poziv funkcije
print(student_info) #printanje rezultata funkcije

#pokrenula,radi

"---------------------------------------------------------------------------------------------------"
#zadatak 3

def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper


@ispisi_poziv
def get_student_info(name: str, year: int):
    return {
        "name": name,
        "year": year,
        "greeting": f"Zdravo {name}, vi ste {year} godina studija"
    }

print(get_student_info("Amina", 3))

"---------------------------------------------------------------------------------------------------"
#zadatak 4

# Definicija klase Course koja predstavlja jedan predmet
class Course:
    # Konstruktor koji se poziva pri kreiranju objekta
    def __init__(self, name: str, code: str, credits: int,professor: str):
        # Čuva naziv kursa kao atribut objekta
        self.name = name
        # Čuva šifru kursa kao atribut objekta
        self.code = code
        # Čuva broj kredita kao atribut objekta
        self.credits = credits
        self.professor = professor
    # Metoda koja vraća opis kursa kao string
    def description(self):
        # Vraća formatiran string sa šifrom, nazivom i brojem kredita
        return f"{self.code} - {self.name} ({self.credits} kredita),profesor: {self.professor}"



# Example usage
# Kreiranje objekta klase Course sa konkretnim vrijednostima
course = Course("Razvoj telekomunikacijske programske podrške", "TK207", 6,"Dr. Ahmed")
course2 = Course("Baze podataka", "BD101", 5, "Prof. Ivana")
# Poziv metode description i ispis rezultata
print(course.description())
print(course2.description())
#pokrenula, radi ono sto je generisano 

"---------------------------------------------------------------------------------------------------"
#zadatak 5

students = [
    {"name": "Amina", "year": 3, "email": "amina@untz.ba"},
    {"name": "Emir", "year": 2, "email": "emir@untz.ba"},
    {"name": "Lejla", "year": 1, "email": "lejla@untz.ba"},
    {"name": "Marko", "year": 3, "email": "marko@untz.ba"}
]

def filter_by_year(students: list, year: int) -> list:
    filtered = []
    
    for student in students:
        if student["year"] == year:
            filtered.append(student)
    
    return filtered


def print_registry(students: list) -> None:
    for student in students:
    
        print(f"Ime: {student['name']}, Email: {student['email']}")

third_year_students = filter_by_year(students, 3)

print("Studenti 3. godine:")
print_registry(third_year_students)
print("\nSvi studenti:")
print_registry(students)

"---------------------------------------------------------------------------------------------------"
#Bonus zadatak
def sort_by_year(students: list) -> list:
    return sorted(students, key=lambda student: student["year"])

def filter_by_year(students: list, year: int) -> list:
    result = []
    for student in students:
        if student["year"] == year:
            result.append(student)
    return result

def filter_by_name_letter(students: list, letter: str) -> list:
    result = []
    for student in students:
        if student["name"][0] == letter:
            result.append(student)
    return result


sorted_students = sort_by_year(students)
print("Sortirani studenti:")
print_registry(sorted_students)
print("\nStudenti 3. godine:")
print_registry(filter_by_year(students, 3))
print("\nStudenti čije ime počinje sa 'A':")
print_registry(filter_by_name_letter(students, "A"))
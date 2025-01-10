""""""""""""
#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Jakub Gajdzica
#email: j.gajdzica@gmail.com
""""""""""""

#přihlašování uživatelů
uzivatel={"bob":"123",
          "ann":"pass123",
          "mike":"password123",
          "liz":"pass123"
        }
username=input("username:")
heslo=input("password:")
print("-"*40)
if username in uzivatel and uzivatel[username] == heslo:
    print (f"Welcome to the app,{username}")
    print("We have 3 text to analyze for you")
else:
    print("unregistrated user, terminating the program..")
    exit()
print("-"*40)
# Texty k analýze
TEXTS = [
    """Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive topographic feature that rises 
    sharply some 1000 feet above Twin Creek Valley to an elevation of 
    more than 7500 feet above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, which traverse the valley.""",

    """At the base of Fossil Butte are the bright red, purple, yellow, 
    and gray beds of the Wasatch Formation. Eroded portions of these 
    horizontal beds slope gradually upward from the valley floor 
    and steepen abruptly.""",

    """The monument contains 8198 acres and protects a portion of the largest 
    deposit of freshwater fish fossils in the world. The richest fossil 
    fish deposits are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils represent several 
    varieties of perch, as well as other freshwater genera and herring 
    similar to those in modern oceans."""
]
try:
    choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if choice < 1 or choice > len(TEXTS):
        print("Invalid choice, terminating the program...")
        exit()
    text = TEXTS[choice - 1]
except ValueError:
    print("Invalid input, terminating the program...")
    exit()

# Analýza textu
words = text.split()
word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper())
lowercase_count = sum(1 for word in words if word.islower())
numeric_strings = [int(word) for word in words if word.isdigit()]
numeric_count = len(numeric_strings)
numeric_sum = sum(numeric_strings)

# Výstup analýzy
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)

# Frekvenční analýza délek slov
lengths = [len(word.strip(".,!?")) for word in words]
length_freq = {length: lengths.count(length) for length in set(lengths)}

# Výstup frekvenční analýzy
print(f"{'LEN':<4}|{'OCCURENCES':<12}|NR.")
print("-" * 40)
for length in sorted(length_freq):
    stars = "*" * length_freq[length]
    print(f"{length:<4}|{stars:<12}|{length_freq[length]}")
print("díky")
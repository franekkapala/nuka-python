from ast import If


name = input("Podaj swoje imię: ")
nameLenght = len(name)
print("Twoje imię składa się tyu znaków: ", nameLenght);
plec = input("podaj swojom płeć [K,M]: ") 

year = input("podaj ile masz lat: ")
yearOfBirdthday = 2022 - int(year)
print("urodzijeś się ", yearOfBirdthday );
print("Nazwasz się ", name,"urodziłeś się: ", yearOfBirdthday,"masz ", year, "lat.")


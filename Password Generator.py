import random
import string

def get_initials(name):
    return ''.join([word[0].upper() for word in name.split()])

def get_special_date_parts(date):
    day, month, year = date.split('-')
    return day, month, year

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def create_password(name, special_date, day, month, age, city, country):
    initials = get_initials(name)
    special_day, special_month, special_year = get_special_date_parts(special_date)
    city_code = ''.join([word[0].upper() for word in city.split()])
    country_code = ''.join([word[0].upper() for word in country.split()])
    
    random_string = generate_random_string(6)
    
    password = f"{initials}{special_day}{special_month}{special_year}{day}{month}{age}{city_code}{country_code}{random_string}"
    return password

def main():
    name = input("Enter your or someone specials name: ")
    special_date = input("Enter a special date (DD-MM-YYYY): ")
    day = input("Enter a memorable day: ")
    month = input("Enter a fav month: ")
    age = input("Enter your or random age: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    
    password = create_password(name, special_date, day, month, age, city, country)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

import csv
import os

WORKOUT_FILE = 'workouts.csv'
NUTRITION_FILE = 'nutrition.csv'
PROGRESS_FILE = 'progress.csv'
USER_FILE = 'users.csv'

def authenticate():
    print("Welcome to the Fitness Tracking System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if user exists in the user file
    try:
        with open(USER_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Authentication successful!")
                    return True
            print("Authentication failed! Please register or check your credentials.")
            return False
    except FileNotFoundError:
        print("No users found. Please register a new user.")
        return False

def register_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(USER_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print(f"User '{username}' registered successfully!")

def add_workout():
    workout_id = input("Enter Workout ID: ")
    workout_type = input("Enter Workout Type: ")
    duration = input("Enter Duration (minutes): ")
    calories_burned = input("Enter Calories Burned: ")

    with open(WORKOUT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([workout_id, workout_type, duration, calories_burned])
    print(f"Workout '{workout_type}' added successfully.")

def view_workouts():
    try:
        with open(WORKOUT_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<20} {:<10} {:<10}".format('ID', 'Type', 'Duration', 'Calories'))
            print("=" * 50)
            for row in reader:
                print("{:<10} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("=" * 50)
    except FileNotFoundError:
        print("Workouts file not found.")

def search_workout():
    search_term = input("Enter Workout ID or Type to search: ")
    found = False

    try:
        with open(WORKOUT_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<20} {:<10} {:<10}".format('ID', 'Type', 'Duration', 'Calories'))
            print("=" * 50)
            for row in reader:
                if search_term.lower() in row[0].lower() or search_term.lower() in row[1].lower():
                    print("{:<10} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
                    found = True
            if not found:
                print("No matching workouts found.")
            print("=" * 50)
    except FileNotFoundError:
        print("Workouts file not found.")

def add_nutrition():
    nutrition_id = input("Enter Nutrition ID: ")
    food_item = input("Enter Food Item: ")
    calories = input("Enter Calories: ")
    protein = input("Enter Protein (g): ")

    with open(NUTRITION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nutrition_id, food_item, calories, protein])
    print(f"Nutrition '{food_item}' added successfully.")

def view_nutrition():
    try:
        with open(NUTRITION_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<30} {:<10} {:<10}".format('ID', 'Food Item', 'Calories', 'Protein'))
            print("=" * 70)
            for row in reader:
                print("{:<10} {:<30} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("=" * 70)
    except FileNotFoundError:
        print("Nutrition file not found.")

def search_nutrition():
    search_term = input("Enter Food Item or ID to search: ")
    found = False

    try:
        with open(NUTRITION_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<30} {:<10} {:<10}".format('ID', 'Food Item', 'Calories', 'Protein'))
            print("=" * 70)
            for row in reader:
                if search_term.lower() in row[1].lower() or search_term.lower() in row[0]:
                    print("{:<10} {:<30} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
                    found = True
            if not found:
                print("No matching nutrition items found.")
            print("=" * 70)
    except FileNotFoundError:
        print("Nutrition file not found.")

def add_progress():
    progress_id = input("Enter Progress ID: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    weight = input("Enter Weight (kg): ")
    body_fat = input("Enter Body Fat (%): ")

    with open(PROGRESS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([progress_id, date, weight, body_fat])
    print(f"Progress entry for '{date}' added successfully.")

def view_progress():
    try:
        with open(PROGRESS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<15} {:<10} {:<10}".format('ID', 'Date', 'Weight', 'Body Fat'))
            print("=" * 50)
            for row in reader:
                print("{:<10} {:<15} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("=" * 50)
    except FileNotFoundError:
        print("Progress file not found.")

def analyze_progress():
    try:
        with open(PROGRESS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\nWeight and Body Fat Progress:")
            print("=" * 50)
            for row in reader:
                print(f"Date: {row[1]}, Weight: {row[2]} kg, Body Fat: {row[3]}%")
            print("=" * 50)
    except FileNotFoundError:
        print("Progress file not found.")

def edit_workout():
    workout_id = input("Enter Workout ID to edit: ")
    found = False
    workouts = []

    try:
        with open(WORKOUT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == workout_id:
                    found = True
                    workout_type = input("Enter new Workout Type: ")
                    duration = input("Enter new Duration (minutes): ")
                    calories_burned = input("Enter new Calories Burned: ")
                    workouts.append([workout_id, workout_type, duration, calories_burned])
                else:
                    workouts.append(row)

        if found:
            with open(WORKOUT_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(workouts)
            print(f"Workout ID '{workout_id}' updated successfully.")
        else:
            print(f"Workout ID '{workout_id}' not found.")

    except FileNotFoundError:
        print("Workouts file not found.")

def delete_workout():
    workout_id = input("Enter Workout ID to delete: ")
    found = False
    workouts = []

    try:
        with open(WORKOUT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != workout_id:
                    workouts.append(row)
                else:
                    found = True

        if found:
            with open(WORKOUT_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(workouts)
            print(f"Workout ID '{workout_id}' deleted successfully.")
        else:
            print(f"Workout ID '{workout_id}' not found.")

    except FileNotFoundError:
        print("Workouts file not found.")

def delete_nutrition():
    nutrition_id = input("Enter Nutrition ID to delete: ")
    found = False
    nutrition_items = []

    try:
        with open(NUTRITION_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != nutrition_id:
                    nutrition_items.append(row)
                else:
                    found = True

        if found:
            with open(NUTRITION_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(nutrition_items)
            print(f"Nutrition ID '{nutrition_id}' deleted successfully.")
        else:
            print(f"Nutrition ID '{nutrition_id}' not found.")

    except FileNotFoundError:
        print("Nutrition file not found.")

def delete_progress():
    progress_id = input("Enter Progress ID to delete: ")
    found = False
    progress_entries = []

    try:
        with open(PROGRESS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != progress_id:
                    progress_entries.append(row)
                else:
                    found = True

        if found:
            with open(PROGRESS_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(progress_entries)
            print(f"Progress ID '{progress_id}' deleted successfully.")
        else:
            print(f"Progress ID '{progress_id}' not found.")

    except FileNotFoundError:
        print("Progress file not found.")

def export_workouts():
    output_file = input("Enter the filename to save workouts (e.g., workouts.txt): ")
    try:
        with open(WORKOUT_FILE, mode='r') as file:
            reader = csv.reader(file)
            with open(output_file, mode='w') as outfile:
                for row in reader:
                    outfile.write(f"ID: {row[0]}, Type: {row[1]}, Duration: {row[2]} mins, Calories: {row[3]}\n")
        print(f"Workouts exported successfully to '{output_file}'.")
    except FileNotFoundError:
        print("Workouts file not found.")

def export_nutrition():
    output_file = input("Enter the filename to save nutrition (e.g., nutrition.txt): ")
    try:
        with open(NUTRITION_FILE, mode='r') as file:
            reader = csv.reader(file)
            with open(output_file, mode='w') as outfile:
                for row in reader:
                    outfile.write(f"ID: {row[0]}, Food Item: {row[1]}, Calories: {row[2]}, Protein: {row[3]} g\n")
        print(f"Nutrition items exported successfully to '{output_file}'.")
    except FileNotFoundError:
        print("Nutrition file not found.")

def main():
    while True:
        print("\n===========Fitness Tracking System==========")
        print("===Presented in Kanha Makhan Public School=====")
        print("========Created By-Utkarsh Sharma & sumit Kumar ===")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Add Workout")
        print("4. View Workouts")
        print("5. Search Workout")
        print("6. Add Nutrition")
        print("7. View Nutrition")
        print("8. Search Nutrition")
        print("9. Add Progress")
        print("10. View Progress")
        print("11. Analyze Progress")
        print("12. Edit Workout")
        print("13. Delete Workout")
        print("14. Delete Nutrition")
        print("15. Delete Progress")
        print("16. Export Workouts")
        print("17. Export Nutrition")
        print("18. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if not authenticate():
                continue
        elif choice == '3':
            add_workout()
        elif choice == '4':
            view_workouts()
        elif choice == '5':
            search_workout()
        elif choice == '6':
            add_nutrition()
        elif choice == '7':
            view_nutrition()
        elif choice == '8':
            search_nutrition()
        elif choice == '9':
            add_progress()
        elif choice == '10':
            view_progress()
        elif choice == '11':
            analyze_progress()
        elif choice == '12':
            edit_workout()
        elif choice == '13':
            delete_workout()
        elif choice == '14':
            delete_nutrition()
        elif choice == '15':
            delete_progress()
        elif choice == '16':
            export_workouts()
        elif choice == '17':
            export_nutrition()
        elif choice == '18':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

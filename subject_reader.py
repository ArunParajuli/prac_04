FILENAME = "subject_data.txt"


def main():
    data = get_data()
    if data:
        print(data)
        display_subject_details(data)
    else:
        print("No data found.")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    try:
        with open(FILENAME) as input_file:
            data_list = []  # Initialize an empty list to store the data
            for line in input_file:
                line = line.strip()  # Remove the \n
                parts = line.split(',')  # Separate the data into its parts
                parts[2] = int(parts[2])  # Make the number an integer
                data_list.append(parts)  # Append the parts to the data list
            return data_list  # Return the list of lists
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found.")
        return None


def display_subject_details(data):
    """Display subject details."""
    for subject_data in data:
        subject_code = subject_data[0]
        lecturer = subject_data[1]
        num_students = subject_data[2]


def read_text_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_text_file("file_07-06-2024_12-49-04.txt")
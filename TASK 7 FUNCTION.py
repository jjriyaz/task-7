
from datetime import datetime

def create_text_file_with_timestamp():
    
    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    
    file_name = f"file_{current_time}.txt"
    
    
    with open(file_name, "w") as file:
        file.write("This is a text file created at " + current_time)

    print(f"Text file '{file_name}' created successfully.")


create_text_file_with_timestamp()

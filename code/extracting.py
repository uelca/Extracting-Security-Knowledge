import os
import time

from ChatGPT import ChatGPT


def extract_control_types(root_folder, query):
    """
    In this function we will iterate through each subfolder of the root_folder and create a new .txt File. We will
    then take the content of the "-Controls.txt" file and give it to ChatGPT along with the query. The response of
    ChatGPT will be then stored in the created .txt File.
    :param root_folder: The root-folder where all sub-folders are stored
    :param query: The pre-defined query for ChatGPT, which does only contain the question header and no content
    :return:
    """
    with open('/Users/M.Fatih/PycharmProjects/Ontologie/data/api.txt', 'r') as api_key:
        API_KEY = api_key.read()
        chat_GPT = ChatGPT(API_KEY, "Sei ein Sicherheitsexperte")

    import os

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith("-Controls.txt"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        control_text = file.read()

                    folder_name = os.path.basename(dirpath)
                    new_filename = folder_name + "-Control-Types.txt"
                    new_file_path = os.path.join(dirpath, new_filename)

                    if not os.path.exists(new_file_path):
                        # Create new combined String (query + section of control_text) to give it to ChatGPT
                        combined_query = query + "\n\n" + control_text
                        response = chat_GPT.question(combined_query)

                        # Save the response
                        with open(new_file_path, 'a', encoding='utf-8') as new_file:
                            new_file.write(response + '\n')
                        time.sleep(15)
                        print(control_text.split(" ")[0] + " was added to " + new_filename)
                    else:
                        print(f"The File {new_file_path} exist already.")

                except Exception as e:
                    print(f"Context is too large for {file_path}: {str(e)}")



def split_text_into_sections(text, section_header):
    sections = []
    current_section = []

    lines = text.split('\n')

    for line in lines:
        # If the line starts with a paragraph, begin a new paragraph.
        if line.strip() == "":
            if current_section:
                sections.append('\n'.join(current_section))
            current_section = []
        elif line.strip().startswith(section_header):
            # Append the header and the row to the current paragraph
            current_section.append(line)
        else:
            current_section.append(line)

    if current_section:
        sections.append('\n'.join(current_section))

    return sections

def copy_controls_files(root_path, target_file_path):
    # Check if the target file is not empty
    if os.path.exists(target_file_path) and os.path.getsize(target_file_path) > 0:
        print("The target file is not empty. Content will not be overwritten.")
        return

    with open(target_file_path, 'a', encoding='utf-8') as target_file:
        for directory_path, _, files in os.walk(root_path):
            for file_name in files:
                if file_name.endswith("-Controls.txt"):
                    file_path = os.path.join(directory_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as controls_file:
                        controls_content = controls_file.read()
                        target_file.write(controls_content)


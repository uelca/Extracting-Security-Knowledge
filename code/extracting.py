import os
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
                        # Create new combined String (query + control_text) to give it to ChatGPT
                        combined_query = query + "\n\n" + control_text

                        response = chat_GPT.question(combined_query)

                        with open(new_file_path, 'w', encoding='utf-8') as new_file:
                            new_file.write(response)
                    else:
                        print(f"The File {new_file_path} exist already.")

                except Exception as e:
                    print(f"Fehler beim Verarbeiten von {file_path}: {str(e)}")


def split_text_into_sections(text, section_header):
    sections = []
    current_section = []

    lines = text.split('\n')

    for line in lines:
        # Wenn die Zeile mit einem Absatz beginnt, starten Sie einen neuen Abschnitt
        if line.strip() == "":
            if current_section:
                sections.append('\n'.join(current_section))
            current_section = []
        elif line.strip().startswith(section_header):
            # Fügen Sie den Header und die Zeile zum aktuellen Abschnitt hinzu
            current_section.append(line)
        else:
            current_section.append(line)

    if current_section:
        sections.append('\n'.join(current_section))

    return sections
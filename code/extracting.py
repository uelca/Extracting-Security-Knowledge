import os
import time
from ChatGPT import ChatGPT


def extract_control_types(root_folder, query):
    """
    In this function we will iterate through each subfolder of the root_folder and create a new .txt File. We will
    then take all the indidvidual controls from the "-Controls.txt" file and give it to ChatGPT along with the query.
    The response of ChatGPT (The Control Type of the according Control) will be then stored in the created .txt File.
    :param root_folder: The root-folder where all sub-folders are stored
    :param query: The pre-defined query for ChatGPT, which does only contain the question header and no content
    :return:
    """
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Iterate over the subfolders
        for filename in filenames:
            if filename.endswith("-Controls.txt"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        control_text = file.read()
                    # Create new File in which the response from ChatGPT is stored
                    folder_name = os.path.basename(dirpath)
                    new_filename = folder_name + "-Control-Types.txt"
                    new_file_path = os.path.join(dirpath, new_filename)

                    if not os.path.exists(new_file_path):
                        # Create new combined String (query + control_text) to give it to ChatGPT
                        combined_query = query + "\n\n" + control_text
                        with open('/Users/M.Fatih/PycharmProjects/Ontologie/data/api.txt', 'r') as api_key:
                            API_KEY = api_key.read()
                            chatGPT = ChatGPT(API_KEY, "Sei ein Sicherheitsexperte")
                        response = chatGPT.question(combined_query)

                        # Save the response into the newly created File
                        with open(new_file_path, 'a', encoding='utf-8') as new_file:
                            new_file.write(response + '\n')
                        print("The control types for " + new_filename.split(" ")[0] + " was added to " + new_filename)
                    else:
                        print(f"The File {new_file_path} exist already.")

                except Exception as e:
                    print(f"Context is too large for {file_path}: {str(e)}")
    print("Control Types for each '-Controls.txt' was created")

def extract_Threat_Origin_And_Securityattribute(root_folder, query):
    """
    In this function we will iterate through each subfolder of the root_folder and create a new .txt File. We will
    then take all the indidvidual threats from the "-Threats.txt" file and give it to ChatGPT along with the query.
    The response of ChatGPT (The Threat Origin and the affected SecurityAttribute of the according Threat) will be
    then stored in the created .txt File.
    :param root_folder: The root-folder where all sub-folders are stored
    :param query: The pre-defined query for ChatGPT, which does only contain the question header and no content
    :return:
    """
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Iterate over the subfolders
        for filename in filenames:
            if filename.endswith("-Threats.txt"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        threats = file.read()
                    # Create new File in which the response from ChatGPT is stored
                    folder_name = os.path.basename(dirpath)
                    new_filename = folder_name + "-Threat-Origin-SecAttribute.txt"
                    new_file_path = os.path.join(dirpath, new_filename)

                    if not os.path.exists(new_file_path):
                        # Create new combined String (query + Threats) to give it to ChatGPT
                        combined_query = query + "\n\n" + threats
                        with open('/Users/M.Fatih/PycharmProjects/Ontologie/data/api.txt', 'r') as api_key:
                            API_KEY = api_key.read()
                            chatGPT = ChatGPT(API_KEY, "Sei ein Sicherheitsexperte")
                        response = chatGPT.question(combined_query)

                        # Save the response into the newly created File
                        with open(new_file_path, 'a', encoding='utf-8') as new_file:
                            new_file.write(response)
                        print("Threat Origin and affected Security Attribute for " + folder_name + " where added to " + new_filename)
                    else:
                        print(f"The File {new_file_path} exist already.")

                except Exception as e:
                    print(f"Context is too large for {file_path}: {str(e)}")
    print("Threat Origin and affected Security Attribute for each '-Threats.txt' was created")

def extract_vulnerabilities(root_folder):
    """
    In this function we are extracting the vulnerabilities for a given control and threat. This is done for each subfolder of
    the root folder. The answers are stored in the -Vulnerabilities.txt files
    :param root_folder: Path to the root folder
    :return:
    """
    print("Vulnerabilities are extracted now, this might take couple of hours...")
    query_1 = "Ich werde dir nun im folgenden eine Maßnahme mit ihrer Beschreibung und eine Gefährdung mit ihrer Beschreibung nennen. Ich möchte, dass du mir dazu eine Schwachstelle erzeugst. Als erste die Gefährdung:"
    query_2 = "Und nun die Maßnahme zu dieser Gefährdung:"
    query_3 = "Kannst du mir nun Schwachstellen formulieren, die von der Gefährdung ausgenutzt werden könnten und von der Maßnahme gemindert werden. Deine Antwort soll lediglich die Schwachstellen und eine Erläuterung der Schwachstelle  in durchnummerierter Form enthalten und nichts weiteres."
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith("Allocation.txt"):
                file_path = os.path.join(dirpath, file)
                try:
                    with open(file_path, 'r') as allocation_file:

                        folder_name = os.path.basename(dirpath)
                        filename = folder_name + "-Vulnerabilities.txt"
                        vulnerabilities_file_path = os.path.join(dirpath, filename)

                        path_to_All_Controls = '/Users/M.Fatih/PycharmProjects/Ontologie/data/All-Controls.txt'
                        path_to_All_Threats = '/Users/M.Fatih/PycharmProjects/Ontologie/data/All-Threats.txt'

                        if not os.path.exists(vulnerabilities_file_path) or os.path.getsize(
                                vulnerabilities_file_path) == 0:
                            for line in allocation_file:
                                # The Allocation file is built as following:
                                # Control Identifier + Control Description + "mitigates" + Threat Identifier
                                # We split it before "mitigates" and after
                                parts = line.strip().split("mitigates")
                                before_mitigate, after_mitigate = map(str.strip, parts)
                                # We use the splittet strings to search for the Description in the All_Threats and All_Controls Files
                                control = find_term_in_file(before_mitigate, path_to_All_Controls)
                                threat = find_term_in_file(after_mitigate, path_to_All_Threats)
                                # We create a new query consisting of the Descriptions
                                combined_query = query_1 + '\n' + threat + query_2 + '\n' + control + query_3
                                with open('/Users/M.Fatih/PycharmProjects/Ontologie/data/api.txt', 'r') as api_key:
                                    API_KEY = api_key.read()
                                    chatGPT = ChatGPT(API_KEY, "Sei ein Sicherheitsexperte")
                                response = chatGPT.question(combined_query)

                                # Save the response into the Vulnerabilities.txt File
                                with open(vulnerabilities_file_path, 'a', encoding='utf-8') as new_file:
                                    threat_first_part = threat.split(" ")[0]
                                    threat_second_part = threat.split(" ")[1]
                                    new_file.write(
                                        "Schwachstelle für Maßnahme: " + control.split(" ")[0] + " und Bedrohung: " +
                                        threat_first_part + " " + threat_second_part + '\n' + response + '\n\n\n')
                                print("Vulnerability for Allocation: " + control.split(" ")[0] + " mitigates " +
                                      threat_first_part + " " + threat_second_part + " was created successfully")
                        else:
                            print(f"The File {vulnerabilities_file_path} exist already.")
                except Exception as e:
                    print(f"Context is too large for {file_path}: {str(e)}")
    print("Vulnerabilities was extracted. The Script is finished. All File are placed in sub-folders of the root folder")

def find_term_in_file(term, file_path):
    result_string = ""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if term in line:
                    result_string += line.strip() + '\n'
                    if i + 1 < len(lines):
                        result_string += lines[i + 1].strip() + '\n'
    except Exception as e:
        print(f"Context is too large for {file_path}: {str(e)}")
    return result_string
from extracting import split_text_into_sections
from preprocessing import preprocess_data
from extracting import extract_control_types

def main() -> object:
    # Path to the files
    txt_path = '/data/Notwendige Bausteine.txt'
    excel_path = '/data/krt2023_Excel.xlsx'
    root_folder = '/Users/M.Fatih/PycharmProjects/Ontologie/Single Excel Tables'
    # preprocess_data(txt_path, excel_path, root_folder)
    query_Control_Type = "Du sollst im folgenden als Sicherheitsexperte agieren. Ich werde dir nun eine Reihe von Maßnahmen geben und möchte von dir, dass du mir mitteilst, um was für eine Maßnahme es sich handelt. Es gibt vier mögliche Arten von Maßnahmen: abschreckende, korrigierende, vorbeugende,   Wiederherstellungs- oder Aufdeckungsmaßnahmen. Deine Antwort soll wie folgt aufgebaut sein: Bezeichner der Maßnahme - Art der Maßnahme. Es soll keine weitere Erklärung oder Erläuterung in deiner Antwort vorkommen. Ein Beispiel: APP.1.1.A2 Einschränken von Aktiven Inhalten ist Vorbeugend. Hier sind die Maßnahmen: "
    query_Threat_Origin_SecAttr = "Du sollst im folgenden als Sicherheitsexperte agieren. Ich werde dir nun eine Reihe von Gefährdungen mit ihren Beschreibungen geben. Jedee Gefährdung hat auch einen Ursprung. Dieser kann versehentlich oder vorsätzlich sein. Weiterhin beeinflusst eine Gefährdung ein Sicherheitsattribut. Diese sind können sein: Vertraulichkeit, Integrität, Verfügbarkeit. Ich möchte, dass du mir zu folgenden Gefährdungen, den Ursrpung und das beeinflusste Sicherheitsattribut mitteilst: "
    # extract_control_types(root_folder, query_Control_Type)



if __name__ == '__main__':
    # main()
    file_path = '/Users/M.Fatih/PycharmProjects/Ontologie/Single Excel Tables/APP.1.1 Office-Produkte/APP.1.1 Office-Produkte-Controls.txt'

    # Header für die Abschnitte
    section_header = "APP.1.1"  # Ersetzen Sie "Header" durch den tatsächlichen Header

    # Text aus der Datei lesen
    with open(file_path, 'r', encoding='utf-8') as file:
        file_text = file.read()

    # Funktion aufrufen, um den Text in Abschnitte aufzuteilen
    sections = split_text_into_sections(file_text, section_header)

    # Die aufgeteilten Abschnitte anzeigen
    for i, section in enumerate(sections):
        print(f"Abschnitt {i + 1}:\n{section}\n")
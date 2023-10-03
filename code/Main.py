from preprocessing import preprocess_data
from extracting import extract_control_types
from extracting import extract_vulnerabilities
from extracting import extract_Threat_Origin_And_Securityattribute
from ChatGPT import ChatGPT

def main():
    # Path to the files
    txt_path = '/data/Notwendige Bausteine.txt'
    excel_path = '/data/krt2023_Excel.xlsx'
    root_folder = '/Users/M.Fatih/PycharmProjects/Ontologie/Single Excel Tables'
    # preprocess_data(txt_path, excel_path, root_folder)
    query_Control_Type = "Du sollst im folgenden als Sicherheitsexperte agieren. Ich werde dir nun Riehe von Maßnahmen geben und möchte von dir, dass du mir mitteilst, um was für eine Maßnahme es sich handelt. Es gibt vier mögliche Arten von Maßnahmen: abschreckende, korrigierende, vorbeugende, Wiederherstellungs- oder Aufdeckungsmaßnahmen. Deine Antwort soll wie folgt aufgebaut sein: Bezeichner der Maßnahme - Art der Maßnahme. Es soll keine weitere Erklärung oder Erläuterung in deiner Antwort vorkommen. Eine Beispielantwort: APP.1.1.A2 Einschränken von Aktiven Inhalten ist Vorbeugend. Hier sind die Maßnahmen: "
    query_Threat_Origin_SecAttr = "Du sollst im folgenden als Sicherheitsexperte agieren. Ich werde dir nun eine Reihe von Gefährdungen mit ihren Beschreibungen geben. Jede Gefährdung hat auch einen Ursprung. Dieser kann versehentlich oder vorsätzlich sein. Weiterhin beeinflusst eine Gefährdung ein Sicherheitsattribut. Diese sind können sein: Vertraulichkeit, Integrität, Verfügbarkeit. Ich möchte, dass du mir zu folgenden Gefährdungen, den Ursrpung und das beeinflusste Sicherheitsattribut mitteilst. Deine Antwort soll wie folgt aufgebaut sein: Bezeichner der Gefährdung - Ursprung und beeinflusste Sicherheitsattribut. Es soll keine weitere Erklärung oder Erläuterung in deiner Antwort vorkommen: "
    # extract_control_types(root_folder, query_Control_Type)
    # extract_vulnerabilities(root_folder)
    extract_Threat_Origin_And_Securityattribute(root_folder, query_Threat_Origin_SecAttr)

if __name__ == '__main__':
    main()

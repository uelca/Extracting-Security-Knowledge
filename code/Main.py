from preprocessing import preprocess_data
def main():
    # Path to the files
    txt_path = '/data/Notwendige Bausteine.txt'
    excel_path = '/data/krt2023_Excel.xlsx'
    root_folder = '/Users/M.Fatih/PycharmProjects/Ontologie/Single Excel Tables'
    preprocess_data(txt_path, excel_path, root_folder)


if __name__ == '__main__':
    main()

# Otwieranie plików wejściowych i odczytywanie danych
with open("dane.txt", "r") as dane_file:
    input_data = dane_file.read().strip().split()

with open("output.txt", "r") as output_file:
    output_data = output_file.read().strip().split("\n")

# Tworzenie tabeli HTML z danymi wejściowymi i wyjściowymi
table = "<table>"

# Wiersz z danymi wejściowymi
table += "<tr><td style='border: 1px solid black;'>Input</td><td style='border: 1px solid black;'>" + " ".join(input_data) + "</td></tr>"

# Wiersz z danymi wyjściowymi
table += "<tr><td style='border: 1px solid black;'>Output</td><td style='border: 1px solid black;'>"
table += "<table style='border-collapse: collapse;'>"
for i, row in enumerate(output_data):
    row_data = row.strip().split()
    if i == 0:
        table += "<tr style='border-bottom: 1px solid black;'>"
    elif i == 6:
        table += "<tr style='border-top: 1px solid black;'>"
    else:
        table += "<tr>"
    for j, value in enumerate(row_data):
        if j == 0:
            table += "<td style='border-right: 1px solid black;'>" + value + "</td>"
        elif j == 6:
            table += "<td style='border-left: 1px solid black;'>" + value + "</td>"
        else:
            table += "<td>" + value + "</td>"
    table += "</tr>"
table += "</table>"
table += "</td></tr>"

table += "</table>"

# Zapisywanie tabeli do pliku HTML
with open("raport.html", "w") as report_file:
    report_file.write(table)

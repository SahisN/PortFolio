import csv


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as csv_database:
        email, message, subject = data["name"], data["email"], data["message"]
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])

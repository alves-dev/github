class ReportFileWriter:

    @staticmethod
    def write(report):
        with open('report.txt', 'w') as file:
            file.write(report)


class ReportFileWriter2:

    @staticmethod
    def write(report):
        with open('report2.txt', 'w') as file:
            file.write(report)

# Dica: talvez usar uma interface para garantir a def write

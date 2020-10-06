from .reports.file_writer import ReportFileWriter


class ReportWrite:
    @staticmethod
    def write(report, writer=ReportFileWriter):
        writer.write(report)

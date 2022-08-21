import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    def read_csv(path):
        with open(path) as file:
            csv_data = csv.DictReader(file)

        return csv_data

    def read_json(path):
        with open(path) as file:
            dict_list = json.loads(file.read())

        return dict_list

    def type_file(path):
        if "csv" in path:
            return Inventory.read_csv(path)
        if "json" in path:
            return Inventory.read_json(path)

    @classmethod
    def import_data(path, type):
        if type == "simples":
            return SimpleReport.generate(Inventory.type_file(path))
        return CompleteReport.generate(Inventory.type_file(path))

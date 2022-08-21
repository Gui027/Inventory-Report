from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def counter_empresa(cls, products):
        list_business_name = list()

        for product in products:
            list_business_name.append(product["nome_da_empresa"])

        return Counter(list_business_name)

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"Physicians Total Care, Inc.:\n"
            f"Newton Laboratories, Inc.:\n"
            f"Forces of Nature:"
        )

from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def counter_empresa(cls, products):
        list_business_name = list()

        for product in products:
            list_business_name.append(product["nome_da_empresa"])

        counter = Counter(list_business_name).most_common()
        i = ''

        for business_name, quant in counter:
            i += f"- {business_name}: {quant}\n"

        return i

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        qtd = cls.counter_empresa(products)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{qtd}"
        )

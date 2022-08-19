from collections import Counter


class SimpleReport:
    @classmethod
    def get_fab_date(cls, products):
        list_fab_date = list()

        for date in products:
            list_fab_date.append(date["data_de_fabricacao"])

        return min(list_fab_date)

    @classmethod
    def get_val_date(cls, products):
        list_val_date = list()

        for date in products:
            list_val_date.append(date["data_de_validade"])

        return min(list_val_date)

    @classmethod
    def get_more_products(cls, products):
        list_more_product = list()

        for product in products:
            list_more_product.append(product["nome_da_empresa"])

        return Counter(list_more_product).most_common(1)[0][0]

    @classmethod
    def generate(cls, products):
        fab_date = cls.get_fab_date(products)
        val_date = cls.get_val_date(products)
        more_products = cls.get_more_products(products)

        return (

            f"Data de fabricação mais antiga: {fab_date}\n"
            f"Data de validade mais próxima: {val_date}\n"
            f"Empresa com mais produtos: {more_products}"
        )

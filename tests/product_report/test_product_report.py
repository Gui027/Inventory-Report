from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_rep = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "21/02/2022",
        "21/02/2025",
        "numero_de_serie",
        "armazenamento"
    )
    assert product_rep.__repr__() == (
        f"O produto {product_rep.nome_do_produto}"
        f" fabricado em {product_rep.data_de_fabricacao}"
        f" por {product_rep.nome_da_empresa} com validade"
        f" até {product_rep.data_de_validade}"
        f" precisa ser armazenado {product_rep.instrucoes_de_armazenamento}."
    )

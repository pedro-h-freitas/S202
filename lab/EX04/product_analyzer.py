from database import Database
from helper.write_a_json import write_a_json


class ProductAnalyzer:
    def __init__(self, database: Database):
        self._database = database

    def get_total_vendas_por_dia(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {
                "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": None, "total": {"$sum": "$total"}}}
        ])

        write_a_json(result, "total_vendas_por_dia")

    def get_produto_mais_vendido(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao",
                        "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        write_a_json(result, "produto_mais_vendido")

    def get_cliente_maior_compra(self):
        result = self._database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {
                "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        write_a_json(result, "cliente_maior_compra")

    def get_produtos_vendidos_mais_que_1(self):
        pass

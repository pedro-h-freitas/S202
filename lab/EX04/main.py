from database import Database
from helper.write_a_json import write_a_json
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
pa = ProductAnalyzer(db)

pa.get_total_vendas_por_dia()
pa.get_produto_mais_vendido()
pa.get_cliente_maior_compra()
pa.get_produtos_vendidos_mais_que_1()

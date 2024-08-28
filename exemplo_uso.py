import schema_compare_postgres as scp


def busca_parametro_conexao(banco):
    return {
        "banco": banco,
        "user": "",
        "password": "",
        "host": ""
    }


def conectar_banco_origem_destino(banco_origem, banco_destino):
    return {
        "conexao_banco_origem": scp.conectar(**busca_parametro_conexao(banco_origem)),
        "conexao_banco_destino": scp.conectar(**busca_parametro_conexao(banco_destino))
    }


bancos_verificar = conectar_banco_origem_destino("bd_planejamento", "bd_planejamento_dev")

# Individual
scp.comparar_estruturas_tabelas(**bancos_verificar)
scp.comparar_procedures(**bancos_verificar)

# Conjunto
scp.comparar(**bancos_verificar)

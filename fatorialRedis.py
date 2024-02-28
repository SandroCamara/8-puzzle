import redis

# Conexão com o Redis
# Substitua 'localhost' e '6379' pelos valores apropriados para o seu ambiente Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def fatorial(n):
    # Verificar se o resultado já está no cache
    chave = f"fatorial:{n}"
    resultado = r.get(chave)
    
    if resultado:
        # O resultado foi encontrado no cache, converta para int e retorne
        return int(resultado)
    else:
        # O resultado não está no cache, calcular o fatorial
        if n == 0:
            resultado = 1
        else:
            resultado = n * fatorial(n - 1)
        
        # Armazenar o resultado calculado no cache
        r.set(chave, resultado)
        
        return resultado

# Exemplo de uso
numero = 6
print(f"O fatorial de {numero} é {fatorial(numero)}")

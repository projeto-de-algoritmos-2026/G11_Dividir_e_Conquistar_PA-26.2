from inversion_count import count_inversions

def calcular_similaridade(usuario_ref, usuario_comp):
    
    n = len(usuario_ref)
    if n != len(usuario_comp):
        raise ValueError("Ambas as listas devem conter a mesma quantidade de filmes.")

   
    mapa_posicoes = {filme: idx + 1 for idx, filme in enumerate(usuario_ref)}

   
    arr_numerico = [mapa_posicoes[filme] for filme in usuario_comp]

   
    # Obtém o resultado de inversões (caso o algoritmo retorne lista [inversoes, ...], extrai o valor no índice 0)
    resultado = count_inversions(arr_numerico.copy())
    inversoes = resultado[0] if isinstance(resultado, list) else resultado

    max_inversoes = (n * (n - 1)) // 2
    similaridade = (1.0 - (inversoes / max_inversoes)) * 100.0 if max_inversoes > 0 else 100.0

    pares_invertidos = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr_numerico[i] > arr_numerico[j]:
                filme_a = usuario_comp[i] 
                filme_b = usuario_comp[j] 
                pares_invertidos.append((filme_a, filme_b))

    return inversoes, round(similaridade, 2), pares_invertidos


def rankear_perfis(usuario_atual, banco_perfis):
   
    resultados = []

    for nome, dados in banco_perfis.items():
        ranking_perfil = dados["ranking"]
        avatar = dados.get("avatar", "👤")
        descricao = dados.get("descricao", "")

        inversoes, similaridade, pares_invertidos = calcular_similaridade(usuario_atual, ranking_perfil)

        resultados.append({
            "nome": nome,
            "avatar": avatar,
            "descricao": descricao,
            "inversoes": inversoes,
            "similaridade": similaridade,
            "ranking": ranking_perfil,
            "pares_invertidos": pares_invertidos
        })

    # Ordena: maior similaridade primeiro (menor inversões)
    resultados.sort(key=lambda x: (-x["similaridade"], x["inversoes"]))
    return resultados

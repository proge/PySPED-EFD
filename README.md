PySPED-EFD
==========

Biblioteca para geração de arquivo especificado pelo SPED Fiscal.

Versão: [2.0.11 - Setembro 2012 (PDF)](http://www1.receita.fazenda.gov.br/sistemas/sped-fiscal/download/GUIA_PRATICO_DA_EFD_Versao_2.0.11.pdf).

TODO
----
- Testes
- Verificar campos obrigatórios
- Validar tamanho e tipo dos registros
- Validar arquivo no sistema do governo

DONE
----
- Criar automaticamente registros de início e fim de cada bloco
- Ordenar linhas de acordo com hierarquia definida pelo manual

USAGE
-----
Por enquanto não há um método para a geração do arquivo em si, apenas do seu conteúdo (efd.generate()).

```python
import pysped_efd

efd = pysped_efd.efd(
    COD_FIN='',
    DT_INI='',
    DT_FIN='',
    NOME='',
    CNPJ='',
    CPF='',
    UF='',
    IE='',
    COD_MUN='',
    IM='',
    SUFRAMA='',
    IND_PERFIL='',
    IND_ATIV=''
    )
reg = pysped_efd.r0005(
    FANTASIA='Empresa Teste Ltda',
    CEP='90900-000',
    END='R. Um',
    NUM='1',
    COMPL='101',
    BAIRRO='Único',
    FONE='11 3011 1103',
    FAX='',
    EMAIL='responsavel@empresa.com.br',
    )

efd.add(reg)

# File content result
print efd.generate()
```

# Guia de Ferrados: Pseudoaleatoriedade e Masterworking em Itens Ancestrais

Itens ancestrais, que podem ser todos os lendários ancestrais, únicos ancestrais e os ancestrais míticos únicos, podem ter upgrades distribuídos em diferentes afixos. Cada item possui 4 ou 5 afixos (incluindo *imprintados*, quando suportado pelo item em questão), e os upgrades são aplicados nos ranks 4, 8 e 12.

- **Itens com 4 afixos**: Maior probabilidade de cair o upgrade no afixo desejado, mas menos diversidade.
- **Itens com 5 afixos**: Menor probabilidade de upgrades no afixo exato, mas maior diversidade.

## Probabilidade de Upgrades no Afixo Esperado

A fórmula para calcular a chance de todos os upgrades (ranks 4, 8 e 12) caírem no mesmo afixo é:

$$
P = \left( \frac{1}{n} \right)^3
$$

Onde \( n \) é o número de afixos.

## Cálculo de Probabilidades

- **Para itens com 4 afixos**:
  $$
  P = \left( \frac{1}{4} \right)^3 = \frac{1}{64}, \quad E = \frac{1}{\frac{1}{64}} = 64
  $$
  Número médio de tentativas: 64 resets.
  
- **Para itens com 5 afixos**:
  $$
  P = \left( \frac{1}{5} \right)^3 = \frac{1}{125}, \quad E = \frac{1}{\frac{1}{125}} = 125
  $$
  Número médio de tentativas: 125 resets.

Sendo que o número de afixos permanece os mesmos entre qualquer uma das tentativas, podemos concluir que conseguir o mesmo afixo em todos os ranks tem exatamente a mesma probabilidade em qualquer um dos casos.

## Tabela de Recursos para Masterworking

| Rank   | Efeito                               | Custo                                                                                                                          |
|--------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 1      | Todos os afixos aumentados em 5%     | 10 *Obducite*, 10 *Rawhide* / 10 *Iron Chunk*, 4 *Veiled Crystal*, 2 *Abstruse Sigil*, 1 *Forgotten Soul*, 64k *Gold*          |
| 2      | Todos os afixos aumentados em 5%     | 20 *Obducite*, 12 *Rawhide* / 12 *Iron Chunk*, 6 *Veiled Crystal*, 1 *Forgotten Soul*, 86k *Gold*                              |
| 3      | Todos os afixos aumentados em 5%     | 30 *Obducite*, 16 *Rawhide* / 16 *Iron Chunk*, 6 *Veiled Crystal*, 4 *Abstruse Sigil*, 2 *Forgotten Soul*, 110k *Gold*         |
| **4**  | **Afixo aleatório aumentado em 25%** | **40 *Obducite*, 20 *Rawhide* / 20 *Iron Chunk*, 8 *Veiled Crystal*, 4 *Abstruse Sigil*, 2 *Forgotten Soul*, 150k *Gold***     |
| 5      | Todos os afixos aumentados em 5%     | 60 *Obducite*, 23 *Rawhide* / 23 *Iron Chunk*, 9 *Veiled Crystal*, 5 *Abstruse Sigil*, 2 *Forgotten Soul*, 450k *Gold*         |
| 6      | Todos os afixos aumentados em 5%     | 120 *Obducite*, 25 *Rawhide* / 25 *Iron Chunk*, 10 *Veiled Crystal*, 5 *Abstruse Sigil*, 3 *Forgotten Soul*, 600k *Gold*       |
| 7      | Todos os afixos aumentados em 5%     | 240 *Obducite*, 28 *Rawhide* / 28 *Iron Chunk*, 11 *Veiled Crystal*, 6 *Abstruse Sigil*, 3 *Forgotten Soul*, 800k *Gold*       |
| **8**  | **Afixo aleatório aumentado em 25%** | **360 *Obducite*, 33 *Rawhide* / 33 *Iron Chunk*, 13 *Veiled Crystal*, 7 *Abstruse Sigil*, 3 *Forgotten Soul*, 1.2M *Gold***   |
| 9      | Todos os afixos aumentados em 5%     | 450 *Obducite*, 35 *Rawhide* / 35 *Iron Chunk*, 14 *Veiled Crystal*, 7 *Abstruse Sigil*, 7 *Forgotten Soul*, 1.7M *Gold*       |
| 10     | Todos os afixos aumentados em 5%     | 900 *Obducite*, 38 *Rawhide* / 38 *Iron Chunk*, 15 *Veiled Crystal*, 8 *Abstruse Sigil*, 8 *Forgotten Soul*, 2.3M *Gold*       |
| 11     | Todos os afixos aumentados em 5%     | 1,350 *Obducite*, 40 *Rawhide* / 40 *Iron Chunk*, 16 *Veiled Crystal*, 8 *Abstruse Sigil*, 8 *Forgotten Soul*, 3M *Gold*       |
| **12** | **Afixo aleatório aumentado em 25%** | **2,250 *Obducite*, 45 *Rawhide* / 45 *Iron Chunk*, 18 *Veiled Crystal*, 9 *Abstruse Sigil*, 5 *Forgotten Soul*, 4.5M *Gold*** |

## Reset de Itens

Você pode *resetar* o item em três momentos críticos: 4/12, 8/12 e 12/12. *Resetar* mais cedo economiza recursos, pois o custo de upgrades aumenta com o progresso do item. A cada reset, a chance de sucesso se reinicia.

## Custo de Reset

O custo de reset é constante em qualquer rank:

- **30 *Iron Chunks***
- **20 *Veiled Crystals***
- **5 *Forgotten Souls***
- **5,000,000 *Gold***

## Número Médio de Resets

Levando em conta as três tentativas (ranks 4/12, 8/12 e 12/12), o número esperado de resets para obter os upgrades no afixo desejado pode ser calculado com a seguinte decomposição:

- A probabilidade \( P \) de que os três upgrades (ranks 4, 8, e 12) sejam aplicados ao mesmo afixo é dada por:

$$
P = \left( \frac{1}{n} \right)^3
$$

Onde \( n \) é o número de afixos.

- O número esperado de tentativas \( E \) para que os três upgrades caiam no mesmo afixo é o inverso da probabilidade \( P \), ou seja:

$$
E = \frac{1}{P}
$$

## Cálculo de Tentativas por Número de Afixos

- **Para itens com 4 afixos**:
  $$
  P = \left( \frac{1}{4} \right)^3 = \frac{1}{64}, \quad E = \frac{1}{\frac{1}{64}} = 64
  $$
  Portanto, o número médio de tentativas é **64 resets**.

- **Para itens com 5 afixos**:
  $$
  P = \left( \frac{1}{5} \right)^3 = \frac{1}{125}, \quad E = \frac{1}{\frac{1}{125}} = 125
  $$
  Portanto, o número médio de tentativas é **~125 resets**.

Esses cálculos mostram que, em média, você precisará de 64 tentativas para itens com 4 afixos e 125 tentativas para itens com 5 afixos para obter todos os upgrades no mesmo afixo.

## O Python Não Mente

Para validar os cálculos, podemos simular o processo de conseguir o item perfeito. O (`simulator.py`)[./simulator.py] é um script Python que simula o processo de *masterworking* de um item ancestral. O script gera um item com 4 ou 5 afixos e simula os resets até que todos os upgrades estejam no afixo esperado:

```bash
$ python3 simulator.py
Summary for 4-affix item:
Expected affixes (ranks 4, 8, 12): [1, 3, 0]
Probability of success: 0.015625
Expected runs to get a perfect item: 64

Summary for 5-affix item:
Expected affixes (ranks 4, 8, 12): [2, 0, 1]
Probability of success: 0.008000
Expected runs to get a perfect item: 124

Starting simulation for #1000 turns...
Simulation complete. Results saved to: <REDACTED>

Summary for 4-affix item:
- Average Resets: 63
- Average Rolls: 336

Average Materials Used:
- obducite: 38488
- rawhide: 6082
- iron_chunk: 7978
- veiled_crystal: 3738
- abstruse_sigil: 1198
- forgotten_soul: 987
- gold: 436464460

Summary for 5-affix item:
- Average Resets: 119
- Average Rolls: 599

Average Materials Used:
- obducite: 54853
- rawhide: 10408
- iron_chunk: 13998
- veiled_crystal: 6637
- abstruse_sigil: 2040
- forgotten_soul: 1724
- gold: 777340920
```

## Recursos Recomendados

Para maximizar as chances de obter um item **12/12 perfeito**, é necessário acumular uma verdadeira infinidade de recursos. Para calcular com uma simulação de um simpático milhão de tentativas, utilizei o script abaixo:

```python
import json
from typing import Dict, List

file_path = 'item_simulation_d26fff2b-8534-4c40-8b74-cdd88d42f07d.json'
with open(file_path) as f:
    simulation_data = json.load(f)

def calculate_summary(simulations: List[Dict]) -> Dict[str, float]:
    total_resets = sum(sim['total_resets'] for sim in simulations)
    total_rolls = sum(sim['total_rolls'] for sim in simulations)
    
    total_materials = {key: sum(sim['total_materials'][key] for sim in simulations) for key in simulations[0]['total_materials']}
    num_simulations = len(simulations)

    average_resets = total_resets / num_simulations
    average_rolls = total_rolls / num_simulations
    average_materials = {key: value / num_simulations for key, value in total_materials.items()}

    return {
        'average_resets': average_resets,
        'average_rolls': average_rolls,
        'average_materials': average_materials
    }

summary_4_affixes = calculate_summary(simulation_data['4_affixes'])
summary_5_affixes = calculate_summary(simulation_data['5_affixes'])

summary_4_affixes, summary_5_affixes
```

Abaixo estão as recomendações de recursos para o número médio de tentativas:

### Recursos Recomendados para 64 Resets (4 afixos)

- **Média de Resets**: 63,20
- **Média de Rolls**: 336,22
- **Média de Materiais Utilizados**:
  - ***Obducite***: 38.488,76
  - ***Rawhide***: 6.082,71
  - ***Iron Chunk***: 7.978,59
  - ***Veiled Crystal***: 3.738,04
  - ***Abstruse Sigil***: 1.198,67
  - ***Forgotten Soul***: 987,19
  - ***Gold***: 436.464.460

### Recursos Recomendados para 125 Resets (5 afixos)

- **Média de Resets**: 119,68
- **Média de Rolls**: 599,16
- **Média de Materiais Utilizados**:
  - ***Obducite***: 54.853,61
  - ***Rawhide***: 10.408,41
  - ***Iron Chunk***: 13.998,72
  - ***Veiled Crystal***: 6.637,90
  - ***Abstruse Sigil***: 2.040,36
  - ***Forgotten Soul***: 1.724,53
  - ***Gold***: 777.340.920

## Conclusão

Conseguir um item ancestral 12/12 com todos os upgrades no mesmo afixo é extremamente complexo e dispendioso. Embora a probabilidade de sucesso seja baixa, começar os resets cedo pode reduzir o custo total. Mesmo assim, o jogador deve estar preparado para enfrentar dezenas, ou até centenas, de resets para atingir o item perfeito.

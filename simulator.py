#! /usr/bin/env python3

from pathlib import Path
import random
import json
import tempfile
import uuid
from typing import List, Dict, Any

ATTEMPTS = 1_000

# Tabela de custos por rank
rank_costs: Dict[int, Dict[str, int]] = {
    1: {'obducite': 10, 'rawhide': 10, 'iron_chunk': 10, 'veiled_crystal': 4, 'abstruse_sigil': 2, 'forgotten_soul': 1, 'gold': 64_000},
    2: {'obducite': 20, 'rawhide': 12, 'iron_chunk': 12, 'veiled_crystal': 6, 'abstruse_sigil': 1, 'forgotten_soul': 1, 'gold': 86_000},
    3: {'obducite': 30, 'rawhide': 16, 'iron_chunk': 16, 'veiled_crystal': 6, 'abstruse_sigil': 4, 'forgotten_soul': 2, 'gold': 110_000},
    4: {'obducite': 40, 'rawhide': 20, 'iron_chunk': 20, 'veiled_crystal': 8, 'abstruse_sigil': 4, 'forgotten_soul': 2, 'gold': 150_000},
    5: {'obducite': 60, 'rawhide': 23, 'iron_chunk': 23, 'veiled_crystal': 9, 'abstruse_sigil': 5, 'forgotten_soul': 2, 'gold': 450_000},
    6: {'obducite': 120, 'rawhide': 25, 'iron_chunk': 25, 'veiled_crystal': 10, 'abstruse_sigil': 5, 'forgotten_soul': 3, 'gold': 600_000},
    7: {'obducite': 240, 'rawhide': 28, 'iron_chunk': 28, 'veiled_crystal': 11, 'abstruse_sigil': 6, 'forgotten_soul': 3, 'gold': 800_000},
    8: {'obducite': 360, 'rawhide': 33, 'iron_chunk': 33, 'veiled_crystal': 13, 'abstruse_sigil': 7, 'forgotten_soul': 3, 'gold': 1_200_000},
    9: {'obducite': 450, 'rawhide': 35, 'iron_chunk': 35, 'veiled_crystal': 14, 'abstruse_sigil': 7, 'forgotten_soul': 7, 'gold': 1_700_000},
    10: {'obducite': 900, 'rawhide': 38, 'iron_chunk': 38, 'veiled_crystal': 15, 'abstruse_sigil': 8, 'forgotten_soul': 8, 'gold': 2_300_000},
    11: {'obducite': 1_350, 'rawhide': 40, 'iron_chunk': 40, 'veiled_crystal': 16, 'abstruse_sigil': 8, 'forgotten_soul': 8, 'gold': 3_000_000},
    12: {'obducite': 2_250, 'rawhide': 45, 'iron_chunk': 45, 'veiled_crystal': 18, 'abstruse_sigil': 9, 'forgotten_soul': 5, 'gold': 4_500_000},
}

# Custo de reset
reset_costs: Dict[str, int] = {
    'iron_chunk': 30,
    'veiled_crystal': 20,
    'forgotten_soul': 5,
    'gold': 5_000_000
}

def simulate_perfect_item(num_affixes: int, expected_affixes: List[int]) -> List[Dict]:
    results = []
    
    for _ in range(ATTEMPTS):
        total_resets = 0
        total_rolls = 0
        total_materials = {'obducite': 0, 'rawhide': 0, 'iron_chunk': 0, 'veiled_crystal': 0, 'abstruse_sigil': 0, 'forgotten_soul': 0, 'gold': 0}
        rank_reset_log = []

        while True:
            for rank in range(1, 13):
                current_roll = random.randint(1, num_affixes)
                total_rolls += 1

                # Acumulando o custo de materiais para cada upgrade
                for key in total_materials:
                    total_materials[key] += rank_costs[rank][key]

                # Verificar se o reset deve ocorrer nos ranks 4, 8 ou 12
                if rank in [4, 8, 12]:
                    expected_affix = expected_affixes[(rank // 4) - 1]
                    
                    if expected_affix == 0:
                        expected_affix = 1

                    if current_roll != expected_affix:
                        # Upgrade não caiu no afixo esperado, ou seja, reset pra cabeça
                        total_resets += 1
                        rank_reset_log.append(rank)

                        # Adicionar os custos do reset
                        for key in reset_costs:
                            total_materials[key] += reset_costs[key]

                        # Resetar o item e começar de novo
                        break
            else:
                # Se passou por todos os ranks (1 a 12), o item está perfeito (só acontece aqui)
                results.append({
                    'total_resets': total_resets,
                    'total_rolls': total_rolls,
                    'rank_reset_log': rank_reset_log,
                    'total_materials': total_materials
                })
                break

    return results

def save_results_to_json(data: Dict) -> str:
    filename = f'item_simulation_{uuid.uuid4()}.json'
    temp_dir = Path(tempfile.gettempdir())
    file_path = temp_dir / filename
    
    with file_path.open('w') as f:
        raw_json = json.dumps(data, indent=4)
        f.writelines(raw_json)
    
    return str(file_path)


def generate_summary(results: List[Dict]) -> Dict[str, Any]:
    total_resets = sum(result['total_resets'] for result in results)
    total_rolls = sum(result['total_rolls'] for result in results)
    total_materials = {
        'obducite': sum(result['total_materials']['obducite'] for result in results),
        'rawhide': sum(result['total_materials']['rawhide'] for result in results),
        'iron_chunk': sum(result['total_materials']['iron_chunk'] for result in results),
        'veiled_crystal': sum(result['total_materials']['veiled_crystal'] for result in results),
        'abstruse_sigil': sum(result['total_materials']['abstruse_sigil'] for result in results),
        'forgotten_soul': sum(result['total_materials']['forgotten_soul'] for result in results),
        'gold': sum(result['total_materials']['gold'] for result in results),
    }

    num_results = len(results)
    summary = {
        'average_resets': total_resets // num_results,
        'average_rolls': total_rolls // num_results,
        'average_materials': {key: total_materials[key] // num_results for key in total_materials},
    }

    return summary

def print_materials(average_materials: Dict[str, float]):
    for material, amount in average_materials.items():
        print(f'- {material}: {amount}')


def calculate_probability(num_affixes: int, expected_affixes: List[int]) -> float:
    probability = 1.0
    for _ in expected_affixes:
        probability *= 1 / num_affixes  # Probabilidade de acertar o afixo esperado
    return probability

def expected_runs(probability: float) -> int:
    return int(1 / probability)


expected_affixes_4: List[int] = [1, 3, 0]  # Afixos esperados nos ranks 4, 8 e 12 para itens com 4 afixos
expected_affixes_5: List[int] = [2, 0, 1]  # Afixos esperados nos ranks 4, 8 e 12 para itens com 5 afixos

# Exemplo com 4 afixos
prob_4_affixes = calculate_probability(4, expected_affixes_4)
expected_runs_4 = expected_runs(prob_4_affixes)

# Exemplo com 5 afixos
prob_5_affixes = calculate_probability(5, expected_affixes_5)
expected_runs_5 = expected_runs(prob_5_affixes)

print(f'Summary for 4-affix item:')
print(f'Expected affixes (ranks 4, 8, 12): {expected_affixes_4}')
print(f'Probability of success: {prob_4_affixes:.6f}')
print(f'Expected runs to get a perfect item: ~{expected_runs_4}')
print()

print(f'Summary for 5-affix item:')
print(f'Expected affixes (ranks 4, 8, 12): {expected_affixes_5}')
print(f'Probability of success: {prob_5_affixes:.6f}')
print(f'Expected runs to get a perfect item: ~{expected_runs_5}')
print()

print(f'Starting simulation for #{ATTEMPTS} turns...')

# Simulando para 4 e 5 afixos
simulation_4_affixes = simulate_perfect_item(4, expected_affixes_4)
simulation_5_affixes = simulate_perfect_item(5, expected_affixes_5)

# Juntando os resultados
simulation_results = {
    '4_affixes': simulation_4_affixes,
    '5_affixes': simulation_5_affixes
}

# Salvando o resultado em um arquivo JSON
json_file_path = save_results_to_json(simulation_results)
print(f'Simulation complete. Results saved to: {json_file_path}')
print()

summary_4_affixes = generate_summary(simulation_4_affixes)
summary_5_affixes = generate_summary(simulation_5_affixes)

print('Summary for 4-affix item:')
print(f'- Average Resets: {summary_4_affixes['average_resets']}')
print(f'- Average Rolls: {summary_4_affixes['average_rolls']}')
print()
print('Average Materials Used:')
print_materials(summary_4_affixes['average_materials'])
print()

print('Summary for 5-affix item:')
print(f'- Average Resets: {summary_5_affixes['average_resets']}')
print(f'- Average Rolls: {summary_5_affixes['average_rolls']}')
print()
print('Average Materials Used:')
print_materials(summary_5_affixes['average_materials'])

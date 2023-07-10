current_master = input()
nb_of_duals = int(input())
master_list = current_master[:]

def clean_add(masterlist: str, master:str):
    if masterlist.find(master) == -1:
        return masterlist + master
    else:
        return masterlist

for dual in range(nb_of_duals):
    battle = input()
    battle_winner = battle[0]
    battle_looser = battle[-1]
    if battle_looser == current_master:
        current_master = battle_winner
        master_list = clean_add(master_list, current_master)
print(current_master)
print(f'{len(master_list)}')

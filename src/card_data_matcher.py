from algorithms import radix_sort as sort
import pandas as pd
PATH_TO_carddump1 = "data/carddump1.csv"
PATH_TO_carddump2 = "data/carddump2.csv"
PATH_TO_SAVE = "outputs/tables/carddump2_sorted.csv"

def sort_date_and_pin(filepath, savepath):
    shuffled_card_data = pd.read_csv(filepath, dtype={"PIN":str})

    data = shuffled_card_data['Expiry Date'].values.copy()
    pin = shuffled_card_data["PIN"].values.copy()
    for j in range(len(data)):
        for i, letter in enumerate(data[j]):
            if letter == '/':
                data[j] = data[j][i+1:]
                break
            data[j]+=data[j][i]
    for i in range(len(data)):
        data[i]+=pin[i]
        data[i]=int(data[i])
        data[i]*=100000
        data[i]+=i

    sorted_data = sort(data)

    sorted_indices = [num % 100000 for num in sorted_data]

    result_df = shuffled_card_data.iloc[sorted_indices].reset_index(drop=True)

    result_df.to_csv(savepath, index=False)



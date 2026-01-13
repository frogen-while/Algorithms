import sys
from pathlib import Path
root_path = str(Path(__file__).parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)

from src import algorithms as sort
import pandas as pd
PATH_TO_carddump1 = "data/carddump1.csv"
PATH_TO_carddump2 = "data/carddump2.csv"
PATH_TO_SAVE_carddump2_SORTED = "outputs/tables/carddump2_sorted.csv"
PATH_TO_SAVE_FULL = "outputs/tables/carddump_full_sorted.csv"


def sort_date_and_pin_df(
    card_df: pd.DataFrame,
    savepath: str | None = None,
    func=sort.bubble_sort,
    needtosave: bool = False,
):
    shuffled_card_data = card_df.copy()

    data = shuffled_card_data['Expiry Date'].values.copy()
    pin = shuffled_card_data["PIN"].values.copy()

    for j in range(len(data)):
        for i, letter in enumerate(data[j]):
            if letter == '/':
                data[j] = data[j][i + 1:]
                break
            data[j] += data[j][i]

    for i in range(len(data)):
        data[i] += pin[i]
        data[i] = int(data[i])
        data[i] *= 100000
        data[i] += i

    sorted_data = func(data)

    sorted_indices = [num % 100000 for num in sorted_data]

    result_df = shuffled_card_data.iloc[sorted_indices].reset_index(drop=True)
    if needtosave:
        if savepath is None:
            raise ValueError("savepath must be provided when needtosave=True")
        result_df.to_csv(savepath, index=False)
        return None

    return result_df

def sort_date_and_pin(filepath, savepath, func = sort.bubble_sort, needtosave=False):
    shuffled_card_data = pd.read_csv(filepath, dtype={"PIN":str,"Verification Code":str})
    return sort_date_and_pin_df(
        shuffled_card_data,
        savepath=savepath,
        func=func,
        needtosave=needtosave,
    )
    
    

def combine_card_data(filepath1, filepath2, savepath):

    data = pd.read_csv(filepath2, dtype={"PIN":str,"Verification Code":str}).copy()
    l_part = pd.read_csv(filepath1, dtype={"Credit Card Number":str})['Credit Card Number'].values.copy()
    r_part = pd.read_csv(filepath2, dtype={"Credit Card Number":str})['Credit Card Number'].values.copy()

    l_part = [str(number).replace("*", "") for number in l_part]
    r_part = [str(number).replace("*", "")[3:] for number in r_part]

    full_card_numbers = [l_part[i]+r_part[i] for i in range(len(l_part))]

    full_data = data.drop('Credit Card Number', axis=1)
    full_data.insert(loc=0, column='Credit Card Number', value=full_card_numbers)
    full_data.to_csv(savepath, index=False)
  
if __name__ == "__main__":   
    sort_date_and_pin(PATH_TO_carddump2, PATH_TO_SAVE_carddump2_SORTED, )
    combine_card_data(PATH_TO_carddump1, PATH_TO_SAVE_carddump2_SORTED, PATH_TO_SAVE_FULL)


     



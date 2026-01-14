import subprocess
from tqdm import tqdm

from benchmarks import cdh_benchmark as cdh
from benchmarks import quick_sort_pivot_benchmark as qs
from benchmarks import sort_algorithms_benchmark as sa
from benchmarks import trees_benchmark as trs
from benchmarks import vector_benchmark as vctr
from src import card_data_handler as cdhd

def main() -> None:
    print(
        "Choose an option:\n"
        " 1 Run all benchmarks\n"
        " 2 Run all tests\n"
        " 3 Run selected benchmarks\n"
        " 4 Ordnung muss sein (combine card data)"
    )
    user_choice = int(input(" > "))

    if user_choice < 1 or user_choice > 4:
        raise ValueError("Wrong input. Please enter a number between 1 and 4")

    benchmarks = [
        ("Card data handler benchmark", cdh.build),
        ("Quick sort multi pivot benchmark", qs.build),
        ("Sorting algorithms benchmark", sa.build),
        ("Trees benchmark", trs.build),
        ("Vector benchmark", vctr.build),
    ]

    match user_choice:
        case 1:
            for name, bench in tqdm(benchmarks, desc="Processing benchmarks"):
                bench()
                print(name + " completed")
        case 2:
            subprocess.run("test.bat")
        case 3:
            selected_indices: set[int] = set()
            while True:
                print("Select which benchmarks to run")
                for i, bench in enumerate(benchmarks, start=1):
                    print(f" {i} {bench[0]}")
                print(" 0 Start")

                choice = int(input(" > "))
                if choice == 0:
                    for idx in tqdm(sorted(selected_indices), desc="Processing benchmarks"):
                        name, bench = benchmarks[idx]
                        bench()
                        print(name + " completed")
                    break

                idx = choice - 1
                if idx < 0 or idx >= len(benchmarks):
                    print("Choice out of range")
                    continue
                if idx in selected_indices:
                    print("This benchmark is already selected")
                    continue
                selected_indices.add(idx)
        case 4:
            print("Starting data processing...")
            cdhd.sort_date_and_pin(cdhd.PATH_TO_carddump2, cdhd.PATH_TO_SAVE_carddump2_SORTED, needtosave=True)
            cdhd.combine_card_data(cdhd.PATH_TO_carddump1, cdhd.PATH_TO_SAVE_carddump2_SORTED, cdhd.PATH_TO_SAVE_FULL)
            print("Done")


if __name__ == "__main__":
    main()
                



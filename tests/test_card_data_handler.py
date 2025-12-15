import sys
from pathlib import Path
root_path = str(Path(__file__).parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)


import unittest
import os
import pandas as pd
from src import card_data_handler as cdh
from src import algorithms as alg
def get_correct_expected(df):
    temp = df.copy()

    temp['sort_date'] = pd.to_datetime(temp['Expiry Date'], format='%m/%Y')

    temp = temp.sort_values(by=['sort_date', 'PIN'], kind='mergesort')

    return temp.drop(columns='sort_date').reset_index(drop=True)
class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        if not os.path.exists("tests/temp"):
            os.makedirs("tests/temp")

        # Uncomment to create temp .csv files after tests
        # df_empty = pd.DataFrame(columns=['Expiry Date', 'PIN'])
        # df_random = pd.DataFrame(data={
        #     'Expiry Date':['08/2024', '03/2021', '11/2029', '05/2022', '12/2020', '02/2026', '10/2023', '01/2028', '07/2025', '04/2027', '09/2021', '06/2024', '11/2022', '03/2030', '05/2029', '12/2025', '02/2021', '08/2023', '10/2027', '01/2022'], 
        #     'PIN':['4829', '1053', '7264', '3918', '8502', '2741', '6195', '9380', '5026', '1473', '8837', '2610', '5942', '4031', '7596', '1284', '6309', '9175', '3458', '2067']
        # })
        # df_sorted_data = pd.DataFrame(data={
        #     'Expiry Date':['03/2020', '08/2020', '12/2020', '02/2021', '03/2021', '05/2021', '09/2021', '01/2022', '05/2022', '07/2022', '06/2023', '08/2023', '10/2023', '02/2024', '06/2024', '08/2024', '01/2025', '07/2025', '11/2025', '03/2030'],
        #     'PIN':['1053', '1284', '1473', '2067', '2610', '2741', '3458', '3918', '4031', '4829', '5026', '5942', '6195', '6309', '7264', '7596', '8502', '8837', '9175', '9380']
        # })
        # df_reversed = pd.DataFrame(data={
        #     'Expiry Date':['03/2030', '11/2025', '07/2025', '01/2025', '08/2024', '06/2024', '02/2024', '10/2023', '08/2023', '06/2023', '07/2022', '05/2022', '01/2022', '09/2021', '05/2021', '03/2021', '02/2021', '12/2020', '08/2020', '03/2020'], 
        #     'PIN':['9380', '9175', '8837', '8502', '7596', '7264', '6309', '6195', '5942', '5026', '4829', '4031', '3918', '3458', '2741', '2610', '2067', '1473', '1284', '1053']
        # })
        # df_same_dates = pd.DataFrame(data={
        #     'Expiry Date': ['01/2025'] * 20,
        #     'PIN': ['9999', '0001', '5555', '1234', '8888', '2222', '4444', '3333', '7777', '6666', '1000', '0999', '4321', '0010', '0100', '9000', '5000', '2500', '7500', '1111']
        # })
        # df_duplicates = pd.DataFrame(data={
        #     'Expiry Date': ['03/2021', '03/2021', '12/2020', '12/2020', '05/2025', '05/2025', '01/2022', '01/2022', '08/2023', '08/2023','10/2027', '10/2027', '04/2024', '04/2024', '06/2021', '06/2021', '11/2029', '11/2029', '02/2026', '02/2026'],
        #     'PIN': ['1111', '1111', '2222', '2222', '3333', '3333', '4444', '4444', '5555', '5555', '6666', '6666', '7777', '7777', '8888', '8888', '9999', '9999', '0000', '0000']
        # })
        # df_leading_zeros = pd.DataFrame(data={
        #     'Expiry Date': ['01/2020', '02/2020', '03/2020', '04/2020', '05/2020', '06/2020', '07/2020', '08/2020', '09/2020', '10/2020','11/2020', '12/2020', '01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021', '07/2021', '08/2021'],
        #     'PIN': ['0009', '0008', '0007', '0006', '0005', '0004', '0003', '0002', '0001', '0000','0019', '0018', '0017', '0016', '0015', '0014', '0013', '0012', '0011', '0010']
        # })
        # df_century_clash = pd.DataFrame(data={
        #     'Expiry Date': ['01/1999', '12/1999', '01/2000', '02/2000', '05/1980', '08/2010', '10/2023', '03/2024', '11/2025', '06/2030', '01/1990', '12/1991', '04/2005', '07/2015', '09/2022', '02/2028', '05/2040', '08/2050', '11/1970', '03/2001'],
        #     'PIN': ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1016', '1017', '1018', '1019', '1020']
        # })


        # self.files_map = {
        #     "empty": df_empty,
        #     "random": df_random,
        #     "sorted": df_sorted_data,
        #     "reversed": df_reversed,
        #     "same_dates": df_same_dates,
        #     "century_clash":df_century_clash,
        #     "df_duplicates":df_duplicates,
        #     "df_leading_zeros":df_leading_zeros

        # }

        # for name, df in self.files_map.items():
        #     df.to_csv(f"tests/temp/{name}.csv", index=False)

        df_empty = pd.read_csv("tests/temp/empty.csv",dtype={"PIN":str,"Verification Code":str})
        df_random = pd.read_csv("tests/temp/random.csv",dtype={"PIN":str,"Verification Code":str})
        df_sorted = pd.read_csv("tests/temp/sorted.csv",dtype={"PIN":str,"Verification Code":str})
        df_reversed = pd.read_csv("tests/temp/reversed.csv",dtype={"PIN":str,"Verification Code":str})
        df_same_dates = pd.read_csv("tests/temp/same_dates.csv",dtype={"PIN":str,"Verification Code":str})
        df_century_clash = pd.read_csv("tests/temp/century_clash.csv",dtype={"PIN":str,"Verification Code":str})
        df_duplicates = pd.read_csv("tests/temp/df_duplicates.csv",dtype={"PIN":str,"Verification Code":str})
        df_leading_zeros = pd.read_csv("tests/temp/df_leading_zeros.csv",dtype={"PIN":str,"Verification Code":str})

        self.expected = {
            "empty": df_empty,
            "random": get_correct_expected(df_random),
            "sorted": get_correct_expected(df_sorted),
            "reversed": get_correct_expected(df_reversed),
            "same_dates": get_correct_expected(df_same_dates),
            "century_clash":get_correct_expected(df_century_clash),
            "df_duplicates":get_correct_expected(df_duplicates),
            "df_leading_zeros":get_correct_expected(df_leading_zeros)
        }
    # Uncomment to delete temp .csv files after tests
    # def tearDown(self):
    #     if os.path.exists('tests/temp'):
    #         for filename in os.listdir('tests/temp'):
    #             file_path = os.path.join('tests/temp', filename)
    #             if os.path.isfile(file_path):
    #                 os.remove(file_path)


    def test_all_sorts(self):
        for case_name, expected_df in self.expected.items():
            file_path = f"tests/temp/{case_name}.csv"
            

            result_df = cdh.sort_date_and_pin(file_path, savepath=None, needtosave=False)
            result_df = result_df.reset_index(drop=True)
            
            with self.subTest(case=case_name):
                pd.testing.assert_frame_equal(result_df, expected_df, obj=f"Failed: on {case_name}", check_dtype=False, check_column_type=False)

if __name__ == '__main__':
    unittest.main()
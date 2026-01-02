import unittest
from src import vector as v

class TestVector(unittest.TestCase):

    def setUp(self):
        self.oVector = v.Vector()
        self.testData = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.testDataCap = 1
        while self.testDataCap < len(self.testData):
            self.testDataCap *= 2

    def test_push_back(self):
        for el in self.testData:
            self.oVector.push_back(value=el)
        self.assertEqual(self.oVector.size(), len(self.testData), "Failed: unexpected size")

        vectorData = [self.oVector.at(index=i) for i in range(self.oVector.size())]
        
        self.assertEqual(vectorData, self.testData,"Failed: unexpected order")        

        self.assertEqual(self.oVector.capacity(), self.testDataCap,"Failed: unexpected capacity")

    def test_pop_back(self):
        for el in self.testData:
            self.oVector.push_back(value=el)
        self.oVector.pop_back()
        self.assertEqual(self.oVector.size(), len(self.testData)-1, "Failed: unexpected size")

    def test_pop_back_empty(self):
        emptyVector = v.Vector()
        with self.assertRaises(IndexError):
            emptyVector.pop_back()

    def test_resize(self):
        truncate = int(len(self.testData)/2)
        expand = len(self.testData)*2

        tempVector = v.Vector()
        for el in self.testData:
            tempVector.push_back(value=el)
        tempVector.resize(truncate)
        self.assertEqual(tempVector.size(), truncate, "Failed: unexpected size")
        self.assertEqual(tempVector.capacity(), self.testDataCap, "Failed: unexpected capacity")

        self.oVector = v.Vector()
        for el in self.testData:
            self.oVector.push_back(value=el)
        expected_cap_after_expand = self.testDataCap
        while expected_cap_after_expand < expand:
            expected_cap_after_expand *= 2

        tempVector.resize(expand)
        self.assertEqual(tempVector.size(), expand, "Failed: unexpected size")
        self.assertEqual(tempVector.capacity(), expected_cap_after_expand, "Failed: unexpected capacity")

    def test_insert(self):
        oVector = v.Vector()
        oVector.push_back(1)
        oVector.push_back(3)
        oVector.insert(1, 2)
        self.assertEqual([oVector.at(i) for i in range(oVector.size())], [1, 2, 3])

        oVector2 = v.Vector()
        oVector2.push_back(1)
        with self.assertRaises(IndexError):
            oVector2.insert(5, 99)

        oVector3 = v.Vector()
        oVector3.push_back(1)
        with self.assertRaises(IndexError):
            oVector3.insert(-1, 99)

    def test_push_back_scenarios(self):
        scenarios = [
            ("Powers of 2", [1, 2, 4, 8, 16]),
            ("Strings", ["hello", "world", "test"]),
            ("Mixed", [1, "two", 3.0, None]),
            ("Single Element", [42]),
            ("Empty", [])
        ]

        for name, data in scenarios:
            with self.subTest(case=name):
                oVector = v.Vector() 
                for item in data:
                    oVector.push_back(item)
                self.assertEqual(oVector.size(), len(data), f"Size mismatch in case '{name}'")
                cur_data = [oVector.at(i) for i in range(oVector.size())]
                self.assertEqual(cur_data, data, f"Content mismatch in case '{name}'")
                expected_cap = 1
                while expected_cap < len(data):
                    expected_cap *= 2

                self.assertEqual(oVector.capacity(), expected_cap, f"Capacity mismatch in case '{name}'")

    def test_at_invalid_indices(self):
        bad_indices = [-2, -1, 3, 4]
        oVector = v.Vector()

        for index in bad_indices:
            with self.subTest(bad_index=index):
                with self.assertRaises(IndexError, msg=f"at({index}) should fail"):
                    oVector.at(index)

if __name__ == "__main__":
    unittest.main()

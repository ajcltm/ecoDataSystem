from etl_task.staging import staging_pickle
from etl.transform.transformer_stockcorpfnltt import Transformer_stockcorpfnltt
import unittest
from pathlib import Path


class transformer_stockcorpfnltt_test(unittest.TestCase):

    def test_transform(self):
        data = staging_pickle.load_pickle("250820_125715 stockcorpfnltt_2024.pkl")
        data = Transformer_stockcorpfnltt().transform(data)
        print(data)

if __name__ == "__main__":
    unittest.main()

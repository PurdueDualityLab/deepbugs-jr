import keras
import unittest


model = keras.models.load_model("deepbug_model.keras")

class TestTester(unittest.TestCase):
    def test_function(self):
        ##TODO: make smaller test pool
        #model_mdata = model.evaluate(data_test, labels_test)
        self.assertEqual(1, 1)

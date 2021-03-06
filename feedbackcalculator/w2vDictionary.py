import numpy as np
import pandas as pd
from typing import Tuple, List


class W2vDictionary:
    def __init__(self, vocabulary_path: str, vocabulary_length: int):
        self._vocabulary_length = vocabulary_length
        self._words: List[str] = pd.read_csv(
            vocabulary_path, sep=' ', quoting=3, header=None, usecols=(0,), na_filter=False).values.squeeze().tolist()
        self._vectors: np.ndarray = pd.read_csv(vocabulary_path, sep=' ', quoting=3, header=None,
                                                usecols=range(1, vocabulary_length + 1), na_filter=False,
                                                dtype=np.float32).values
        self._dictionary = {}
        index = 0
        for word in self._words:
            self._dictionary[word] = index
            index += 1

    def get_word_vector(self, word: str):
        return self._vectors[self._dictionary[word]]

    def get_vector_from_index(self, index: int):
        return self._vectors[index]

    @property
    def words(self):
        return self._words

    @property
    def dictionary(self):
        return self._dictionary

    @property
    def vocabulary_length(self) -> int:
        return self._vocabulary_length

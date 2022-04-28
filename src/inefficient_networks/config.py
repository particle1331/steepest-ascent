from pydantic import BaseModel
from pathlib import Path


class Config(BaseModel):
    PACKAGE_DIR = Path(__file__).parent.resolve()
    DATASET_DIR = PACKAGE_DIR / "data"
    TRAINED_MODELS_DIR = PACKAGE_DIR / "trained_models"

    # Create directories
    TRAINED_MODELS_DIR.mkdir(exist_ok=True)
    DATASET_DIR.mkdir(exist_ok=True)


    def set_tensorflow_seeds(self, seed=0):
        import tensorflow as tf
        import numpy as np
        import random as python_random

        np.random.seed(seed)
        python_random.seed(seed)
        tf.random.set_seed(seed)

    def set_matplotlib(self, format="svg"):
        from matplotlib_inline import backend_inline
        backend_inline.set_matplotlib_formats(format)

    def set_ignore_warnings(self):
        import warnings
        warnings.simplefilter(action='ignore')

    def list_tensorflow_devices(self):
        import tensorflow as tf
        return tf.config.list_physical_devices()


config = Config()
'''
This is a global default file, each individual project will have their own respective default file
'''
from .config import CfgNode as CN

C = CN()

C.CONFIG_DIR = 'config/'
C.OUTPUT_BASE_DIR = 'output/'

C.SEED = 7

C.MODEL = CN()
C.MODEL.TYPE = 'unet'
C.MODEL.OUT_CHANNELS = 1
C.MODEL.IN_CHANNELS = 2
C.MODEL.LOSS_TYPE = 'FrankensteinLoss'

C.DATALOADER = CN()
C.DATALOADER.NUM_WORKER = 8
C.DATALOADER.SHUFFLE = True

C.DATASET = CN()
C.DATASET.PATH = ''
C.DATASET.MODE = ''
C.DATASET.SENTINEL1 = CN()
C.DATASET.SENTINEL1.BANDS = ['VV', 'VH']
C.DATASET.SENTINEL1.TEMPORAL_MODE = 'bi-temporal'
C.DATASET.SENTINEL2 = CN()
C.DATASET.SENTINEL2.BANDS = ['B2', 'B3', 'B4', 'B8', 'B11', 'B12']
C.DATASET.SENTINEL2.TEMPORAL_MODE = 'bi-temporal'
C.DATASET.ALL_CITIES = []
C.DATASET.TEST_CITIES = []

C.OUTPUT_BASE_DIR = ''

C.TRAINER = CN()
C.TRAINER.LR = 1e-4
C.TRAINER.BATCH_SIZE = 16
C.TRAINER.EPOCHS = 50

C.AUGMENTATION = CN()
C.AUGMENTATION.CROP_TYPE = 'none'
C.AUGMENTATION.CROP_SIZE = 32
C.RANDOM_FLIP = True
C.RANDOM_ROTATE = True


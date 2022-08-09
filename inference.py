from os import listdir, path
import numpy as np
import scipy
import cv2
import os
import sys
import argparse
import audio
import json
import subprocess
import random
import string
from tqdm import tqdm
from glob import glob
import torch
import face_detection
from models import Wav2Lip
import platform
print("#$$$")

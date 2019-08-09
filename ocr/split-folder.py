
import split_folders
from tqdm import tqdm
tqdm(split_folders.ratio('../letters', output="../data", seed=1337, ratio=(.8, .2)))
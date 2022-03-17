import os
import zipfile
import glob
import pandas as pd

def get_data():
	os.system('kaggle datasets download -d rajyellow46/wine-quality')

	for item in os.walk("."):
		listfile = item[2]
		break

	for file in listfile:
		if 'zip' in file:
			fantasy_zip = zipfile.ZipFile(file)
			fantasy_zip.extractall()

			fantasy_zip.close()

	for item in os.walk("."):
		listfile = item[2]
		break

	for file in listfile:
		if 'csv' in file:
			data = pd.read_csv(file)

	for file in glob.glob('*.zip'):
		os.remove(file)

	for file in glob.glob('*.csv'):
		os.remove(file)

	return data

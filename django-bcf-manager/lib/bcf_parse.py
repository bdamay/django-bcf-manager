import xmlschema
from datetime import datetime
import zipfile
import os
import shutil




def run():
    extraded_dir = 'EXT'
    with zipfile.ZipFile("./SONZAY_DAMAY_APD_BCF.bcfzip", "r") as zip_ref:
        zip_ref.extractall(extraded_dir)
    schema = xmlschema.XMLSchema('./Schemas/2.0/markup.xsd')
    dirs = [o[1] for o in os.walk('./'+extraded_dir)][0]
    for note in dirs:
        dict = schema.to_dict(os.path.join(extraded_dir,note,'markup.bcf'))
        print(dict['Topic']['Title']) # temporary 
    shutil.rmtree(extraded_dir)


if __name__ == '__main__':
    start = datetime.now()
    print('start: ', start)
    run()
    end = datetime.now()
    print('end: ', end)

print('Ending')
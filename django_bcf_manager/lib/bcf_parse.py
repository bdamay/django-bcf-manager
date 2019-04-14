import xmlschema
from datetime import datetime
import zipfile
import os
import shutil

SCHEMAS_DIR = '../assets/BCF/Schemas/'
VERSION_SCHEMA = xmlschema.XMLSchema('../assets/BCF/Schemas/2.1/version.xsd')
# assuming schema will not change with version as we need schema to read version...


def extract_content_from_bcfzip(filename, temp_dir):
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    # first we need to read version
    version = '2.0'

    # then we extract schemas from version
    project_schema = xmlschema.XMLSchema(os.path.join(SCHEMAS_DIR, version, 'project.xsd'))
    markup_schema = xmlschema.XMLSchema(os.path.join(SCHEMAS_DIR, version, 'markup.xsd'))
    viewpoint_schema = xmlschema.XMLSchema(os.path.join(SCHEMAS_DIR, version, 'visinfo.xsd'))

    #One subdirectory = one BCF issue containing markup.bcf, viewpoint.bcfv and snapshots
    issues = [o[1] for o in os.walk('./' + temp_dir)][0]
    topics = []
    for issue in issues:
        markup = markup_schema.to_dict(os.path.join(temp_dir, issue, 'markup.bcf'))
        #viewpoint = viewpoint_schema.to_dict(os.path.join(temp_dir, issue, 'viewpoint.bcfv'))
        topics.append(markup)
    shutil.rmtree(temp_dir)

    return topics

def run():
    topics = extract_content_from_bcfzip("../media/bcf/Annotations.bcfzip", 'TEMP_EXTRACTED')
    [print(t) for t in topics]


if __name__ == '__main__':
    start = datetime.now()
    print('start: ', start)
    run()
    end = datetime.now()
    print('end: ', end)

print('Ending')

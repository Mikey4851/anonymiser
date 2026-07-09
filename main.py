
import os
from pydicom import dcmread
from metadata import check_if_anonymised
from generate_report import generate_report
from save_to_excel import save_to_excel

folder = os.fsencode("dicom_files")
passed = 0
failed = 0
images = []

for file in os.listdir(folder):
    image = {}

    file_name = os.fsdecode(file)
    ds = dcmread(f"dicom_files/{file_name}")
    
    image["name"] = file_name

    if check_if_anonymised(ds):
        passed += 1
        image["status"] = "passed"
    else:
        failed += 1
        image["status"] = "failed"

    images.append(image)

generate_report(passed, failed)
save_to_excel(images)
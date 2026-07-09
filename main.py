
import os
from pydicom import dcmread
from metadata import check_if_anonymised
from generate_report import generate_report

folder = os.fsencode("dicom_files")
passed = 0
failed = 0

for file in os.listdir(folder):
    file_name = os.fsdecode(file)
    ds = dcmread(f"dicom_files/{file_name}")
    
    if check_if_anonymised(ds):
        passed += 1
    else:
        failed += 1


generate_report(passed, failed)

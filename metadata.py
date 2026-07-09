
from pydicom import dcmread

"""
1. Loop through metadata
2. Check if it exists
3. Check if it display 'ANONYMOUS'
4. Check if it contains hashtags
"""

def check_if_anonymised(ds):
    data_passed = 0

    for i in ds:
        try:
            if str(i.value).upper() == "ANONYMOUS" or "#" in str(i.value) or str(i.value).strip() == "" or i.name == "Modality":
                data_passed += 1
            else:
                print(f"Failed: {i.keyword} - {i.value}")
        except Exception as e:
            data_passed += 1


    if len(ds) == data_passed:
        print("File passed")
        return True
    else:
        print("File failed")
        return False

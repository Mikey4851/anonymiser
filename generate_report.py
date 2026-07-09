
def generate_report(passed, failed):
    percentage_passed = (passed / (passed + failed)) * 100
    print("_"*40)
    print(f"\n{round(percentage_passed, 1)}% of files passed ({passed}/{(passed+failed)})\n{failed} file(s) failed the anonymisation check")
    print("_"*40)

generate_report(70, 20)
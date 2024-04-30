def spreadsheet_id_extractor(url):
    BASE_URL = "https://docs.google.com/spreadsheets/d/"
    stripped_url = url.split("/")
    return stripped_url

test_input = input("Enter url: ")

print(spreadsheet_id_extractor(test_input))
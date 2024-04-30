def spreadsheet_id_extractor(url):
    BASE_URL = "https://docs.google.com/spreadsheets/d/"
    BASE_SPLITTER = "d"
    stripped_url = url.split("/")
    index_splitter = stripped_url.index(BASE_SPLITTER)
    return stripped_url[index_splitter + 1]

test_input = input("Enter url: ")

print(spreadsheet_id_extractor(test_input))
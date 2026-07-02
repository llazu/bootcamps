#flat text is plain data but can grow and consume a lot of memory

# Not using generators strains limited memory.
# You could get a memory Error.
def csv_reader(file_name):
    open(file_name)
    result = file_name.read().split("\n")
    return result

# unlike the csv reader above, we only process one line at a time.
# we never process the entire file at one go.
# this leaves a small memory footprint.
# very good to use with Big Data.

filename = "techcrunch.csv"
lines =(line for line in open(filename))
list_line = (s.strip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data))for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")


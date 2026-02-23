contents = [
    "Suspendisse euismod, ex vitae vestibulum semper, velit orci tincidunt diam, vitae dignissim augue lectus ac orci.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Phasellus elit neque, porttitor eget ultricies eget, gravida ut quam."
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
    file.close()
contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced.", "More dummy text about carrot cutting"]

filenames = ["doc.txt", 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"bonusFolder/files/{filename}",'w')
    file.write(content)

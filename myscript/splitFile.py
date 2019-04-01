
with open('oldTinyTwitterForTest.json', 'r') as reader:

    counter = 0
    findex = 0
    for line in reader:
        if counter==0:
            writer = open('file-'+str(findex)+'.json', 'w')
        print >> writer, line.strip()
        counter += 1
        if counter >= 500:
            writer.close()
            counter = 0
            findex += 1

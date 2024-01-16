books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

organize = []
organize.append(authors[1] + ' : ' + books[3])
organize.append(authors[3] + ' : ' + books[1])
organize.append(authors[0] + ' : ' + books[2])
organize.append(authors[2] + ' : ' + books[0])
organize.append(authors[4] + ' : ' + books[4])

for x in organize:
    print(x)
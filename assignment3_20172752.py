import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        try:
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            elif parse[0] == 'del':
                i = 0
                for p in scdb:
                    for i in scdb:
                        if i['Name'] == parse[1]:
                            scdb.remove(i)
            elif parse[0] == 'show':
                try:
                    sortKey ='Name' if len(parse) == 1 else parse[1]
                    showScoreDB(scdb, sortKey)
                except KeyError as e:
                    print('input error')
            elif parse[0] == 'quit':
                break
            elif parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + p[attr], end=' ')
                        print()
            elif parse[0] == 'inc':
                try:
                    x = int(parse[2])
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            p['Score'] = int(p['Score']) + x
                            p['Score'] = str(p['Score'])
                except ValueError as e:
                    print('input error')
            else:
                print("Invalid command: " + parse[0])
        except IndexError as e:
            print('input error')


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

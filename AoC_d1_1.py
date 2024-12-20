def distances(inputfile):
    loca = []
    locb = []

    with open(inputfile) as infile:
        for thing in infile.readlines():
            thing1, thing2 = thing.split()
            loca.append(int(thing1))
            locb.append(int(thing2))
    
    loca.sort()
    locb.sort()

    total = 0
    for i in range(0, len(loca)):
        total += abs(loca[i]-locb[i])
    
    return(total)

if __name__ == '__main__':
    result = distances('AoC_d1_1_input.txt')
    print('Total Distance: ', result)
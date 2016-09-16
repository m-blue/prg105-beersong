def beers(num_beers):
    n = str(num_beers)
    if num_beers > 0:
        str(n)
        print (n + " bottles of beer on the wall")
        print (n + " bottles of beer")
        print ("if one of those bottles should happen to fall")
        print (str(num_beers-1) + " bottles of beer of the wall\n")
        beers(num_beers-1)


beers(99)

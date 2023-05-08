def CodontoAA(n1,n2,n3):
        if n1 =='A':
            if n2 =='U' :
                if n3 =='G':
                    print("M", end='')
                else :
                    print("I", end='')   
            elif n2 =='C' :
                print("T", end='')
            elif n2 == 'A' :
                if n3 =='U' or n3 =='C':
                    print("N", end='')
                else:
                    print("K", end='')
            else :
                if n3 =='U' or n3 =='C':
                    print("S", end='')
                else:
                    print ("R", end='')
        elif n1 == 'U' :
                if n2 == 'U':
                        if n3 =='U' or n3 =='C':
                                print("F", end='')
                        else :
                                print("L", end='')
                elif n2 == 'C' :
                        print("S", end='')
                elif n2 == 'A':
                        if n3 =='U' or n3 =='C':
                                print("Y", end='')
                        else :
                                print("", end='')
                else:
                        if n3 =='U' or n3 =='C':
                                print("C", end='')
                        elif n3 == 'A':
                                print("", end='')
                        else:
                                print("W", end='')
        elif n1 == 'C':
                if n2 == 'U':
                        print("L", end='')
                elif n2 == 'C':
                        print("P", end='')
                elif n2 == 'A':
                        if n3 =='U' or n3 =='C':
                                print("H", end='')
                        else:
                                print("Q", end='')
                else:
                        print("R", end='')
        elif n1 == 'G':
                if n2 == 'U':
                        print("V", end='')
                elif n2 == 'C':
                        print("A", end='') 
                elif n2 == 'A':
                        if n3 =='U' or n3 =='C':
                                print("N", end='')
                        else:
                                print("Q", end='')
                else:
                        print("G", end='')
        else :
            print("Erreur", end='')

# code génétique http://www.trikapalanet-fr.com/wp-content/uploads/2009/10/03_code_genetique_xl.jpg

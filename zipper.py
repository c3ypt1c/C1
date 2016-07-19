#Zipper 0.0.1

def inputi(*whatsay):
    while True:
        try:
            return input ( whatsay[0] )
            break
        except IndexError:
            whatsay = ( "> ", )
        except KeyboardInterrupt:
            pass
##            return None
##            break
        except:
            print ( Exception )  

def yn(*whatsay):
    while True:
        try:
            s = input ( whatsay[0] )
            if len ( s ) == 0: return None
            else:
                if s[0].lower() == "y": return True
                elif s[0].lower() == "n": return False
                else: return None
            break
        except IndexError:
            whatsay = ( "Y/N> ", )
        except KeyboardInterrupt:
            #return None
            print ()
            #break
        except:
            print ( Exception )  

loop = True

while loop:
    filenames = [None, None]
    print ( "Press enter every time you submit a file." )
    print ( "Enter an empty value to end the sumitting" )
    while True:
        try:
            fn = inputi("File Loc.> ")
            p = False
            for x in filenames:
                p = fn == x or p
            if not p:    
                file = open ( fn )
                file.close()
                filenames.append( fn )
            else:
                print ( "File has already been added" )
        except:
            if fn == "": break
            else: print ( "File not found" )
    
    filenames = filenames[2:]

    lengh = []
    data = []
    
    for x in filenames:
        try:
            file = open ( x, "rb" )
            try:
                dat = file.read()
                data.append ( dat )
                lengh.append( len ( dat ) )
                
            except:
                print ( "there was an error reading the file" )
                filenames.remove(x)
            
        except:
            print ( "there was an error oppening file:", x )
            filenames.remove(x)

        try: file.close()
        except: pass
        
    lenghst = str ( filenames )
    for x in lengh: lenghst += " " + str ( x )
    lenghst = str ( str ( len ( lenghst ) - 1 ) + str ( lenghst )  ).encode("UTF-8")
    
    print ( lenghst )

    for x in data: lenghst += x
    
    while True:
        while True:
            print ( "What would you like to name the file?" )
            name = inputi()
            if name != "":
                break
            
        ext = True
        try:
            if len ( name.split(".") ) > 1:
                ext = not yn("Would you like to use your own extention? Y/N> ")
        except: pass
        
        try: file.close()
        except: pass #Better safe than sorry

        if ext: ext = ".c1"
        else: ext = ""

        filename = str ( name ) + ext
        
        try:    
            file = open ( filename, "wb+" )
            try:
                file.write(lenghst)
                print ( "Success!" )
                break
            except:
                print ( "Failed to write to file" )
        except:
            print ( "Failed to open file." )

    try: file.close()
    except: pass #Better safe than sorry

    loop = None
    while loop == None:
        loop = yn("Would you like to loop this program? Y/N> ")
        
quit()
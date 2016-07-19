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

def delv(string, bannedChars):
    string = list ( string )
    for x in string:
        for y in bannedChars:
            if str(y) == str(x):
                try:
                    string.remove(str(y))
                except: print ( Exception )
    cont = string[:]
    string = ""
    for x in cont:
        string += x
    return string
    
            
#def datav( data ):

print (
"""Make sure that when you run this,
you run this in an empty folder as it
will overwrite any file with the same name!""", flush=True )

while True:
    try:
        path = inputi("Path of the .c3y or zipped file> ")
        a = open ( path )
        a.close()
        break
    except:
        print ( "Could not open file" )
        pass


a = open ( path, "rb" )
data = a.read()
a.close()

t = 0
dl = len ( data )
headerl = []
comp = False
try:
    for x in range(1,dl,1):
        y = data[x-1:x]
        try:
            headerl.append(int(y.decode("UTF-8")))
        except:
            try:
                comp = y.decode("UTF-8") == "["
            except:
                pass
            break
except:
    print ( "End" )
if comp:
    print ( "Header lengh extracted successfully...")
else:
    print ( "Header lengh extraction failed... Trying back up algorythm..." )
    ###Insert algorythm here
    
header = ""
for x in headerl:
    header += str ( x )

#del headerl

header = int ( header ) + len ( str ( header ) )
head = data[len( str ( header ) ):header + 1]

try:
    head = head.decode("UTF-8")
    pass
except:
    print ( Exception )
head2 = head.split(",")
head3 = ""
for x in head2:
    head3 += delv(x,[#"'",
                    "[",
                    "]"])
##del head2
head3 = head3.split("'")
for x in head3:
    if x == str ( " " ): head3.remove( x )
    if x == str ( "" ): head3.remove( x )
    

numbs = head3[len(head3)-1][1:].split(" ")
ttls = head3[:len(head3)-1]
if len ( ttls ) != len ( numbs ):
    raise UnicodeEncodeError

comb = []
for x in range(0,len(ttls)):
    comb.append([ttls[x],numbs[x]])
curbit = 1
curbit += header
for x in comb:
    x.append(data[curbit:int(x[1])+curbit])
    curbit += int ( x[1] )
##    if int ( x[1] ) == len ( x[2] ):
##        print ( x[0], "Pass! :D" )
##        x.append(True)
##    else:
##        print ( "Fail D: " )
##        x.append(False)

tick = 1
for x in comb:
    print ( tick, x[0] )
    tick += 1

unzip = None
while unzip == None:
    unzip = yn( "Unzip all?> " )

if unzip:
    for x in comb:
        file = open ( x[0], "wb" )
        file.write( x[2] )
        ##print ( Exception )
        file.close()
            
            
quit()
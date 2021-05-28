import pymysql
import cgi

form = cgi.FieldStorage()
searchType = form.getvalue('search_type')
searchArtistName = form.getvalue('search_artist_name')
searchImageLocation = form.getvalue('search_image_location')
searchArtistCountry = form.getvalue('search_artist_country')
searchArtistBirthYear = form.getvalue('search_artist_birth_year')
searchCreationStartYear = form.getvalue('search_creation_start_year')
searchCreationEndYear = form.getvalue('search_creation_end_year')
db = pymysql.connect(host='localhost',user='root',passwd='kusogaki69',db='gallery')
cur = db.cursor()

print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
print()
print('<a href = "mp3_homepage.py"> Display All Galleries </a>')
print("<title> Search Functions</title>")
print("<h1>Search Results</h1>")
print("<p> Search stuff here </p>")

#CANCERRRRRRRRRRRRRRRRRRRRR Type Searching
if searchType is not None:
    image_search_str = ''
    image_search = "SELECT * FROM image where "

    list_image_ids = []
    sql = "SELECT image_id FROM detail where type = '" + str(searchType) + "'"
    numImgId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_image_ids.append(row[0])
        numImgId += 1
    for x in range(0,int((numImgId)/2+1)):  #numImg = 3  1 2
        if x == 0 and x == int(numImgId/2):
            image_search_str = "image_id = " + str(list_image_ids[2*x])
        elif 2*(x+1) > numImgId:
            break
        else:
            image_search_str = "image_id = " + image_search_str + str(list_image_ids[2*x]) + " OR image_id = " + str(list_image_ids[2*x+1])

    image_search = image_search + image_search_str
    #print(image_search)
    cur.execute(image_search)
    for row in cur.fetchall():
        #print("<p id = 'numberOfImages'> Yes </p>")
        print('<div class = "row">')
        print('<div class = "column">')
        print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = "300" width = "300">')
        print('<form method ="get">')
        print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
        print('</form>')
        print('<p> Image ID: ' + str(row[0]))
        print('</div>')
        print('</div>')

#Not as cancer Search by Artist Name
if searchArtistName is not None:
    artist_search_str = ''
    artist_search = "SELECT * FROM image where "

    list_artist_ids = []
    sql = "SELECT artist_id FROM artist where name = '" + str(searchArtistName) + "'"
    numArtistId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_artist_ids.append(row[0])
        numArtistId += 1
    for x in range(0,int((numArtistId)/2+1)):  #numImg = 3  1 2
        if x == 0 and x == int(numArtistId/2):
            artist_search_str = "artist_id = " + str(list_artist_ids[2*x])
        elif 2*(x+1) > numArtistId:
            break
        else:
            artist_search_str = "artist_id = " + artist_search_str + str(list_artist_ids[2*x]) + " OR artist_id = " + str(list_artist_ids[2*x+1])
    artist_search = artist_search + artist_search_str
    print(artist_search)
    cur.execute(artist_search)
    for row in cur.fetchall():
        #print("<p id = 'numberOfImages'> Yes </p>")
        print('<div class = "row">')
        print('<div class = "column">')
        print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = "300" width = "300">')
        print('<form method ="get">')
        print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
        print('</form>')
        print('<p> Image ID: ' + str(row[0]))
        print('</div>')
        print('</div>')

#COUNTRY SEARCH
if searchArtistCountry is not None:
    sql = "SELECT * FROM artist where country = '" + str(searchArtistCountry) + "'"
    cur.execute(sql)
    for row in cur.fetchall():
        print('<p> Artist ID: ' + str(row[0]) + '</p>')
        print('<p> Artist Name: ' + str(row[1]) + '</p>')
        print('<p> Artist Birth Year: ' + str(row[2]) + '</p>')
        print('<p> Artist Country: ' + str(row[3]) + '</p>')
        print('<p> Artist Description: ' + str(row[4]) + '</p>')

#Not as cancer Search by Artist Name
if searchImageLocation is not None:
    image_search_str = ''
    image_search = "SELECT * FROM image where "
    list_image_ids = []
    sql = "SELECT image_id FROM detail where location = '" + str(searchImageLocation) + "'"
    numImgId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_image_ids.append(row[0])
        numImgId += 1
    for x in range(0,int((numImgId+1)/2)):
        #If odd
        if numImgId%2 == 1:
            if x == int(numImgId/2) and x == 0:
                image_search_str = image_search_str + "image_id = " + str(list_image_ids[2*x])
            elif x == int(numImgId/2) and x != 0:
                image_search_str = image_search_str + " OR image_id = " + str(list_image_ids[2*x])
            else:
                image_search_str = image_search_str + "image_id = " + str(list_image_ids[2*x]) + " OR image_id = " + str(list_image_ids[2*x+1])
        else:
            image_search_str = image_search_str + "image_id = " + str(list_image_ids[2*x]) + " OR image_id = " + str(list_image_ids[2*x+1])

    image_search = image_search + image_search_str
    print(image_search)
    cur.execute(image_search)
    for row in cur.fetchall():
        #print("<p id = 'numberOfImages'> Yes </p>")
        print('<div class = "row">')
        print('<div class = "column">')
        print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = "300" width = "300">')
        print('<form method ="get">')
        print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
        print('</form>')
        print('<p> Image ID: ' + str(row[0]))
        print('</div>')
        print('</div>')

#SEARCH ARTIST BIRTH YEAR
if searchArtistBirthYear is not None:
    artist_search_str = ''
    artist_search = "SELECT * FROM artist where artist_id = "
    list_artist_ids = []
    sql = "SELECT artist_id FROM artist where birth_year = '" + str(searchArtistBirthYear) + "'"
    numArtistId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_artist_ids.append(row[0])
        numArtistId += 1
    for x in range(0,int((numArtistId)/2+1)):  #numImg = 3  1 2
        if x == 0 and x == int(numArtistId/2):
            artist_search_str = "artist_id = " + str(list_artist_ids[2*x])
        elif 2*(x+1) > numArtistId:
            break
        else:
            artist_search_str = "artist_id = " + artist_search_str + str(list_artist_ids[2*x]) + " OR artist_id = " + str(list_artist_ids[2*x+1])
    artist_search = artist_search + artist_search_str
    print(artist_search)
    cur.execute(artist_search)
    for row in cur.fetchall():
        print('<p> Artist ID: ' + str(row[0]) + '</p>')
        print('<p> Artist Name: ' + str(row[1]) + '</p>')
        print('<p> Artist Birth Year: ' + str(row[2]) + '</p>')
        print('<p> Artist Country: ' + str(row[3]) + '</p>')
        print('<p> Artist Description: ' + str(row[4]) + '</p>')

if searchArtistName is not None:
    artist_search_str = ''
    artist_search = "SELECT * FROM image where artist_id = "

    list_artist_ids = []
    sql = "SELECT artist_id FROM artist where name = '" + str(searchArtistName) + "'"
    numArtistId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_artist_ids.append(row[0])
        numArtistId += 1
    # print('Num artist: ')
    # print(numArtistId)
    for x in range(0,int((numArtistId)/2+1)):
        #If odd
        if numArtistId%2 == 1:
            if x == int(numArtistId/2) and x == 0:  #Edge case where numArtist = 1
                artist_search_str = str(list_artist_ids[2*x])
            elif x == int(numArtistId/2) and x!= 0:
                artist_search_str = artist_search_str + " OR artist_id = " + str(list_artist_ids[2*x])
            else:
                artist_search_str = artist_search_str + "artist_id = " + str(list_artist_ids[2*x]) + " OR artist_id = " + str(list_artist_ids[2*x+1])
        else:
            image_search_str = artist_search_str + "artist_id = " + str(list_artist_ids[2*x]) + " OR artist_id = " + str(list_artist_ids[2*x+1])
    artist_search = artist_search + artist_search_str
    print(artist_search)
    cur.execute(artist_search)
    for row in cur.fetchall():
        #print("<p id = 'numberOfImages'> Yes </p>")
        print('<div class = "row">')
        print('<div class = "column">')
        print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = "300" width = "300">')
        print('<form method ="get">')
        print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
        print('</form>')
        print('<p> Image ID: ' + str(row[0]))
        print('</div>')
        print('</div>')

if searchCreationStartYear is not None and searchCreationEndYear is not None:
    image_search_str = ''
    image_search = "SELECT * FROM image where "
    list_image_ids = []
    #sql = "SELECT image_id FROM detail where year > '" + str(searchCreationStartYear) + "'" + str(searchCreationStartYear) + "'"
    sql = "SELECT image_id FROM detail where year > '" + str(searchCreationStartYear) + "' AND year <'" + str(searchCreationEndYear) + "'"
    numImgId = 0
    cur.execute(sql)
    for row in cur.fetchall():  #Get all image_ids
        list_image_ids.append(row[0])
        numImgId += 1
    for x in range(0,int((numImgId)/2+1)):  #numImg = 3  1 2
        if x == 0 and x == int(numImgId/2):
            #print('executed1')
            image_search_str = "image_id = " + str(list_image_ids[2*x])
            #print(image_search_str)
        elif 2*(x+1) > numImgId:
            #print('executed2')
            break
        else:
            #print('executed3')
            image_search_str = "image_id = " + image_search_str + str(list_image_ids[2*x]) + " OR image_id = " + str(list_image_ids[2*x+1])
            #print(image_search_str)
    image_search = image_search + image_search_str
    #print(image_search)
    cur.execute(image_search)
    for row in cur.fetchall():
        #print("<p id = 'numberOfImages'> Yes </p>")
        print('<div class = "row">')
        print('<div class = "column">')
        print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = "300" width = "300">')
        print('<form method ="get">')
        print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
        print('</form>')
        print('<p> Image ID: ' + str(row[0]))
        print('</div>')
        print('</div>')


for x in range(1):
    print("<h1> Search Images via Type </h1>")
print("<form method='post' action='#'>")
print("<p> Image type: <input type= 'text' id = 'searchGalleryID' name = 'search_type'/></p>")
print('<input type="submit" value="Search Type"/>')
print('</form>')

print("<h1> Search Images via Year Range </h1> </p>")
print("<form method='post' action='#'>")
print("<p> From: <input type= 'text' id = 'newGalleryID' name = 'search_creation_start_year'/></p>")
print("<p> To: <input type= 'text' id = 'newGalleryName' name = 'search_creation_end_year'/></p>")
print('<input type="submit" value="Search Images"/>')
print('</form>')

print("<h1> Search Images via Artist Name </h1> </p>")
print("<form method='post' action='#'>")
print("<p> Artist Name: <input type= 'text' id = 'searchGalleryID' name = 'search_artist_name'/></p>")
print('<input type="submit" value="Access Gallery"/>')
print('</form><br>')

print("<h1> Search Images via Location </h1> </p>")
print("<form method='post' action='#'>")
print("<p> Artist Name: <input type= 'text' id = 'searchGalleryID' name = 'search_image_location'/></p>")
print('<input type="submit" value="Search Location"/>')
print('</form><br>')


print("<h1> Search Artists via Country </h1> </p>")
print("<form method='post' action='#'>")
print("<p> Artist Name: <input type= 'text' id = 'searchGalleryID' name = 'search_artist_country'/></p>")
print('<input type="submit" value="Search Artist"/>')
print('</form><br>')

print("<h1> Search Artists by Birth Year </h1> </p>")
print("<form method='post' action='#'>")
print("<p> Artist Birth Year: <input type= 'text' id = 'searchGalleryID' name = 'search_artist_birth_year'/></p>")
print('<input type="submit" value="Search Artist"/>')
print('</form><br>')

print("</body>")
print("</html>")

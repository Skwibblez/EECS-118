import cgi
import pymysql
import sys, os ,io

#take in form details for new galleries here
form = cgi.FieldStorage()
gallery_id = form.getvalue('search_gallery_id')
image_id = form.getvalue('add_image_id')
#For adding to #DB
addImageID = form.getvalue('add_image_id')
addImageTitle = form.getvalue('add_image_title')
addImageLink = form.getvalue('add_image_link')
addArtistID = form.getvalue('add_artist_id')
addGalleryID = form.getvalue('add_gallery_id')
addDetailID = form.getvalue('add_detail_id')
addImageYear = form.getvalue('add_image_year')
addImageType = form.getvalue('add_image_type')
addImageWidth = form.getvalue('add_image_width')
addImageHeight = form.getvalue('add_image_height')
addImageLocation = form.getvalue('add_image_location')
addImageDescription = form.getvalue('add_image_description')

addArtistID = form.getvalue('add_artist_id')
addArtistName = form.getvalue('add_artist_name')
addArtistBirthYear = form.getvalue('add_artist_birth_year')
addArtistCountry = form.getvalue('add_artist_country')
addArtistDescription = form.getvalue('add_artist_description')

deleteImageID = form.getvalue('delete_image_id')

db = pymysql.connect(host='localhost',user='root',passwd='kusogaki69',db='gallery')
cur = db.cursor()

print("Content-Type: text/html\n\n")
print("<TITLE> Gallery </TITLE>")

print("<h1> Images in Gallery </h1>")
print("<h2> Images Below </h2>")
print("<html>")
print("<body>")
print('<a href = "mp3_search.py"> Search </a><br><br>')
print('<a href = "mp3_homepage.py"> Home Page (Display All Galleries) </a>')
print('<div class = "row">')
print('<div class = "column">')
print('</div>')
print('</div>')

if deleteImageID is not None:
    sql = "DELETE FROM detail WHERE image_id = " + str(deleteImageID)
    cur.execute(sql)
    sql = "DELETE FROM image WHERE image_id = " + str(deleteImageID)
    cur.execute(sql)
    db.commit()

if addArtistID is not None and addArtistName is not None and addArtistBirthYear is not None and addArtistCountry is not None and addArtistDescription is not None :  #Appropriate comparison
    # a = a + "Gallery Name: " + newGalleryName + "\nGallery ID: " + newGalleryID + "\nGallery Description: " + newGalleryDescription #OK #For display on html page
    sql = ("""INSERT INTO artist(artist_id, name, birth_year, country, description) VALUES(%s, %s, %s, %s, %s)""") #Add into database
    cur.execute(sql, (addArtistID, addArtistName, addArtistBirthYear, addArtistCountry, addArtistDescription))
    db.commit()
    print("Artist ADDING COMPLETE")

if addImageID is not None and addImageTitle is not None and addImageLink is not None and addArtistID is not None and addGalleryID is not None and addDetailID is not None and addImageYear is not None and addImageType is not None and addImageWidth is not None and addImageHeight is not None and addImageLocation is not None and addImageDescription is not None:  #Appropriate comparison
    # a = a + "Gallery Name: " + newGalleryName + "\nGallery ID: " + newGalleryID + "\nGallery Description: " + newGalleryDescription #OK #For display on html page
    sql = ("""INSERT INTO image(image_id, title, link, gallery_id, artist_id, detail_id) VALUES(%s, %s, %s, %s, %s, %s)""") #Add into database
    cur.execute(sql, (addImageID, addImageTitle, addImageLink, addGalleryID, addArtistID, addDetailID))
    db.commit()

    sql = ("""INSERT INTO detail(detail_id, image_id, year, type, width, height, location, description) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""") #Add into database
    cur.execute(sql, (addDetailID, addImageID, addImageYear, addImageType, addImageWidth, addImageHeight, addImageLocation, addImageDescription))
    db.commit()
    print("IMAGE ADDING COMPLETE")

myQuerySelf = os.environ.get('QUERY_STRING')
query_string_arr = myQuerySelf.split("=")
srch_gal_id = query_string_arr[1]
how_search = query_string_arr[0]


#Check condition later
image_search_str = ''
image_search = "SELECT * FROM detail where "
list_image_ids = []
sql = "SELECT image_id FROM image where gallery_id = '" + str(srch_gal_id) + "'"
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
width_arr = []
height_arr = []
cur.execute(image_search)
for row in cur.fetchall():
    width_arr.append(row[4])
    height_arr.append(row[5])

#Display images
sql = "SELECT * FROM image WHERE gallery_id = " + str(srch_gal_id)
cur.execute(sql)
numImg = 0
counter = 0
for row in cur.fetchall():
    #print("<p id = 'numberOfImages'> Yes </p>")
    print('<div class = "row">')
    print('<div class = "column">')
    print('<p>')
    print('<a href = "' + str(row[2]) + '">' )
    print('<img src="' + str(row[2]) + '"id ="img_link"' + str(row[0]) + '" height = ' + str(height_arr[counter]) + " width = " + str(width_arr[counter]) + '>')
    print('</a>')
    print('</p>')
    print('<form method ="get">')
    print('<a href = "mp3_details.py' + '?description_id=' + str(row[5]) +'&image_id='+ str(row[0]) + '&artist_id='+ str(row[4]) + '">Title: ' + str(row[1]) + '</a>')
    print('</form>')
    print('<p> Image ID: ' + str(row[0]))
    print('</div>')
    print('</div>')
    counter += 1
    numImg += 1

print('<p> Number of Images in Gallery: ' + str(numImg) + '</p>')
print("<h1> Add a new image </h1>")
print("<form method='post' action='#'>")
print("<p>Image ID: <input type= 'text' id = 'addImageID' name = 'add_image_id'/></p>")
print("<p> Image Title: <input type= 'text' id='addImageTitle' name = 'add_image_title'/></p>")
print("<p> Image Link: <input type= 'url' id = 'addImageLink' name = 'add_image_link'/></p>")
print("<p> Artist ID: <input type= 'text' id = 'addArtistID' name = 'add_artist_id'/>")
print("<p> Gallery ID: <input type= 'text' id = 'addGalleryID' name = 'add_gallery_id'/></p>")
print("<p> Detail ID: <input type= 'text' id = 'addDetailID' name = 'add_detail_id'/></p>")
print("<p> Image Year: <input type= 'text' id = 'addImageYear' name = 'add_image_year'/></p>")
print("<p> Image Type: <input type= 'text' id = 'addImageType' name = 'add_image_type'/></p>")
print("<p> Image Width: <input type= 'text' id = 'addImageWidth' name = 'add_image_width'/></p>")
print("<p> Image Height: <input type= 'text' id = 'addImageHeight' name = 'add_image_height'/></p>")
print("<p> Image Location: <input type= 'text' id = 'addImageLocation' name = 'add_image_location'/></p>")
print("<p> Image Description: <input type= 'text' id = 'addImageDescription' name = 'add_image_description'/></p>")
print('<input type="submit" value="Add Image"/>')
print('</form>')

print("<h1> Add a new artist </h1>")
#print("<form method='post' action='mp3_images.py'>")
print("<form method='post' action='#'>")
print("<p> Artist ID: <input type= 'text' id = 'addArtistID' name = 'add_artist_id'/></p>")
print("<p> Artist Name: <input type= 'text' id='addArtistName' name = 'add_artist_name'/></p>")
print("<p> Artist Birth Year: <input type= 'text' id = 'addArtistBirthYear' name = 'add_artist_birth_year'/></p>")
print("<p> Artist Country: <input type= 'text' id = 'addArtistCountry' name = 'add_artist_country'/></p>")
print("<p> Artist Description: <input type= 'text' id = 'addArtistDescription' name = 'add_artist_description'/></p>")
print('<input type="submit" value="Add Artist"/>')
print('</form>')

print("<h1> Delete Image </h1>")
print("<form method='post' action='#'>")
print("<p> Image ID: <input type= 'text' id = 'deleteImageID' name = 'delete_image_id'/></p>")
print('<input type="submit" value="Delete Image"/>')
print('</form>')

print("</body>")
print("</html>")

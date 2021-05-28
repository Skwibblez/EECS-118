import cgi
import pymysql
import sys, os ,io
import datetime
form = cgi.FieldStorage()

newGalleryID = form.getvalue('new_gallery_id')
newGalleryName = form.getvalue('new_gallery_name')
newGalleryDescription = form.getvalue('new_gallery_description')

modifyGalleryID = form.getvalue('modify_gallery_id')
modifyGalleryName = form.getvalue('modify_gallery_name')
modifyDescription = form.getvalue('modify_description_1')

db = pymysql.connect(host='localhost',user='root',passwd='kusogaki69',db='gallery')
cur = db.cursor()

print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
#Greeting
now = datetime.datetime.now()
if now.hour >= 6 and now.hour <= 12:
    print("<h1> Good Morning </h1>")
elif now.hour >12 and now.hour <=17:
    print("<h1> Good Afternoon </h1>")
elif now.hour > 17 and now.hour <= 20:
    print("<h1> Good Evening </h1>")
elif now.hour > 20 or now.hour <24:
    print("<h1> Good Night </h1>")
print('<a href = "mp3_search.py"> Search </a>')
a = ''
sql = "SELECT name from gallery"
if newGalleryID is not None and newGalleryName is not None and newGalleryDescription is not None:  #Appropriate comparison
    a = a + "Gallery Name: " + newGalleryName + "\nGallery ID: " + newGalleryID + "\nGallery Description: " + newGalleryDescription #OK #For display on html page
    sql = ("""INSERT INTO gallery(gallery_id, name, description) VALUES(%s, %s, %s)""") #Add into database
    cur.execute(sql, (newGalleryID, newGalleryName, newGalleryDescription))
    db.commit()

if modifyGalleryID is not None and modifyGalleryName is not None and modifyDescription is not None:
    sql = "UPDATE gallery set name = '" + str(modifyGalleryName) + "', description = '" + str(modifyDescription) + "' WHERE gallery_id = " + str(modifyGalleryID)
    cur.execute(sql)
    db.commit()

print("<title>MP3 Home</title>")
print("<h1>Galleries</h1>")

sql = "SELECT * from gallery"
numGalleries = 0
cur.execute(sql)
for row in cur.fetchall():
    print('<div class = "row">')
    print('<div class = "column">')
    print('Gallery ID: ' + str(row[0]))
    print('Gallery Name: ' + str(row[1]))
    print('Gallery Description: ' + str(row[2]))
    print('</div>')
    print('</div>')
    numGalleries+=1

print("<h1> Add new gallery </h1></p>")
print("<form method='post' action='mp3_homepage.py'>")
print("<p>Gallery ID: <input type= 'text' id = 'newGalleryID' name = 'new_gallery_id'/></p>")
print("<p>Gallery Name: <input type= 'text' id = 'newGalleryName' name = 'new_gallery_name'/></p>")
print("<p>Gallery Description: <input type= 'text' id = 'newGalleryDescription' name = 'new_gallery_description'/></p>")
print('<input type="submit"/>')
print('</form>')

print("<h1> Modify Gallery Detail </h1>")
print("<form method='post' action='mp3_homepage.py'>")
print("<p> Gallery ID: <input type= 'text' id = 'modifyGalleryID' name = 'modify_gallery_id'/></p>")
print("<p> New Gallery Name: <input type= 'text' id='modifyGalleryName' name = 'modify_gallery_name'/></p>")
print("<p> New Description: <input type= 'text' id = 'modifyDescription' name = 'modify_description_1'/></p>")
print('<input type="submit" value="Modify Details"/>')
print('</form>')

#Change Location to artist page
print("<h1> Search via gallery id</h1> </p>")
print("<form method='get' action='mp3_images.py'>")
#print("<form method='get' action='mp3_artist.py'>")
print("<p>Input Gallery ID:<input type= 'text' id = 'searchGalleryID' name = 'search_gallery_id'/> <br>")
#print('<input type="hidden" name = "searched_gal_id" value="'+ str(form.getvalue('search_gallery_id')) + '"/>')
print('<input type="submit" value="Access Gallery"/>')
print('</form><br>')

print("</body>")
print("</html>")

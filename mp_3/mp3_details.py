import cgi
import pymysql
import sys, os ,io

form = cgi.FieldStorage()

modifyImageID = form.getvalue('modify_image_id')
modifyNewYear = form.getvalue('modify_new_year')
modifyNewType = form.getvalue('modify_new_type')
modifyNewWidth = form.getvalue('modify_new_width')
modifyNewHeight = form.getvalue('modify_new_height')
modifyNewLocation = form.getvalue('modify_new_location')
modifyNewDescription = form.getvalue('modify_new_description')

db = pymysql.connect(host='localhost',user='root',passwd='kusogaki69',db='gallery')

myQuerySelf = os.environ.get('QUERY_STRING')
# if len(myQuerySelf) != 0:
#     test_string_arr = myQuerySelf.split("=")
#     if test_string_arr[0] == "description_id": #From previous page
query_string_arr = myQuerySelf.split("&")
det_arr = query_string_arr[0]
img_arr = query_string_arr[1]
art_arr = query_string_arr[2]

det_id_split = det_arr.split("=")
img_id_split = img_arr.split("=")
art_id_split = img_arr.split("=")

det_id = det_id_split[1]
img_id = img_id_split[1]
art_id = art_id_split[1]

print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
print("<TITLE>Gallery Details</TITLE>")
print("<h1> Details Page (Include artist clickable link) </h1>")
print('<a href = "mp3_search.py"> Search </a><br><br>')
print('<a href = "mp3_homepage.py"> Display All Galleries </a>')
cur = db.cursor()
#Artist table
sql = "SELECT name from artist WHERE artist_id = " + str(art_id)
print(sql)
cur.execute(sql)
for row in cur.fetchall():
    #print('Description: ' + str(row[7]))
    print('<p> Artist Name: ' + str(row[0]) + '</p>')

#Image table
sql = "SELECT link from image where image_id = " + str(img_id)
cur.execute(sql)
for row in cur.fetchall():
    print('<img src="' + str(row[0]) +  '" height = "300" width = "300">')

#Detail table
sql = "SELECT * from detail WHERE detail_id =" + str(det_id) + " AND image_id = " + str(img_id)
cur.execute(sql)
for row in cur.fetchall():
    #print('Description: ' + str(row[7]))
    print('<p id = "detJS"> Detail id: ' + str(row[0]))
    print('<p id = "imgJS"> Image id: ' + str(row[1]))
    print('<p id = "yearJS"> Year: ' + str(row[2]))
    print('<p id = "typeJS"> Type: ' + str(row[3]))
    print('<p id = "widthJS"> Width: ' + str(row[4]))
    print('<p id = "heightJS"> Height: ' + str(row[5]))
    print('<p id = "locationJS"> Location: ' + str(row[6]))
    print('<p id = "descriptionJS"> Description: ' + str(row[7]))

#Modify
if modifyNewDescription is not None and modifyNewType is not None and modifyNewHeight is not None and modifyNewYear is not None and modifyNewWidth is not None and modifyImageID is not None and modifyNewLocation is not None:
    sql = "UPDATE detail set year = '" + str(modifyNewYear) + "', type = '" + str(modifyNewType) + "', width = '" + str(modifyNewWidth)+ "', height = '" + str(modifyNewHeight)+ "', location = '" + str(modifyNewLocation)+ "', description = '" + str(modifyNewDescription) + "' WHERE image_id = " + str(modifyImageID)
    cur.execute(sql)
    db.commit()

print('<form method ="get">')
print('<a href = "mp3_artist.py' + '?artist_id=' + str(art_id) + '">Artist Details </a>')
print('</form>')

print("<h1> Modify Image Details (Refresh page to see change) </h1>")
print("<form method='post' action='#'>")
print("<p> Image ID: <input type= 'text' id = 'modifyGalleryID' name = 'modify_image_id'/></p>")
print("<p> New year: <input type= 'text' id = 'modifyDescription' name = 'modify_new_year'/></p>")
print("<p> New type: <input type= 'text' id = 'modifyDescription' name = 'modify_new_type'/></p>")
print("<p> New width: <input type= 'text' id = 'modifyDescription' name = 'modify_new_width'/></p>")
print("<p> New height: <input type= 'text' id = 'modifyDescription' name = 'modify_new_height'/></p>")
print("<p> New location: <input type= 'text' id = 'modifyDescription' name = 'modify_new_location'/></p>")
print("<p> New description: <input type= 'text' id = 'modifyDescription' name = 'modify_new_description'/></p>")
print('<input type="submit" value="Modify Details" onclick = "UpdateDetails()"/>')
print('</form>')

print('<script type = "text/javascript">')
print('function UpdateDetails()')
print('{')
print('document.getElementById("yearJS").innerHTML = wtf;')
print('}')
print('</script>')


print("</body>")
print("</html>")

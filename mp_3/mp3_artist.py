import cgi
import pymysql
import sys, os ,io

db = pymysql.connect(host='localhost',user='root',passwd='kusogaki69',db='gallery')

form = cgi.FieldStorage()

modifyArtistID = form.getvalue('modify_artist_id')
modifyArtistName = form.getvalue('modify_artist_name')
modifyArtistBirthYear = form.getvalue('modify_artist_birth_year')
modifyArtistCountry = form.getvalue('modify_artist_country')
modifyArtistDescription = form.getvalue('modify_artist_description')

print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
print("<TITLE>Artist Details</TITLE>")
print("<h1> Artist Page (Refresh Page to see Updates) </h1>")

cur = db.cursor()

myQuerySelf = os.environ.get('QUERY_STRING')
if len(myQuerySelf) != 0:
    query_string_arr = myQuerySelf.split("=")
    art_id = query_string_arr[1]

#Artist table
    sql = "SELECT * from artist WHERE artist_id = " + str(art_id)
    cur.execute(sql)
    for row in cur.fetchall():
        print('<p> Artist ID: ' + str(row[0]) + '</p>')
        print('<p> Artist Name: ' + str(row[1]) + '</p>')
        print('<p> Artist Birth Year: ' + str(row[2]) + '</p>')
        print('<p> Artist Country: ' + str(row[3]) + '</p>')
        print('<p> Artist Description: ' + str(row[4]) + '</p>')

if modifyArtistID is not None and modifyArtistName is not None and modifyArtistBirthYear is not None and modifyArtistCountry is not None and modifyArtistDescription is not None:
    sql = "UPDATE artist set name = '" + str(modifyArtistName) + "', birth_year = '" + str(modifyArtistBirthYear) + "', country = '" + str(modifyArtistCountry)+ "', description = '" + str(modifyArtistDescription) + "' WHERE artist_id = " + str(modifyArtistID)
    cur.execute(sql)
    db.commit()

smth = 'hi'
print('<form method ="get">')
print('<a href = "mp3_homepage.py' + '?artist_id=' + str(smth) +'&description_id='+ str(smth) + '"> Home </a><br><br>')
print('<a href = "mp3_search.py' + '?artist_id=' + str(smth) +'&description_id='+ str(smth) + '"> Search </a><br><br>')
#print('<a href = "mp3_.py' + '?artist_id=' + str(smth) +'&description_id='+ str(smth) + '">Back </a>')
#print('<a href = "mp3_artist.py' + '?artist_id=' + str(smth) +'&description_id='+ str(smth) + '">Back </a>')
print('</form>')

print("<h1> Modify Artist Details </h1>")
#print("<form method='post' action='mp3_artist.py'>")
print("<form method='post' action='#'>")
print("<p> Artist ID: <input type= 'text' id = 'modifyGalleryID' name = 'modify_artist_id'/></p>")
print("<p> New Artist Name: <input type= 'text' id = 'modifyDescription' name = 'modify_artist_name'/></p>")
print("<p> New Artist Birth Year: <input type= 'text' id = 'modifyDescription' name = 'modify_artist_birth_year'/></p>")
print("<p> New Artist Country: <input type= 'text' id = 'modifyDescription' name = 'modify_artist_country'/></p>")
print("<p> New Artist Description: <input type= 'text' id = 'modifyDescription' name = 'modify_artist_description'/></p>")
print('<input type="submit" value="Modify Artist Details" onclick = ""/>')
print('</form>')

print('<script type = "text/javascript">')
print('</script>')

print("</body>")
print("</html>")

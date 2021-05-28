import cgi

print("Content-Type: text/html")
print("<html>")
print("<body>")
print()

print("<title>CGI script output</title>")
print("<h1>This is my first CGI script</h1>")


print("<form method='post' action='mp2.py'>")
print("<p>URL: <input type= 'url' id = 'URL1' name = 'url1'/><br>")
print("<p>Title: <input type= 'text' id='title1' name = 'title_1'/><br>")
print("<p>Year: <input type= 'text' id='year1' name = 'yr_1'/><br>")
print("<p>Artist: <input type= 'text' id = 'artist1' name = 'art_1'/><br>")
print("<p>Description: <input type= 'text' id = 'description1' name = 'desc_1'/><br>")

print("<p>URL2: <input type= 'url' id = 'URL2' name = 'url2'/><br>")
print("<p>Title2: <input type= 'text' id = 'title2' name = 'title_2'/><br>")
print("<p>Year2: <input type= 'text' id='year2' name = 'yr_2'/><br>")
print("<p>Artist2: <input type= 'text' id = 'artist2' name = 'art_2'/><br>")
print("<p>Description2: <input type= 'text' id = 'description2' name = 'desc_2'/><br>")
print('<input type="submit" value="Submit"/>') 


print("</body>")
print("</html>")




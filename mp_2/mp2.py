import cgi

form = cgi.FieldStorage()

first_url = form.getvalue('url1')
first_title = form.getvalue('title_1')
first_year = form.getvalue('yr_1')
first_artist = form.getvalue('art_1')
first_description = form.getvalue('desc_1')

second_url = form.getvalue('url2')
second_title = form.getvalue('title_2')
second_year = form.getvalue('yr_2')
second_artist = form.getvalue('art_2')
second_description = form.getvalue('desc_2')

print("Content-Type: text/html")

print()
print("<head>")
print("<title>CGI script output</title>")
print("</head>")
#Script
print('<script type = "text/javascript">')
print('function EnableImage1()')
print('{')
print('document.getElementById("details").innerHTML = " Title: %s Year: %s Artist: %s Description: %s";' % (first_title,first_year,first_artist,first_description))
print('document.getElementById("imagery1").src ="' + str(first_url) + '";')
print('}')

print('function EnableImage2()')
print('{')
print('document.getElementById("details").innerHTML = " Title: %s Year: %s Artist: %s Description: %s";' % (second_title,second_year,second_artist,second_description))
print('document.getElementById("imagery1").src ="' + str(second_url) +'";')
print('}')

print('</script>')
print("<body>")

print("<img src='"+ str(first_url)+"' id='imagery1' height='300' width='200'>")
#print("<img id='imagery2' height='300' width='200'>")

print("<form method='post' action='mp2.py'>")
print('<button type="button" onclick="EnableImage1()">Image 1</button>')
print('<button type="button" onclick="EnableImage2()">Image 2</button>')
print('</form>')

print("<p id='details'>Title: %s\nYear: %s\nArtist: %s\nDescription: %s </p>" % (first_title,first_year,first_artist,first_description))
#Display image


#Goal - try to extract url from other file
#print("<img src = 'https://m.media-amazon.com/images/M/MV5BYjQzYWViMTctNjEyYi00YzU2LTk5ZTAtM2M0YjA1Y2JjMGY1XkEyXkFqcGdeQXVyMzgxODM4NjM@._V1_UY268_CR3,0,182,268_AL_.jpg' id='imagery1' height='300' width='200'>")

print("</body>")


import os
import sqlite3 as sl
import markdown
import math
import urllib.parse

print("deleting old files...")
os.system("rm -r  docs/*")
print("copying new files...")
os.system("cp -r sources/* docs")

con = sl.connect("content.db", check_same_thread=False)



# Definitons ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# head ------------------------------------------------------
def buildHead(title, head):
    print("    head: {}".format(title))
    file.write('''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Xilef12000 | {}</title>
<meta charset="utf-8" name="description" content="Xilef12000 {}">
<link rel="icon" sizes="any" type="image/svg+xml" href="/assets/favicon_dark.svg" id="icon"/>
<link rel="stylesheet" href="/style-sheets/style.css">
<script src="/scripts/urlName.js" args="{}" type="text/javascript"></script>
    '''.format(title, title, urllib.parse.quote(title)))
    if head:
        file.write(open("content/head/{}".format(head), 'r').read())
    file.write('''
</head>
    ''')
# header ------------------------------------------------------
def buildHeader(header):
    print("    header: {}".format(header))
    file.write('''
<body>
<header>
    ''')
    if header:
        file.write(open("content/header/{}".format(header), 'r').read())
    file.write('''
</header>
    ''')
# footer ------------------------------------------------------
def buildFooter(footer):
    print("    footer: {}".format(footer))
    file.write('''
<footer>
    ''')
    if footer:
        file.write(open("content/footer/{}".format(footer), 'r').read())
    file.write('''
</footer>
</body>
</html>
    ''')


# Database ------------------------------------------------------------------------------------------------------------------------------------------------------------------
with con: # tags.db
    content = con.execute('SELECT * FROM "TAGS"')
os.system("touch docs/tags.db")
with open("docs/tags.db", "a") as file:
    for row in content:
        file.write(str(row).replace('(','').replace(')','').replace("'", '') + ';\n')
        print(str(row))
    file.write("null, null")
with con: # id.db
    content = con.execute('SELECT * FROM "ID"')
os.system("touch docs/id.db")
with open("docs/id.db", "a") as file:
    for row in content:
        file.write(str(row).replace('(','').replace(')','').replace("'", '') + ';\n')
        print(str(row))
    file.write("null, null, null")
# Projects ------------------------------------------------------------------------------------------------------------------------------------------------------------------
projects = []
with con:
    content = con.execute('SELECT * FROM "PROJECTS"')
for row in content:
    id = row[0]
    title = row[1]
    head = ""
    header = row[2]
    body = row[3]
    footer = row[4]
    if not os.path.isdir("docs/project/{}".format(id)):
        os.system("mkdir docs/project/{}".format(id))
    projects.insert(0,(id, title))
    print(" \nBuilding: project/{}".format(id))
    os.system("touch docs/project/{}".format(id))
    with open("docs/project/{}/index.html".format(id), "a") as file:
        buildHead(title, head)
        buildHeader(header)
        # body ------------------------------------------------------
        print("    body: {}".format(body))
        file.write('''
<div class="content-wrapper">
        ''')
        if body:
            if str(body).split('.')[-1] == "html":
                file.write(open("content/body/{}".format(body), 'r').read())
            elif str(body).split('.')[-1] == "md":
                file.write(markdown.markdown(open("content/body/{}".format(body), 'r').read()))
        file.write('''
</div>
        ''')
        buildFooter(footer)
# Gallery/ART ------------------------------------------------------
gallery = []
with con:
    content = con.execute('SELECT * FROM "ART"')
for row in content:
    id = row[0]
    title = row[1]
    source = row[2]
    type = row[3]
    gallery.insert(0,(id, title, source, type))
# SYSTEM ------------------------------------------------------------------------------------------------------------------------------------------------------------------
with con: #read DB
    content = con.execute('SELECT * FROM "SYSTEM"')
for row in content:
    id = row[0]
    title = row[1]
    head = row[2]
    header = row[3]
    body = row[4]
    footer = row[5]
    print(" \nBuilding: {}".format(id))
    os.system("touch docs/{}".format(id))
    with open("docs/{}".format(id), "a") as file:
        buildHead(title, head)
        buildHeader(header)
        # body ------------------------------------------------------
        if id == 'index.html': # index ------------------------------------------------------
            print("    body: {}".format(body))
            file.write('''
<div class="content-wrapper">
            ''')
            if body:
                if str(body).split('.')[-1] == "html":
                    file.write(open("content/body/{}".format(body), 'r').read())
                elif str(body).split('.')[-1] == "md":
                    file.write(markdown.markdown(open("content/body/{}".format(body), 'r').read()))
            file.write('''
        <br>
        <br>
        <h2>Projects:</h2>
        <table class="image_table">
            ''')
            projects_short = projects[0:2]
            print(projects_short)
            for i in range(math.ceil(len(projects_short)/2)):
                file.write('''
            <tr>
                <td>
                    <a class="aH" href="project/{}/">
                        <h3>{}</h3>
                        <img src="project/{}/thumbnail.png">
                    </a>
                </td>
                <td>
                    <a class="aH" href="project/{}/">
                        <h3>{}</h3>
                        <img src="project/{}/thumbnail.png">
                    </a>
                </td>
            </tr>
                '''.format(projects_short[(i+1)*2-2][0],projects_short[(i+1)*2-2][1],projects_short[(i+1)*2-2][0],projects_short[(i+1)*2-1][0],projects_short[(i+1)*2-1][1],projects_short[(i+1)*2-1][0]))
            file.write('''
        </table>
        <a href="projects">See More...</a>
        <br>
        <h2>Gallery:</h2>
        <table class="image_table">
            ''')
            gallery_short = gallery[0:2]
            print(gallery_short)
            for i in range(math.ceil(len(gallery_short)/2)):
                file.write('''
            <tr>
                <td>
                    <div tabindex="0"  class="image_table_div">
                        <h3>{}</h3>
                '''.format(gallery_short[(i+1)*2-2][1]))
                if gallery_short[(i+1)*2-2][3] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery_short[(i+1)*2-2][2]))
                elif gallery_short[(i+1)*2-2][3] == 'html':
                    file.write(open("content/body/{}".format(gallery_short[(i+1)*2-2][2]), 'r').read())

                file.write('''
                    </div>
               </td>
                <td>
                    <div tabindex="0"  class="image_table_div">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-1][1]))
                if gallery[(i+1)*2-1][3] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-1][2]))
                elif gallery[(i+1)*2-1][3] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-1][2]), 'r').read())

                file.write('''
                    </div>
                </td>
            </tr>
                ''')
            file.write('''
    </table>
    <a href="gallery">See More...</a>
</div>
            ''')
        elif id == 'gallery.html': # Gallery/ART ------------------------------------------------------
            print("    body: GALLERY")
            file.write('''
<div class="content-wrapper">
        <h2>Gallery</h2>
        <table class="image_table">
            ''')
            for i in range(math.ceil(len(gallery)/2)):
                file.write('''
            <tr>
                <td>
                    <div tabindex="0" class="image_table_div">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-2][1]))
                if gallery[(i+1)*2-2][3] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-2][2]))
                elif gallery[(i+1)*2-2][3] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-2][2]), 'r').read())
                elif gallery[(i+1)*2-2][3] == 'img+html':
                    file.write('''
                        <img src="art/{}">
                        {}
                    '''.format(gallery[(i+1)*2-2][0], open("content/body/{}".format(gallery[(i+1)*2-2][2]), 'r').read()))

                file.write('''
                    </div>
               </td>
                <td>
                    <div tabindex="0" class="image_table_div">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-1][1]))
                if gallery[(i+1)*2-1][3] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-1][2]))
                elif gallery[(i+1)*2-1][3] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-1][2]), 'r').read())
                elif gallery[(i+1)*2-1][3] == 'img+html':
                    file.write('''
                        <img src="art/{}">
                        {}
                    '''.format(gallery[(i+1)*2-1][0], open("content/body/{}".format(gallery[(i+1)*2-1][2]), 'r').read()))

                file.write('''
                    </div>
                </td>
            </tr>
                ''')
            #file.write(str(gallery))
            file.write('''
    </table>
</div>
            ''')
        elif id == 'projects.html': # Projects ------------------------------------------------------
            print("    body: PROJECTS")
            file.write('''
<div class="content-wrapper">
        <h2>Projects</h2>
        <table class="image_table">
            ''')
            for i in range(math.ceil(len(projects)/2)):
                file.write('''
            <tr>
                <td>
                    <a class="aH" href="project/{}/">
                        <h3>{}</h3>
                        <img src="project/{}/thumbnail.png">
                    </a>
                </td>
                <td>
                    <a class="aH" href="project/{}/">
                        <h3>{}</h3>
                        <img src="project/{}/thumbnail.png">
                    </a>
                </td>
            </tr>
                '''.format(projects[(i+1)*2-2][0],projects[(i+1)*2-2][1],projects[(i+1)*2-2][0],projects[(i+1)*2-1][0],projects[(i+1)*2-1][1],projects[(i+1)*2-1][0]))
            #file.write(str(projects))
            file.write('''
    </table>
</div>
            ''')
        else: # Pages ------------------------------------------------------
            print("    body: {}".format(body))
            file.write('''
<div class="content-wrapper">
            ''')
            if body:
                if str(body).split('.')[-1] == "html":
                    file.write(open("content/body/{}".format(body), 'r').read())
                elif str(body).split('.')[-1] == "md":
                    file.write(markdown.markdown(open("content/body/{}".format(body), 'r').read()))
            file.write('''
</div>
            ''')
        buildFooter(footer)
    
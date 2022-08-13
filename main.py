import os
import sqlite3 as sl
import markdown
import math

print("deleting old files...")
os.system("rm -r  docs/*")
print("copying new files...")
os.system("cp -r sources/* docs")

con = sl.connect("content.db", check_same_thread=False)

# Build Page ------------------------------------------------------
def build_page(data, id, path, table):
    #print(data)
    print("Building: {}".format(path + id))
    os.system("touch docs/{}".format(path + id))
    with open("docs/{}".format(path + id), "a") as file:
        # head ------------------------------------------------------
        print("    head: {}".format(data[2]), end="")
        file.write('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Xilef12000 | {}</title>
    <meta charset="utf-8" name="description" content="Xilef12000 {}">
    <link rel="icon" sizes="any" type="image/svg+xml" href="/assets/favicon_dark.svg" id="icon"/>
    <link rel="stylesheet" href="/style-sheets/style.css">
        '''.format(data[1], data[1]))
        if data[2]:
            file.write(open("content/head/{}".format(data[2]), 'r').read())
        file.write('''
</head>
        ''')
        # header ------------------------------------------------------
        print("    header: {}".format(data[3]), end="")
        file.write('''
<body>
    <header>
        ''')
        if data[3]:
            file.write(open("content/header/{}".format(data[3]), 'r').read())
        file.write('''
    </header>
        ''')
        # body ------------------------------------------------------
        if table == 'projects': # Projects ------------------------------------------------------
            print("    body: PROJECTS", end="")
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
        elif table == 'gallery': # Gallery/ART ------------------------------------------------------
            print("    body: GALLERY", end="")
            file.write('''
<div class="content-wrapper">
        <h2>Gallery</h2>
        <table class="image_table">
            ''')
            for i in range(math.ceil(len(gallery)/2)):
                file.write('''
            <tr>
                <td>
                    <div tabindex="0">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-2][1]))
                print(gallery[(i+1)*2-2][2])
                if gallery[(i+1)*2-2][2] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-2][0]))
                elif gallery[(i+1)*2-2][2] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-2][3]), 'r').read())

                file.write('''
                    </div>
               </td>
                <td>
                    <div tabindex="0">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-1][1]))
                print(gallery[(i+1)*2-1][2])
                if gallery[(i+1)*2-1][2] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-1][0]))
                elif gallery[(i+1)*2-1][2] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-1][3]), 'r').read())

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
        elif table == 'index': # Index ------------------------------------------------------
            print("    body: {}".format(data[4]), end="")
            file.write('''
<div class="content-wrapper">
            ''')
            if data[4]:
                if str(data[4]).split('.')[-1] == "html":
                    file.write(open("content/body/{}".format(data[4]), 'r').read())
                elif str(data[4]).split('.')[-1] == "md":
                    file.write(markdown.markdown(open("content/body/{}".format(data[4]), 'r').read()))
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
            gallery_short = gallery[0:1]
            for i in range(math.ceil(len(gallery_short)/2)):
                file.write('''
            <tr>
                <td>
                    <div tabindex="0">
                        <h3>{}</h3>
                '''.format(gallery_short[(i+1)*2-2][1]))
                print(gallery_short[(i+1)*2-2][2])
                if gallery_short[(i+1)*2-2][2] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery_short[(i+1)*2-2][0]))
                elif gallery_short[(i+1)*2-2][2] == 'html':
                    file.write(open("content/body/{}".format(gallery_short[(i+1)*2-2][3]), 'r').read())

                file.write('''
                    </div>
               </td>
                <td>
                    <div tabindex="0">
                        <h3>{}</h3>
                '''.format(gallery[(i+1)*2-1][1]))
                print(gallery[(i+1)*2-1][2])
                if gallery[(i+1)*2-1][2] == 'img':
                    file.write('''
                        <img src="art/{}">
                    '''.format(gallery[(i+1)*2-1][0]))
                elif gallery[(i+1)*2-1][2] == 'html':
                    file.write(open("content/body/{}".format(gallery[(i+1)*2-1][3]), 'r').read())

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
        else: # Pages ------------------------------------------------------
            print("    body: {}".format(data[4]), end="")
            file.write('''
<div class="content-wrapper">
            ''')
            if data[4]:
                if str(data[4]).split('.')[-1] == "html":
                    file.write(open("content/body/{}".format(data[4]), 'r').read())
                elif str(data[4]).split('.')[-1] == "md":
                    file.write(markdown.markdown(open("content/body/{}".format(data[4]), 'r').read()))
            file.write('''
</div>
            ''')
        # footer ------------------------------------------------------
        print("    footer: {}".format(data[5]))
        file.write('''
    <footer>
        ''')
        if data[5]:
            file.write(open("content/footer/{}".format(data[5]), 'r').read())
        file.write('''
    </footer>
</body>
</html>
        ''')



# Projects ------------------------------------------------------
projects = []
with con:
    content = con.execute("SELECT * FROM CONTENT WHERE type='project'")

for row in content:
    if not os.path.isdir("docs/project/{}".format(row[0])):
        os.system("mkdir docs/project/{}".format(row[0]))
    build_page(row,"index.html", "project/{}/".format(row[0]), "")
    #projects.append((row[0], row[1]))
    projects.insert(0,(row[0], row[1]))
print(projects)

# Gallery/ART ------------------------------------------------------
gallery = []
with con:
    content = con.execute("SELECT * FROM CONTENT WHERE type='art'")

for row in content:
    #build_page(row,"index.html", "art/{}/".format(row[0]), "")
    gallery.insert(0,(row[0], row[1], row[2], row[4]))
print(gallery)


# Pages ------------------------------------------------------
with con:
    content = con.execute("SELECT * FROM CONTENT WHERE type='page'")

for row in content:
    if row[0] == 'projects.html' or row[0] == 'gallery.html' or row[0] == 'index.html':
        build_page(row, row[0], "", row[0].split('.')[0])
    else:
        build_page(row, row[0], "", "")
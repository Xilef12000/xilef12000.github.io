import os
import sqlite3 as sl
import markdown
import math

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
    '''.format(title, title))
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
        if False:
            pass # later for index
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
    
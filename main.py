import os
import sqlite3 as sl
import markdown

print("deleting old files...")
os.system("rm -r  docs/*")
print("copying new files...")
os.system("cp -r sources/* docs")

con = sl.connect("content.db", check_same_thread=False)

# Build Page ------------------------------------------------------
def build_page(data, id, path):
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

# Pages ------------------------------------------------------
with con:
    content = con.execute("SELECT * FROM CONTENT WHERE type='page'")

for row in content:
    build_page(row, row[0],"")

# Projects ------------------------------------------------------
with con:
    content = con.execute("SELECT * FROM CONTENT WHERE type='project'")

for row in content:
    if not os.path.isdir("docs/project/{}".format(row[0])):
        os.system("mkdir docs/project/{}".format(row[0]))
    build_page(row,"index.html", "project/{}/".format(row[0]))
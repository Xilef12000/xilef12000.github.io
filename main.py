import os
import sqlite3 as sl
import markdown

os.system("rm -r  docs/*")
os.system("cp -r sources/* docs")

con = sl.connect("content.db", check_same_thread=False)

with con:
    content = con.execute("SELECT * FROM CONTENT")

for row in content:
    #print(row)
    print("Building: {}".format(row[0]))
    os.system("touch docs/{}".format(row[0]))
    with open("docs/{}".format(row[0]), "a") as file:
        # head ------------------------------------------------------
        print("    head: {}".format(row[2]), end="")
        file.write('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Xilef12000 | {}</title>
    <meta charset="utf-8" name="description" content="Xilef12000 {}">
    <link rel="icon" sizes="any" type="image/svg+xml" href="/assets/favicon_dark.svg" id="icon"/>
    <link rel="stylesheet" href="/style-sheets/style.css">
        '''.format(row[1], row[1]))
        if row[2]:
            file.write(open("content/head/{}".format(row[2]), 'r').read())
        file.write('''
</head>
        ''')
        # header ------------------------------------------------------
        print("    header: {}".format(row[3]), end="")
        file.write('''
<body>
    <header>
        ''')
        if row[3]:
            file.write(open("content/header/{}".format(row[3]), 'r').read())
        file.write('''
    </header>
        ''')
        # body ------------------------------------------------------
        print("    body: {}".format(row[4]), end="")
        file.write('''
<div class="content-wrapper">
        ''')
        if row[4]:
            if str(row[4]).split('.')[-1] == "html":
                file.write(open("content/body/{}".format(row[4]), 'r').read())
            elif str(row[4]).split('.')[-1] == "md":
                file.write(markdown.markdown(open("content/body/{}".format(row[4]), 'r').read()))
        file.write('''
</div>
        ''')
        # footer ------------------------------------------------------
        print("    footer: {}".format(row[5]))
        file.write('''
    <footer>
        ''')
        if row[5]:
            file.write(open("content/footer/{}".format(row[5]), 'r').read())
        file.write('''
    </footer>
</body>
</html>
        ''')
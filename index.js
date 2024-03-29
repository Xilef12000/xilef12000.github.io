//https://www.digitalocean.com/community/tutorials/how-to-use-ejs-to-template-your-node-application
//https://fireship.io/courses/javascript/node-basics/
const express = require('express');
const marked = require ('marked');
const fs = require ('fs');
const app = express();
app.set('view engine', 'ejs');
const { readFile } = require('fs').promises;
const { existsSync } = require('fs');
const mime = require('mime');

const assets = ['style-sheets', 'scripts', 'assets', 'robots.txt', 'sitemap.txt', 'project'];
const ejs = ['', '/', '/index', '/about', '/projects', '/gallery', 'project', '/aboutme']

var md = function (filename) {
    var path = __dirname +"/views/" + filename;
    var include = fs.readFileSync (path, 'utf8');
    var html = marked.parse(include);
    return html;
};

app.get('*', async (req, res) => {
    try {
        var url = req.originalUrl;
        //console.log(url);
        if (ejs.includes(url) || ejs.includes(url.split('/')[1])) {
            if (url == '/' || url == '') {
                url = 'index';
            }
            //console.log('pages/' + url)
            res.render('pages/' + url, {"md": md});
        }
        else if (assets.includes(url.split('/')[1]) && existsSync('.' + url)){
            //console.log(url);
            if (mime.getType(url.split('.').at(-1)).split('/')[0] == 'text') {
                res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url, 'utf8') );
            }
            else {
                res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url) );
            }
        }
        else {
            //res.status(404).render('pages/404');
            res.status(200).render('pages/404');
        }
    }
    catch (e) {
        console.error(e);
        res.status(500);
    };
});

app.listen(process.env.PORT || 3000, () => console.log(`App available on http://localhost:3000`))

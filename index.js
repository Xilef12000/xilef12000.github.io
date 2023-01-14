//https://www.digitalocean.com/community/tutorials/how-to-use-ejs-to-template-your-node-application
//https://fireship.io/courses/javascript/node-basics/
const express = require('express');
const app = express();
app.set('view engine', 'ejs');
const { readFile } = require('fs').promises;
const { existsSync } = require('fs');
const mime = require('mime');

const assets = ['style-sheets', 'scripts', 'assets', 'robots.txt', 'sitemap.txt'];
const ejs = ['', '/', '/index', '/about']

app.get('*', async (req, res) => {
    try {
        var url = req.originalUrl;
        //console.log(url);
        if (ejs.includes(url)){
            if (url == '/' || url == '') {
                url = 'index';
            }
            res.render('pages/' + url);
        }
        else if (assets.includes(url.split('/')[1]) && existsSync('.' + url)){
            //console.log(url);
            if (url.includes('style-sheets/Fonts/Fontfiles/')) {
                res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url) );
            }
            else {
                res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url, 'utf8') );
            }
        }
        else {
            res.status(404).render('pages/404');;
        }
    }
    catch (e) {
        console.error(e);
        res.status(500);
    };
});

app.listen(process.env.PORT || 3000, () => console.log(`App available on http://localhost:3000`))

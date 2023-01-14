//https://www.digitalocean.com/community/tutorials/how-to-use-ejs-to-template-your-node-application
//https://fireship.io/courses/javascript/node-basics/
const express = require('express');
const app = express();
app.set('view engine', 'ejs');
const { readFile } = require('fs').promises;
const { existsSync } = require('fs');
const mime = require('mime');

const assets = ['style-sheets', 'scripts', 'assets'];

app.get('/', function(req, res) {
    res.render('pages/index');
});

app.get('/about', function(req, res) {
    res.render('pages/about');
});


app.get('*', async (req, res) => {
    const url = req.originalUrl;
    //console.log(url.split('/')[1]);
    
    if (assets.includes(url.split('/')[1]) && existsSync('.' + url)){
        //console.log(url);
        if (url.includes('style-sheets/Fonts/Fontfiles/')) {
            res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url) );
        }
        else {
            res.contentType(mime.getType(url.split('.').at(-1))).send( await readFile('.' + url, 'utf8') );
        }
    }
    else {
        res.status(404).send( await readFile('./404.html', 'utf8') );
    }
});

app.listen(process.env.PORT || 3000, () => console.log(`App available on http://localhost:3000`))

//https://www.digitalocean.com/community/tutorials/how-to-use-ejs-to-template-your-node-application
//https://fireship.io/courses/javascript/node-basics/
const express = require('express');
const app = express();
app.set('view engine', 'ejs');
const { readFile } = require('fs').promises;

app.get('/', function(req, res) {
    res.render('pages/index');
});

app.get('/about', function(req, res) {
    res.render('pages/about');
});


app.get('*', async (req, res) => {
    res.status(404).send( await readFile('./404.html', 'utf8') );
});

app.listen(process.env.PORT || 3000, () => console.log(`App available on http://localhost:3000`))

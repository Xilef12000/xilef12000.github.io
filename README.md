# xilef12000.github.io
Xilef12000's Github Repository for his Github Pages website

[www.Xilef12000.com](https://www.xilef12000.com/)

the actual webpage lives in the [/docs](https://github.com/Xilef12000/xilef12000.github.io/tree/main/docs) folder

render node.js/EJS into static files:
```bash
sh render_webpage.sh
```
use fast mode (i.e. only files in db will be rendered):
```bash
sh render_webpage.sh -f
```
see help:
```bash
sh render_webpage.sh -h
```
```
HELP:  
use -f for fast render mode  
use -w to run without running test web server at the end  
use -n start only the node server in the background  
use -c to stop the node server running in the background  
```

MIT License

Copyright (c) 2022 Xilef12000

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())

function processDNA(a) {
  if (a.length % 3 != 0) {
    return "Invalid sequence"
  }

  if (a[0] != "T" || a[1] != "A" || a[2] != "C") {
    return "Invalid start"
  }

  if (a.slice(-3) == "ATT" || a.slice(-3) == "ATX" || a.slice(-3) == "AXT") {
    var replacedString = a.replace(/[TAXGC]/g, function(match) {
    switch(match) {
        case 'T':
            return 'A';
        case 'A':
            return 'T';
        case 'G':
            return 'X';
        case 'X':
            return 'G';
        case 'C':
            return 'G';
        default:
            return match; // no replacement
    }
});
    return replacedString;
  }
   
  return 'Invalid'
}


app.get('/', (req, res) => {
  res.send("Cannot GET / ;)")
})

app.get('/model', (req, res) => {
  const body = req.body;
  res.send(processDNA(body.sequence))
})

app.listen(8080);

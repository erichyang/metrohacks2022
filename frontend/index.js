const express = require('express')
const app = express()
const port = 3500

app.use(express.static('site'))

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  console.log(`http://localhost:${port}/`)
})

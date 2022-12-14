
const { pyrun } = require('./pyexe')

const test = pyrun('model_test')

test().then(console.log)

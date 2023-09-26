
var pkg = require('./package.json')

module.exports = {
  apps : [{
    name      : pkg.name,
    interpreter: "env/bin/python3",
    script : "./server.py",
    env: {
        PORT: 5001,
    },
  }]
}

module.exports = {
  apps : [{
    name   : "some-python-api",
    interpreter: "env/bin/python3",
    script : "./app.py",
    env: {
        PORT: 5000,
    },
  }]
}

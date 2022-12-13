module.exports = {
  apps : [{
    name   : "keyframe-img2vec-api",
    interpreter: "env/bin/python3",
    script : "./app.py",
    env: {
        PORT: 5000,
    },
  }]
}

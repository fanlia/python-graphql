
const path = require('path')
const { exec } = require('child_process')

const pyexe = path.join(__dirname, '../env/bin/python3')

exports.pyexe = pyexe

const getpyfile = model => path.join(__dirname, `${model}.py`)

exports.getpyfile = getpyfile

const pyrun = (model) => {
    const pyfile = getpyfile(model)

    return async (...modelargs) => {
        const args = [pyexe, pyfile, ...modelargs].join(' ')

        return new Promise((resolve, reject) => {
            exec(args, { encoding: 'utf-8' }, (err, stdout) => {
                if (err) return reject(err)
                stdout = stdout.split('__\n', 2)[1]
                try {
                    const json = JSON.parse(stdout)
                    resolve(json)
                } catch (e) {
                    reject(e)
                }
            })
        })
    }
}

exports.pyrun = pyrun


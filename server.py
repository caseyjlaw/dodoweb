import flask
from subprocess import Popen, PIPE, call

app = flask.Flask(__name__)

@app.route("/<float:resolution>")
def ddplan(resolution):

    # typical parameter values include -d 500.0 -n 96 -b 96 -t 0.000072 -f 1400.0 -s 32 -r 0.5
    cmd = ['dodo', '--', 'DDplan.py', '-otmp.ps']
    if resolution:
        cmd.append('-r {}'.format(resolution))

    stdout, stderr = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
    print(stdout)

    cmd = "dodo  --  gs  -dQUIET  -dSAFER  -dBATCH  -dNOPAUSE  -sDEVICE=jpeg  -sOutputFile=/home/tmp.jpg  -c  <</Orientation 3>> setpagedevice  -f  /home/tmp.ps".split('  ')
    status = call(cmd)

    return flask.send_file('tmp.jpg')

if __name__ == "__main__":
    app.run()

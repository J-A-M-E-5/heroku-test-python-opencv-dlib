# README #

## Heroku Deployment Instructions ##

First to save time and typing set a temporary variable to the name you want for your Heroku deployment, which will be located at http://(yourname).herokuapp.com Ensure you have heroku tool installed (apt-get install heroku for Linux, brew install heroku for OSX) and open up a terminal prompt.

```sh
$ export HEROKU_APP=yourname # Change this accordingly
```

Now we create the heroku instance, specifying whether we'll be using cedar-14 (current production stack) or heroku-16 (beta stack, upcoming production).

For cedar-14:-
```sh
$ heroku create --remote cedar-14 --stack cedar-14 --app $HEROKU_APP
```

...or for beta heroku-16:-
```sh
$ heroku create --remote heroku-16 --stack heroku-16 --app $HEROKU_APP
```

Now specify the buildpack for the instance, there are 4 buildpacks, 2 for each version of the stack, Python 2 or Python 3.

Example for Python 2 on cedar-14 stack:-
```sh
$ heroku buildpacks:add https://github.com/J-A-M-E-5/heroku14-buildpack-python-opencv-dlib --app=$HEROKU_APP
```

Buildpacks you can use are:-
* https://github.com/J-A-M-E-5/heroku14-buildpack-python-opencv-dlib
* https://github.com/J-A-M-E-5/heroku14-buildpack-python3-opencv-dlib
* https://github.com/J-A-M-E-5/heroku16-buildpack-python-opencv-dlib
* https://github.com/J-A-M-E-5/heroku16-buildpack-python3-opencv-dlib

Now either clone this repo (git clone https://github.com/J-A-M-E-5/heroku-test-python-opencv-dlib ) and cd to the folder, or cd /to/your/local/git/repo/with/python/flask/cv2/dlib/code.

Setup the repo for remote push to Heroku:-
```sh
$ heroku git:remote -a $HEROKU_APP
```

Confirm it is setup OK:-
```sh
$ git remote -v
```

Now push to Heroku:-
```sh
$ git push heroku master
```

Now you should be able to visit your instance in your browser.

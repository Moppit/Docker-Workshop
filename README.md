# Docker-Workshop
CUWIC Docker Workshop Fall 2021

# Prerequisites

To complete this workshop, you must have a DockerHub account. It is also helpful to have Python3 and its `flask` library installed.

Create a Docker Hub account: https://hub.docker.com/ 
- Note: make sure you specify that you are using this for educational/personal use to get a free account
- Also note: this is a public sandbox. **DO NOT** add private information to this site, and use a password you don't use on any other site just to be safe.

To download Python 3: https://www.python.org/downloads/

You can install `flask` with the `pip3 install flask` command.

# High Level Idea
Docker is hands-down the most popular containerization tool used in industry today. How does it work? In this workshop, we'll learn how to spin up a docker container to deploy an app!

# Instructions
1. Let's see what we have in this repository -- we've got this README, `app.py`, and `Dockerfile` (and `Dockerfile-Solns` for troubleshooting purposes, but no peeking because that's no fun!). The Python script outlines an app using Flask, and we will fill in the Dockerfile later to create a custom Docker image for our app. For now, let's try running our app locally to see what spinning up an app entails.
    
    a. Type `python3 app.py` in your terminal. What do you get as output? It's usually one of these outcomes:
        
      i. No module named `flask`

      ii. Serves Flask app but with `WARNING: This is a development server. Do not use it in a production deployment.`

      iii. Serves Flask app with no warnings, environment set to `development`

    b. Annoying, isn't it? Based on the machine we're running this on, we get all sorts of different output when we try to run it, because all of our development environments are configured differently.

2. Let's avoid this environment setup issue with Docker! Login to the [Play With Docker (PWD)](https://labs.play-with-docker.com/) environment using your Docker Hub account. Usually people have Docker Desktop to do work locally, but the installation process for Docker Desktop is actually pretty involved, so we'll just use the browser environment for now.

3. On the left side of the screen, click 'Add New Instance'. This will generate a new environment with Docker for us to play around in. Create a directory called `my-app` and navigate to it using the command:
```
mkdir my-app && cd my-app
```

4. Let's upload our app code. Drag-and-drop `app.py` from your local file system's `Docker-Workshop` repo onto the terminal. You should see a bar at the top indicating that you files are loading.

5. Now, we will create a `Dockerfile`, which is basically a list of instructions for Docker to note when creating an image for your app. Execute `touch Dockerfile`. Make sure there is no extention to the file name (i.e. don't have .txt).

6. Now we can add our features of our environment that we want image to support:
    
    a. Start with a root image provided by Docker. Since we are only using Python for our app, using the standard Python image works well here. Add the following to your  `Dockerfile`:
    ```
    FROM python:3.7-alpine
    ADD . /code
    WORKDIR /code
    ```

    b. Now that our image has Python3, let's get the necessary Python3 library: `flask`.
    ```
    RUN pip3 install flask
    ```

    c. Now let's configure our Flask app to run in the development environment to avoid errors. Add:
    ```
    ENV FLASK_APP=app.py
    ENV FLASK_ENV=development
    ```

    d. Let's specify the port at which our app can be accessed. By default, Flask uses port 5000, so let's specify that one.
    ```
    EXPOSE 5000
    ```

    e. Last but not least, we specify what command to use to run the app.
    ```
    CMD ["flask", "run", "--host=0.0.0.0"]
    ```

7. Our image specifications are now good to go! Navigate out of the `my-app` directory using `cd ..`. Then, execute the following command, which basically takes our instructions outlined in our Dockerfile and creates the actual Docker image:
```
docker image build my-app
```

  a. You might see a warning pop up about using pip with root -- don't worry about that, that's just a sandbox issue.
  
  b. You should see "Successfully built XXXXX" at the bottom of the output. Alternatively, you can check if your image build was successful using `docker image ls`, which lists all local docker images. The same XXXXX ID should show up!

  c. Note that this first build will be the slowest -- the rest will be much faster.

8. Label your image with a name and tag using the following command, where XXXXX is the Image ID specified when you do `docker image ls`:
```
docker image tag XXXXX my-app:latest
```

9. Now that our image has a name, we can deploy our Flask app. Run:
```
docker run -p 5000:5000 my-app
```

10. Your site should now be good to go! Right next to `Open Port`, a button should pop up with our port number: `5000`. Click on it, and you should be able to see your site!

# More Resources
Want to learn more about containerization and Docker? Here are some great resources!
- Conceptual approach to containerization: https://docs.docker.com/get-started/overview/ 
- Thorough outline of how to install Docker locally and use it: https://www.tutorialspoint.com/docker/index.htm 
- Labs and tutorials (beginner and advanced): https://training.play-with-docker.com/alacart/
- Docker commands (their documentation is very thorough): https://docs.docker.com/get-started/  

Happy learning!
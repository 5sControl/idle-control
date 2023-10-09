# Idle control

# About Idle control
Idle control is one of the Official [5controlS](https://5controls.com/) algorithm.

Take charge of your team's workforce and ensure maximum productivity. Employees spend time on non-work activities, such as social media or phone calls in the workplace? Optimize your team's or company’s efficiency without delay.

![Frame 2608804](https://github.com/5sControl/idle-control/assets/131950264/4f1ceac2-c24f-4738-a6f4-1c0d6532d62d)


## Key features

- detects idle or unproductive time;
- locates employees when needed.

**Plug-in Idle control to 5controlS platform to start detecting when your workers are on a phone!**

## Getting started 

### Build image for idle_python algorithm
- For x86 users

    ```docker build -t 5scontrol/idle_python:latest .```

- for AArch64 users 

    ```docker buildx build --platform linux/amd64 -t 5scontrol/idle_python:latest .```


### Build image for idle_python_server algorithm

- For x86 users

    ```docker build -t 5scontrol/idle_python_server:latest ./model_image```

- For AArch64 users 

    ```docker build buildx --platform linux/amd64 -t 5scontrol/idle_python_server:latest ./model_image```



### Run containers

*Check id of container:* ```docker images```

- For min_max_python

    ```docker run -rm -it idle_python -e <variables>```

- For min_max_python-server

    ```docker run -rm -it idle_python_server```

  To run min_max algorithm you have to pass following variables:
    - ```folder``` -- folder for saving images
    - ```camera_url``` -- camera url
    - ```server_url``` -- server url


### Run/Test code

- For idle_python

  ```python main.py```

- For idle_python_server

  ```cd ./idle_model && python -m flask run --host 0.0.0.0 --port 5001```


### Push images

- For min_max_python:

  ```docker image push 5scontrol/min_max_python:latest```

- For machine_control_python_server_model:

  ```docker image push 5scontrol/min_max_python-server:latest```

---

# **Project repositories**

The connections between the project repositories are illustrated by the following diagram. 

> Please note that to ensure system stability and perfomance you can use one of the Official 5S algorithms instead of Your Algorithm.

<p align="center">
  <img src="https://github.com/5sControl/5s-backend/assets/131950264/60cbc463-ce88-4af2-a4ed-7e3c01f7a955" alt="5controlS-diagram" />
</p>

**5controlS Platform:**
1. [5s-backend](https://github.com/5sControl/5s-backend)
2. [5s-frontend](https://github.com/5sControl/5s-frontend)
3. [5s-algorithms-controller](https://github.com/5sControl/5s-algorithms-controller)
4. [5s-onvif](https://github.com/5sControl/5s-onvif)
5. [5s-onvif-finder]()

**Official Algorithms:**
1. [min-max](https://github.com/5sControl/min-max)
2. [idle-control](https://github.com/5sControl/idle-control)
3. [operation-control-js](https://github.com/5sControl/operation-control-js)
4. [machine-control](https://github.com/5sControl/machine-control)
5. [machine-control-js](https://github.com/5sControl/machine-control-js)

**Algorithms Servers:**
1. [inference-server-js]()

# **Documentation**

[User Documentation](https://github.com/5sControl/Manufacturing-Automatization-Enterprise/wiki)

# **Contributing**
Thank you for considering contributing to 5controlS. We truly believe that we can build an outstanding product together!

We welcome a variety of ways to contribute. Read below to learn how you can take part in improving 5controlS.

## **Code of conduct**

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## Code contributing

If you want to contribute, read  our [contributing guide](CONTRIBUTING.md) to learn about our development process and pull requests workflow.

We also have a list of [good first issues]() that will help you make your first step to beсoming a 5S contributor.

# **License**

> Please note that [some](Components-with-copyleft-licensies.md) of the Official Algorithms are using copyleft licensies.


<br>
<div align="center">
  <a href="https://5controls.com/" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/3bafa5805821a34e8b825df7cc78e00543fd7a58/assets/Property%201%3DVariant4.png" width="10%" alt="" /></a> 
  <img src="https://github.com/5sControl/5s-backend/assets/131950264/d48bcf5c-8aa6-42c4-a47d-5548ae23940d" width="3%" alt="" />
  <a href="https://github.com/5sControl" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/3bafa5805821a34e8b825df7cc78e00543fd7a58/assets/github.png" width="4%" alt="" /></a>
  <img src="https://github.com/5sControl/5s-backend/assets/131950264/d48bcf5c-8aa6-42c4-a47d-5548ae23940d" width="3%" alt="" />
  <a href="https://www.youtube.com/@5scontrol" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/ebf176c81fdb62d81b2555cb6228adc074f60be0/assets/youtube%20(1).png" width="5%" alt="" /></a>
</div>


# algorithms-python

```bash
docker build ./idle_model -t 5scontrol/idle_python_server:v-.-.-
docker build . -t 5scontrol/idle_python:v-.-.-
```

```bash
docker run --network host --rm 5scontrol/idle_python_server:v-.-.-
docker run --network host --rm 5scontrol/idle_python:v-.-.-
```

# About Idle control
Idle control is one of the Official [5controlS](https://5controls.com/) algorithm. Plug it in our video monitoring system with AI analysis and ERP Integration (Open Source) to uncover employee inefficiencies and minimize downtime.

Take charge of your team's workforce and ensure maximum productivity. Employees spend time on non-work activities, such as social media or phone calls in the workplace? Optimize your team's or company’s efficiency without delay.

![Idle-control](https://github.com/5sControl/5s-user-documentation/blob/main/assets/Idle-control.png)


## Key features

- detects idle or unproductive time;
- locates employees when needed.

**Plug-in Idle control to 5controlS platform to start detecting when your workers are on a phone!**

> Learn more about Idle control on the [5controlS website](https://5controls.com/solutions/employee-monitoring-software).

# Getting started 

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

- For idle_python

    ```docker run -rm -it idle_python -e <variables>```

- For idle_python_server

    ```docker run -rm -it idle_python_server```

  To run idle algorithm you have to pass following variables:
    - ```folder``` -- folder for saving images
    - ```camera_url``` -- camera url
    - ```server_url``` -- server url


### Run/Test code

- For idle_python

  ```python main.py```

- For idle_python_server

  ```cd ./idle_model && python -m flask run --host 0.0.0.0 --port 5001```


### Push images

- For idle_python:

  ```docker image push 5scontrol/idle_python:latest```

- For idle_python_server:

  ```docker image push 5scontrol/idle_python_server:latest```


# **Documentation**

[Documentation for Developers](https://github.com/5sControl/5s-dev-documentation/wiki)

[User Documentation](https://github.com/5sControl/Manufacturing-Automatization-Enterprise/wiki)

# **Contributing**
Thank you for considering contributing to 5controlS. We truly believe that we can build an outstanding product together!

We welcome a variety of ways to contribute. Read below to learn how you can take part in improving 5controlS.

## **Code of conduct**

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## Code contributing

If you want to contribute, read  our [contributing guide](CONTRIBUTING.md) to learn about our development process and pull requests workflow.

We also have a list of [good first issues](https://github.com/5sControl/idle-control/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) that will help you make your first step to beсoming a 5S contributor.


# **Project repositories**

**5controlS Platform:**
1. [5s-webserver](https://github.com/5sControl/5s-webserver)
2. [5s-backend](https://github.com/5sControl/5s-backend)
3. [5s-frontend](https://github.com/5sControl/5s-frontend)
4. [5s-algorithms-controller](https://github.com/5sControl/5s-algorithms-controller)
5. [5s-onvif](https://github.com/5sControl/5s-onvif)
6. [5s-onvif-finder](https://github.com/5sControl/5s-onvif-finder)
  
**Official Algorithms:**
1. [min-max](https://github.com/5sControl/min-max)
2. [idle-control](https://github.com/5sControl/idle-control)
3. [operation-control-js](https://github.com/5sControl/operation-control-js)
4. [machine-control](https://github.com/5sControl/machine-control)
5. [machine-control-js](https://github.com/5sControl/machine-control-js)

**Algorithms Servers:**
1. [inference-server-js](https://github.com/5sControl/inference-server-js)

# **License**

[AGPL-3.0](LICENSE)

> Idle control uses third party libraries that are distributed under their own terms (see [LICENSE-3RD-PARTY.md](https://github.com/5sControl/idle-control/blob/main/LICENSE-3RD-PARTY.md)).<br>

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


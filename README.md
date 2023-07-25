# algorithms-python

```bash
docker build ./idle_models -t 5scontrol/idle_python_server:v-.-.-
docker build . -t 5scontrol/idle_python:v-.-.-
```

```bash
docker run --network host --rm 5scontrol/idle_python_server:v-.-.-
docker run --network host --rm 5scontrol/idle_python:v-.-.-
```

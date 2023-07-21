# algorithms-python

```bash
docker build ./idle_model -t 5scontrol/idle_python_server:v-.-.-
docker build . -t 5scontrol/idle_python:v-.-.-

docker run --network host --rm 5scontrol/idle_python_server:v-.-.-
docker run --network host --rm 5scontrol/idle_python:v-.-.-
```

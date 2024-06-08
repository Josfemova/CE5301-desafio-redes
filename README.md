## Configuración

```Shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Requisitos

Se debe tener un equipo que provea un entrono IOS XE, de no tenerlo se puede
solicitar un sandbox en
<https://devnetsandbox.cisco.com/DevNet/sandboxes/>.
Para el desarrollo de este desafío se hizo uso del sandbox
"IOS XE on Cat8kv AlwaysOn"

## Ejecución:

### Monitor:

```Shell
python subscriber.py
```

### Trigger de alerta (cambio de config)

```Shell
python trigger.py
```

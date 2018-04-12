# konfig

konfig is a library to make it simple for Python applications to read and write config maps.

The library aims to solve the problem that some applications have that they only need
a relatively tiny amount of storage that is rarely updated.

## Usage

Give the service account access to read a config map:

```
kubectl create configmap test-config --from-literal=test1=1
kubectl create role test-config-writer --verb=get,update --resource=configmaps --resource-name=test-config
kubectl create rolebinding sa-test-config-writer --serviceaccount=default:default --role=test-config-writer
```

Read / write the config map:
```
import konfig

configmap = konfig.configmap('test-config', namespace='default')

myconfig = configmap.read()
myconfig['test1'] = int(myconfig['test1'])
configmap.update(myconfig)
```

Enjoy!

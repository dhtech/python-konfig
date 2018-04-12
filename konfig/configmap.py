"""konfig is a library to make it simple to read and write config maps.

It uses the service account inside the pod to access the API and supports no
other way of reading the credentials. The library aims to solve the problem
that some applications have that they only need a relatively tiny amount of
storage that is rarely updated.

Example: Read / write the config map:

    import konfig

    configmap = konfig.configmap('test-config', namespace='default')
    myconfig = configmap.read()
"""

import json
import os
import requests


class ConfigMap(object):
    def __init__(self, name, namespace, server):
        self.name = name
        self.namespace = namespace
        self.server = server

    def read(self):
        pass

    def update(self):
        pass


def configmap(name, namespace=None, server=None):
    """Create a ConfigMap referring to a config map.

    Args:
      name: Name of the config map.
      namespace: Namespace name, or None in which case either
        KONFIG_NAMESPACE will be used if set or 'default'.
      server: Server URL, or None in which case either
        KONFIG_SERVER will be used if set or 'https://kubernetes.default'.

    Returns:
      ConfigMap instance
    """

    return ConfigMap(name, namespace, server)

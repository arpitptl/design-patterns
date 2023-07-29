"""
Proxy design pattern:

The Proxy design pattern is a structural pattern that provides a surrogate or placeholder for another object. It acts as an intermediary to control access to the real object, adding extra functionalities if necessary, without changing the actual object's interface.

Let's create an example of a Proxy pattern for a network connection manager. We have a NetworkConnection interface representing the real network connection, and a NetworkConnectionProxy acting as a proxy to control access to the actual network connection.
"""

from abc import ABC, abstractmethod

# Subject (Interface) - NetworkConnection
class NetworkConnection(ABC):
    @abstractmethod
    def connect(self, url):
        pass

# Real Subject - NetworkConnectionImpl
class NetworkConnectionImpl(NetworkConnection):
    def connect(self, url):
        print(f"Connecting to {url}...")

# Proxy - NetworkConnectionProxy
class NetworkConnectionProxy(NetworkConnection):
    def __init__(self):
        self._real_connection = None

    def connect(self, url):
        if self._real_connection is None:
            self._real_connection = NetworkConnectionImpl()
        print("Proxy: Checking user access...")
        self._real_connection.connect(url)

# Client code
if __name__ == "__main__":
    proxy = NetworkConnectionProxy()

    # First connection - real object is created
    proxy.connect("http://example.com")
    
    # Second connection - real object is reused from the proxy
    proxy.connect("https://example.org")




"""
In this example, the NetworkConnection is the subject interface with the connect() method. The NetworkConnectionImpl is the real subject class that implements the NetworkConnection interface and represents the actual network connection.

The NetworkConnectionProxy acts as a proxy for the real network connection. It has an instance of NetworkConnectionImpl, which is created lazily only when the proxy is first used to connect to a URL. The proxy checks user access or performs additional operations before delegating the connection request to the real connection.

When the client code connects to a URL using the proxy, the proxy checks the user's access (in this case, it's just a placeholder check), and if the real connection does not exist yet, it creates the real connection (NetworkConnectionImpl) and delegates the connection request to it. For subsequent connection requests, the proxy reuses the existing real connection.

By using the Proxy pattern, we can control access to expensive or remote resources, add logging or caching, or perform additional operations without modifying the real object's implementation. It enables us to optimize the usage of resources and provides a level of indirection for the client code, enhancing the system's flexibility and performance.
"""

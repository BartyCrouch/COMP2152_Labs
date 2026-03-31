import socket
import urllib.request
class Scanner:
    """Parent class — shared by all scanner types."""
    def __init__(self, target):
        self.target = target
        self.results = []

    def display_results(self):
        print(f"Results for {self.target}:")
        if not self.results:
            print("  (no results)")
        else:
            for r in self.results:
                print(f"    {r}")


class PortScanner(Scanner):
    """Child class — scans for open ports."""
    def __init__(self, target, ports):
        super().__init__(target)
        self.ports = ports

    def scan(self):
        for port in self.ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    self.results.append(f"Port {port}: OPEN")
                else:
                    self.results.append(f"Port {port}: closed")
            except socket.error as e:
                self.results.append(f"Port {port}: error {e}")


class HTTPScanner(Scanner):
    """Child class — scans HTTP paths for accessible pages."""

    # TODO: Write __init__(self, target, paths)
    #   Call the parent constructor: super().__init__(target)
    #   Store self.paths (a list of URL paths like "/", "/admin")
    def __init__(self, target, paths):
        pass

    # TODO: Write scan(self)
    #   Loop through self.paths
    #   For each path:
    #     Try: urllib.request.urlopen(f"http://{self.target}{path}")
    #       Append f"{path} → {response.status} (accessible)" to self.results
    #     Except: Append f"{path} → NOT FOUND" to self.results
    def scan(self):
        pass


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: SCANNER INHERITANCE")
    print("=" * 60)

    print("\n--- Port Scanner ---")
    ps = PortScanner("127.0.0.1", [22, 80, 443])
    print(f"  Scanning {ps.target} ports...")
    ps.scan()
    ps.display_results()

    print("\n--- HTTP Scanner ---")
    hs = HTTPScanner("127.0.0.1", ["/", "/admin", "/.git/config"])
    print(f"  Scanning {hs.target} paths...")
    hs.scan()
    hs.display_results()

    print("\n" + "=" * 60)
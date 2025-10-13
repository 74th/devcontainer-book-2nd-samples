import urllib.request
import subprocess
import unittest
import re


class TestConnection(unittest.TestCase):
    def test_sidecar(self):
        with urllib.request.urlopen("http://sidecar/") as response:
            self.assertEqual(response.status, 200)

    def test_host_docker_internal(self):
        with urllib.request.urlopen("http://host.docker.internal:18080/") as response:
            self.assertEqual(response.status, 200)

    def test_ip_gateway(self):
        ip_route = subprocess.run(["ip", "route"], check=True, text=True, capture_output=True)
        output = ip_route.stdout
        match = re.search(r'default via (\d+\.\d+\.\d+\.\d+)', output)
        if match:
            gateway_ip = match.group(1)
        else:
            self.fail("Gateway IP not found in ip route output")

        with urllib.request.urlopen(f"http://{gateway_ip}:18080/") as response:
            self.assertEqual(response.status, 200)

    def test_host_ip(self):
        with urllib.request.urlopen("http://192.168.1.191:18080/") as response:
            self.assertEqual(response.status, 200)

    def test_github(self):
        with urllib.request.urlopen("https://github.com/74th.keys/") as response:
            self.assertEqual(response.status, 200)


if __name__ == "__main__":
    unittest.main(verbosity=2)
import httpx
import subprocess
import pytest
import mysql.connector
from mysql.connector import Error
import time
import re


class TestMySQLConnection:
    """MySQLデータベースへの接続テスト"""

    @pytest.fixture(scope="class")
    def mysql_config(self):
        """MySQL接続設定"""
        return {
            'host': 'mysql',  # Docker Composeのサービス名
            'port': 3306,
            'user': 'mysql',
            'password': 'password',
            'database': 'sampledb'
        }

    @pytest.mark.timeout(30)
    def test_mysql_connection(self, mysql_config):
        """MySQLへの接続確認"""
        connection = None
        cursor = None
        try:
            # MySQL接続
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()

            # SHOW TABLESクエリを実行
            cursor.execute("SHOW TABLES")
            cursor.fetchall()

        except Error as e:
            pytest.fail(f"SHOW TABLESクエリの実行に失敗しました: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    @pytest.mark.timeout(30)
    def test_host_docker_internal(self):
        response = httpx.get("http://host.docker.internal:18080/")
        assert response.status_code == 200

    @pytest.mark.timeout(30)
    def test_ip_gateway(self):
        ip_route = subprocess.run(["ip", "route"], check=True, text=True, capture_output=True)
        output = ip_route.stdout
        match = re.search(r'default via (\d+\.\d+\.\d+\.\d+)', output)
        if match:
            gateway_ip = match.group(1)
        else:
            pytest.fail("Gateway IP not found in ip route output")

        response = httpx.get(f"http://{gateway_ip}:18080/")
        assert response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
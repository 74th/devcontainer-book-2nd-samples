import httpx
import pytest
import mysql.connector
from mysql.connector import Error
import time


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
    def test_host_connection(self):
        response = httpx.get("http://host.docker.internal:18080/")
        assert response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
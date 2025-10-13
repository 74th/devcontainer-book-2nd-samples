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
    def test_show_tables(self, mysql_config):
        """SHOW TABLESクエリの実行テスト"""
        connection = None
        cursor = None
        try:
            # MySQL接続
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()

            # SHOW TABLESクエリを実行
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            # テーブル一覧を表示（デバッグ用）
            print(f"データベース内のテーブル数: {len(tables)}")
            for table in tables:
                print(f"テーブル: {table[0]}") # type: ignore

            # テストは成功（テーブルが0個でも接続とクエリ実行が成功していれば良い）
            assert isinstance(tables, list), "SHOW TABLESの結果がリスト形式ではありません"

        except Error as e:
            pytest.fail(f"SHOW TABLESクエリの実行に失敗しました: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
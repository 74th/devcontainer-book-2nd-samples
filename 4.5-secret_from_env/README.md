秘匿情報をenvfileで環境変数に渡す

.devcontainer/devcontainer.env に KEY=VALUE 形式でシークレットを保存する。
生成を、initializeCommandで行うと便利。

[./.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json)

runArgsで`--env-file .devcontainer/devcontainer.env`を指定する。

ただし、コンテナ作成時に埋め込まれるため、コンテナ停止、起動を行っても新しい値は反映されず、コンテナを再作成する必要がある。

.devcontainer/devcontainer.json内で`${localEnv:MY_HOME}`のようにして、ホストの環境変数を参照することもできるが、IDEが認識している環境変数を制御する必要があり、難しいのであまりお勧めしない。
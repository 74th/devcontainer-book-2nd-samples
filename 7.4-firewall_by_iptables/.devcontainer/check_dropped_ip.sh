#!/bin/bash
# xt_recentモジュールで記録されたドロップされたIPアドレス
grep -Eo 'src=[0-9\.]+' /proc/net/xt_recent/dropped_out
#!/bin/bash

# nginx日志目录
log_path={INSTALL_DIR}/opt/nginx/logs

# 切割的日志
log_name=*.log

# 备份目录
backup_path={INSTALL_DIR}/var/backup/nginx/logs
backup_path=$backup_path/$(date -d "yesterday" +"%Y%m%d")

# 保留天数
save_days=30

# NGINX命令
nginx_sbin="{INSTALL_DIR}/opt/nginx/sbin/nginx"

mkdir -p $backup_path/
for i in $(ls ${log_path}/${log_name}); do
	mv $i ${backup_path}/
done
$nginx_sbin -s reload

# 删除历史日志
find $backup_path -mtime +$save_days -exec rm -rf {} \; 

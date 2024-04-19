#!/bin/bash

# Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Clone repo, using the function do_pack.

# Function to archive the content of the web_static dir
do_pack() {
    dt=$(date -u +"%Y%m%d%H%M%S")
    file="versions/web_static${dt}.tgz"

    if [ ! -d "versions" ]; then
        if ! mkdir -p versions; then
            return 1
        fi
    fi

    if ! tar -cvzf "$file" web_static; then
        return 1
    fi

    echo "$file"
}

# Function to distribute an archive to web servers
do_deploy() {
    archive_path="$1"

    if [ ! -f "$archive_path" ]; then
        return 1
    fi

    file=$(basename "$archive_path")
    filename="${file%.*}"

    if ! scp "$archive_path" "ubuntu@54.227.197.97:/tmp/$file"; then
        return 1
    fi

    ssh ubuntu@54.227.197.97 "mkdir -p /data/web_static/releases/$filename/" || return 1
    ssh ubuntu@54.227.197.97 "tar -xzf /tmp/$file -C /data/web_static/releases/$filename/" || return 1
    ssh ubuntu@54.227.197.97 "rm /tmp/$file" || return 1
    ssh ubuntu@54.227.197.97 "mv /data/web_static/releases/$filename/web_static/* /data/web_static/releases/$filename/" || return 1
    ssh ubuntu@54.227.197.97 "rm -rf /data/web_static/releases/$filename/web_static" || return 1
    ssh ubuntu@54.227.197.97 "rm -rf /data/web_static/current" || return 1
    ssh ubuntu@54.227.197.97 "ln -s /data/web_static/releases/$filename/ /data/web_static/current" || return 1

    return 0
}

# Function to deploy the content
deploy() {
    do_deploy "$(do_pack)"
}

# Invoke deploy function
deploy

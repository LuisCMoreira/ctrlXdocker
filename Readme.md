 sudo docker buildx create --use

 ## In scripts folder
 sudo ./build_all.sh "arm64"


scp boschrexroth@snap:/home/boschrexroth/ctrlXdocker/twin/ctrlx-docker-robot_1.1_amd64.snap .

## for file transfer

scp -r boschrexroth@snap:/home/boschrexroth/ctrlXdocker/ .
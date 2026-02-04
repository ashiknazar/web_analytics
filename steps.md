## STEP 1 — Install Docker (ENGINE)
#### Update system
```bash
sudo apt update
sudo apt upgrade -y
```
#### install prerequisites
```bash
sudo apt install -y \
  ca-certificates \
  curl \
  gnupg \
  lsb-release
```
#### Add Docker GPG key
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
#### Add Docker repository
```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
#### install docker
```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```
#### Enable & start Docker
```bash
sudo systemctl enable docker
sudo systemctl start docker

```
#### Allow Docker without sudo (IMPORTANT)

```bash
sudo usermod -aG docker $USER
newgrp docker
```

## STEP 2 —Install Docker Compose (Plugin)
- Modern Docker uses compose plugin, not old `docker-compose`.
```bash
docker compose version
```
## STEP 3 — Create Project Workspace
#### Create project root
```bash
mkdir web_analytics
cd web_analytics
```
#### Create directory structure
```
mkdir -p \
flask-app \
kafka \
storm \
spark \
hdfs \
hive/ddl \
scripts
```
## STEP 4 — Create Minimal Flask App (First Real Component)

- Create `flask-app/app.py`
- create `flask-app/requirements.txt`
- Create `flask-app/Dockerfile`
- create `docker-compose.yml`

### Clean Rebuild of Docker Environment
```bash
docker-compose down -v
docker system prune -af
docker-compose up --build
```

#### step 5 -
-  HDFS NameNode
```bash
 http://localhost:50070
```


#### step 6 - Create HDFS directories

```bash
docker exec -it hdfs-namenode hdfs dfs -mkdir -p /data/raw/web_analytics
docker exec -it hdfs-namenode hdfs dfs -chmod -R 777 /data
```
- verify :
```bash
docker exec -it hdfs-namenode hdfs dfs -ls /data/raw
```
#### step 7 - create kafka -> hdfs consumer
- create kafka/consumer.py,kafka/requirements.txt,kafka/Dockerfile
- added kafka consumer to docker-compose.yml
- build and start everything
```bash
docker compose up --build -d
```
- Verify data is going into HDFS 
   - list directories
    ```bash
     docker exec -it hdfs-namenode hdfs dfs -ls /data/raw/web_analytics
    ```
   - list files
    ```bash
     docker exec -it hdfs-namenode hdfs dfs -ls /data/raw/web_analytics/dt=2026-02-04
    ```
   - view data
    ```bash
     docker exec -it hdfs-namenode hdfs dfs -cat /data/raw/web_analytics/dt=2026-02-04/*.json | head

    ```

# Create a Docker repository in Artifact Registry

gcloud artifacts repositories \
     create my-docker-repo \
     --repository-format=docker \
     --location=us-central1 \
     --description="Docker repository"  

export PROJECT=$(gcloud info --format='value(config.project)')
gcloud builds submit --tag \
     us-central1-docker.pkg.dev/$PROJECT/my-docker-repo/mongo-docker:latest

gcloud run deploy mongo-docker --image us-central1-docker.pkg.dev/$PROJECT/my-docker-repo/mongo-docker:latest
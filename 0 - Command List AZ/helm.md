# Install helm

wget https://get.helm.sh/helm-v3.12.3-linux-amd64.tar.gz 

tar -zxvf helm-v3.12.3-linux-amd64.tar.gz

mv linux-amd64/helm /usr/bin/helm

# Repo Add

helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo add argocd https://argoproj.github.io/argo-helm

# Repo index refresh
helm update repo 

# Repo list
helm repo list

# Repo search charts
helm search repo argocd

# Install argocd and update
helm install argocd argocd/argocd-image-updater

helm upgrade --install argocd argocd/argo-cd

# Namespace
helm install --namespace argocd argocd/argocd-image-updater

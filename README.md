# ArgoCD Upgrade
ArgoCD Installation and Upgrade (GitOps using ArgoCD)

## ArgoCD Old Version
```bash
helm search repo argocd --versions | grep 5.16.0
```
- Chart Version: 5.16.0
- App Version: v2.5.3

## ArgoCD New Version
```bash
helm search repo argocd --versions | grep 5.53.14
```
- Chart Version: 5.53.14
- App Version: v2.9.6

# Installation
## Add ArgoCD Helm Repo
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

## Install ArgoCD Old Version using Helm
```bash
helm install argocd argo/argo-cd --version "5.16.0" -n argocd --create-namespace
```

## Check Revision, Chart Version and App Version
```bash
helm ls -n argocd
```

## Get ArgoCD Admin Password
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## Port-Forward the ArgoCD Service
```bash
kubectl -n argocd port-forward svc/argocd-server 8080:80
```

## Access the ArgoCD UI
- Open [https://localhost:8080](https://localhost:8080) in Web Browser.
- Username: admin
- Password: `See Above Command`

## Create the ArgoCD Applications (App of Apps)
```bash
kubectl -n argocd apply -f https://raw.githubusercontent.com/jameelkaisar/argocd-upgrade/main/multi-app/app-of-apps.yaml
```

## Access the HDFZ App
- Port-Forward the Istio Ingress Service
```
kubectl port-forward service/istio-ingressgateway 8081:80 -n istio-ingress
```
- Open [https://localhost:8081](https://localhost:8081) in Web Browser.

# Upgrade
- Recommended: Disable Auto-Sync and Auto-Prune

## Upgrade ArgoCD Chart Version in the Git Repo
- Change `spec.source.targetRevision` in `app-of-apps/argocd.yaml` from `5.16.0` to `5.53.14` and Commit the Changes

## Apply Upgrade in the Cluster
- Sync the Changes and Prune the Old Resources in ArgoCD UI

## Port-Forward the ArgoCD Service
```bash
kubectl -n argocd port-forward svc/argocd-server 8080:80
```

## Access the ArgoCD UI
- [https://localhost:8080](https://localhost:8080)
- Username: admin
- Password: `Same Password`

# ArgoCD Resources
- https://argo-cd.readthedocs.io/en/stable/user-guide/helm
- https://artifacthub.io/packages/helm/argo/argo-cd
- https://github.com/argoproj/argo-helm
- https://github.com/argoproj/argo-cd

# ArgoCD Changelog
- https://argo-cd.readthedocs.io/en/stable/operator-manual/upgrading/overview
- https://github.com/argoproj/argo-helm/tree/main/charts/argo-cd#changelog

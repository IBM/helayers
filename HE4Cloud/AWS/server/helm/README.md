# HE for Cloud HELM chart deployment instructions

1. Create a Kubernetes secret with your Artifactory credentials:

   ``` 
   kubectl create secret docker-registry -n <namespace> artregcred \
     --docker-server=res-he4cloud-team-docker-local.artifactory.swg-devops.com \
     --docker-username=<e-mail> \
     --docker-password=<artifactory-token> \
     --docker-email=<e-mail>
   ```
   where 
   `<namespace>` is the namespace you plan to deploy he4cloud to;
   `<e-mail>` is your Artifactory email;
   `<artifactory-token>` is retrieved from your Artifactory profile.

2. Modify `values.yaml` to your secret manager values (these will be provided from the installation of IBM Secret Manager/Vault)

   ```
   secret_manager_url: <url>
   secret_manager_token: <token>
   secret_path: <secret-path>
   he4c_env: <env>
   ```
   where `he4c_env` is one of:
   - `IBM` when deploying to the IBM cloud;
   - `K8S` for on-prem deployment;
   - `CASH` for deployment to the CASH OpenShift environment

3. Deploy the server - run from the `helm` directory:

   ```
   helm install <release-name> . -n <namespace>
   ```
   where `<release-name>` is the name the release will be created as (eg `he4cloud`) and `<namespace>` is the name of the namespace to deploy to. **Note:** the namespace must already exist

4. To uninstall:

   ```
   helm uninstall <release-name> -n <namespace>
   ```

Note: If you use other images or tags, just modify `values.yaml` as required.

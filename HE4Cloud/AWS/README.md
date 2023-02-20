# HE for Cloud - AWS Installation 

## Pre-requisisties
- An AWS Account with administrator privileges
- A DNS domain.

## AWS Services Setup  
1. ### **AWS Cognito**  
    1. Create a `user pool` with the following settings:  
        1.  In step 5 of creating the user pool - **Integrate you app**
            - Under the **Hosted authentication pages** section, check **Use the Cognito Hosted UI**.
            - Under the **Initial app client section**:   
                - select **Confidential client**.
                - In the **Allowed callbacks URLs**, add https://`<Your DNS Domain>`/IBMid/callback
    1. Create an `identity pool` with the following settings:  
        1. **Authentication flow settings** having **Allow Basic (Classic) Flow** checked.
        1. **Authentication providers**, in the cognito tab enter the **User Pool ID** and its associated **App client id**, created in the previous steps.

1. ### **IAM**
    1. Create an IAM Policy with the following actions defined:
        - `kms:TagResource`
        - `kms:PutKeyPolicy`
        - `kms:CreateAlias`
        - `kms:ListKeys`
        - `kms:ListAliases`
        - `kms:CreateKey`  
    1. Create an IAM role with the following settings:
        - *Trusted entity type*: `Web Identity`  
        - *Identity Provider*: `Amazon Cognito`  
        - *Identity Pool ID*: The ID of the Identity Pool created in `1.2`  
        - Add the policy defined in `2.1` to the Role’s Permissions list  
    1. Create an IAM policy with the following actions defined:
        - `s3:CreateBucket`
        - `s3:ListBucket`
        - `s3:DeleteBucket`
        - `s3:PutObject`
        - `s3:GetObject`
        - `s3:DeleteObject`
    1. Create an `IAM User` with the following settings:
        - `"AWS Access Type"` of `"Access key - Programmatic Access"`
        - Attach the IAM Policy created in step 3. 
        - Save the `Access Key` and `Secret Key` generated at the end of the process.

1. ### **Elastic Kubernetes Service (EKS)** 
    1. Create a cluster.
    1. Install AWS Load Balancer Controller (Follow instructions in [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)).
    1. Create a Kubernetes docker-registry secret to a Docker repository which will contain the He4Cloud images.

## MongoDB
Create a [free](https://www.mongodb.com/cloud/atlas/register) MongoDb cluster.

## Installation of HE4Cloud Components
- ### **Pre-requisisties**:  
   The following tools need to be installed:  
    - `kubectl`
    - `helm`
    - `yq`
    - `make`

   **`Notes:`**      
   - kubectl needs to be configured to access the kubernetes cluster created above.
   - Push the He4Cloud images found in IBM Box to the Docker repository used during `IAM Services` step `3.3`. Contact chamliam@ie.ibm.com to get access to IBM Box.
     
1. ### **Ingress**
   1. Run make command:
   ```makefile
       make deploy-ingress HOST=<Your Domain's Host Name>
   ```
   2. Add HTTPS Listener to the created Load Balancer (Follow instructions in AWS documentation).
1. ### **HE4Cloud Server**  
    1. Modify file [server.helm.env](./server/server.helm.env).  
       Follow instructions in the file.
    1. Run make command:
    ```makefile
        make helm-server-install HELM_CONFIG=<PATH_TO_SERVER_HELM_ENV>
    ```
1. ### **HE4Cloud UI**
    1. Modify file [ui.helm.env](./ui/ui.helm.env).  
       Follow instructions in the file.
    1. Run make command:
    ```makefile
        make helm-ui-install HELM_CONFIG=<PATH_TO_UI_HELM_ENV>
    ```

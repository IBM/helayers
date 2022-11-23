ifneq ($(HELM_CONFIG),)
include $(HELM_CONFIG)
endif

BLACK        := \033[0;30m 
DARK_GRAY    := \033[1;30m
RED          := \033[0;31m
LIGHT_RED    := \033[1;31m
GREEN        := \033[0;32m
LIGHT_GREEN  := \033[1;32m
ORANGE       := \033[0;33m
YELLOW       := \033[1;33m
BLUE         := \033[0;34m
LIGHT_BLUE   := \033[1;34m
PURPLE       := \033[0;35m
LIGHT_PURPLE := \033[1;35m
CYAN         := \033[0;36m
LIGHT_CYAN   := \033[1;36m
LIGHT_GRAY   := \033[0;37m
WHITE        := \033[1;37m
# No Color
NC           := \033[0m

MAKEFILE_PATH := $(firstword $(MAKEFILE_LIST))
THIS_DIR := $(dir $(abspath $(MAKEFILE_PATH)))
toLC = $(shell echo $1 | tr '[:upper:]' '[:lower:]')

HELM_UI_INSTALL_NAME := he4cloud-ui
HELM_SERVER_INSTALL_NAME := he4cloud-server-provisioning

## Install/Upgrade HE4Cloud UI helm chart
## Options:
## HELM_CONFIG=<HELM_CONFIG> [Mandatory] Path to Helm config file
.PHONY: helm-ui-install
helm-ui-install:
	@if [ -z ${HELM_CONFIG} ] || [ ! -f ${HELM_CONFIG} ]; then \
		echo "HELM_CONFIG not found or defined"; \
		exit 1; \
	fi;

	@helm upgrade \
		--set "deployment.env=AWS" \
		--set "env.clusterUrl=${CLUSTER_URL}" \
		--set "env.serverBaseUrl=${SERVER_PUBLIC_ENDPOINT}" \
		--set "env.apiVersion=${SERVER_VERSION}" \
		--set "env.commonClientId=${AWS_COGNITO_CLIENT_ID}" \
		--set "env.commonClientSecret=${AWS_COGNITO_CLIENT_SECRET}" \
		--set "env.commonBaseAuthorizationUrl=${AWS_COGNITO_AUTH_API_URL}" \
		--set "env.commonIssuer=${AWS_COGNITO_AUTH_ISSUER}" \
		--set "env.kmsEnv=AWS" \
		--set "env.aws.roleArn=${AWS_COGNITO_USER_ROLE_ARN}" \
		--set "env.aws.accountId=${AWS_ACCOUNT_ID}" \
		--set "env.aws.identityPoolId=${AWS_COGNITO_IDENTITY_POOL_ID}" \
		--set "env.aws.loginId=${AWS_COGNITO_IDENTITY_PROVIDER_NAME}" \
		--install \
		--atomic \
		--cleanup-on-fail \
		${PARAMS} \
		${HELM_UI_INSTALL_NAME} \
		${THIS_DIR}./ui/helm

## Uninstall HE4Cloud UI helm chart
.PHONY: helm-ui-uninstall
helm-ui-uninstall:	
	@helm uninstall ${HELM_UI_INSTALL_NAME}

## Install HE4Cloud server helm chart
## Options:
## HELM_CONFIG=<HELM_CONFIG> [Mandatory] Path to Helm config file 
.PHONY: helm-server-install
helm-server-install:
	@if [ -z ${HELM_CONFIG} ] || [ ! -f ${HELM_CONFIG} ]; then \
		echo "HELM_CONFIG not found or defined"; \
		exit 1; \
	fi;

	@helm upgrade \
        --set "deployment.env=AWS" \
        --set "env.cluster_ip=${CLUSTER_PUBLIC_ENDPOINT}" \
        --set "env.api_version=${SERVER_VERSION}" \
		--set "env.shared_model_bucket=${SHARED_MODEL_BUCKET}" \
        --set "env.aws.cognito_client_id=${AWS_COGNITO_CLIENT_ID}" \
        --set "env.aws.cognito_identity_provider_name=${AWS_COGNITO_IDENTITY_PROVIDER_NAME}" \
        --set "env.aws.cognito_signing_keys_url=${AWS_COGNITO_SIGNING_KEYS_URL}" \
        --set "env.aws.mongodb_connection_string=${MONGODB_CONNECTION_STRING}" \
        --set "env.aws.mongodb_database=${MONGODB_DATABASE}" \
		--set "env.aws.access_key_id=${AWS_ACCESS_KEY_ID}" \
		--set "env.aws.secret_access_key=${AWS_SECRET_ACCESS_KEY}" \
		--install \
		--atomic \
		--cleanup-on-fail \
		${PARAMS} \
		${HELM_SERVER_INSTALL_NAME} \
        ${THIS_DIR}./server/helm

## Uninstall HE4Cloud server helm chart
.PHONY: helm-server-uninstall
helm-server-uninstall:	
	@helm uninstall ${HELM_SERVER_INSTALL_NAME}

## Install Ingress
## Options:
## HOST=<HOST> [Mandatory] The Domain Host name 
.PHONY: deploy-ingress
deploy-ingress:
	@if [ -z ${HOST} ]; then \
		echo "HOST not defined"; \
		exit 1; \
	fi;

	@yq eval ".spec.tls[0].hosts = [\"${HOST}\"]" --inplace ${THIS_DIR}./k8s/ingress.yaml
	@kubectl apply -f ${THIS_DIR}./k8s/ingress.yaml

.PHONY: help
help:
	@printf "Usage:\n";
	@printf "make [target]\n";
	@printf "\ntargets:\n";
	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-_0-9]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf "${LIGHT_CYAN}%-15s${NC} %s\n", helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-_0-9.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "${CYAN}%-35s${NC} %s\n", helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = sprintf("%s\n%-20s%s", helpMessage, "" ,substr($$0, 3)); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n%-35s\n", helpMessage \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

.DEFAULT_GOAL := help
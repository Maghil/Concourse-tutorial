command to run concourse in docker
> docker-compose up -d

command to sign in to concourse with fly
> fly -t tutorial login -c http://localhost:8080 -u test -p test

command to set pipeline
> fly -t tutorial set-pipeline -p python_test -c python_test.yml

command to unpause pipeline
> fly -t tutorial unpause-pipeline -p python_test

command to trigger job
> fly -t tutorial trigger-job --job python_test/test-runner --watch

setting concourse web node for vault
> set CONCOURSE_VAULT_URL=https://vault.example.com:8200

setting up path concourse in vault
> vault secrets enable -version=1 -path=concourse kv

creating policy for vault
> path "concourse/*" {
  policy = "read"
}
> save this text in a file
> vault policy write concourse ./concourse-policy.hcl

To generate token
> vault token create --policy concourse --period 5h

set token to web node
> set CONCOURSE_VAULT_CLIENT_TOKEN=<token>

starting vault 
> vault server -dev
> set VAULT_ADDR=http://127.0.0.1:8200
> set VAULT_TOKEN=<Root Token>

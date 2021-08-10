command to run concourse in docker
> docker-compose up -d

command to sign in to concourse with fly
> fly -t tutorial login -c http://localhost:8080 -u test -p test

command to set pipeline
> fly -t tutorial set-pipeline -p stand-alone -c ci/stand_alone.yml

command to unpause pipeline
> fly -t tutorial unpause-pipeline -p stand-alone

command to trigger job
> fly -t tutorial trigger-job --job stand-alone/test-in-master --watch
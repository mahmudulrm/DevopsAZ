### shell gitlab-runner
usermod -aG docker gitlab-runner


image: docker:19.03.12
services:
  - docker:19.03.12-dind

stages:
  - Build
  
variables:
  CONTAINER_TEST_IMAGE: $CI_REGISTRY_IMAGE:latest

build_job:
  stage: Build
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CONTAINER_TEST_IMAGE .
    - docker push $CONTAINER_TEST_IMAGE
    - docker logout

======================
    - docker login -u mahmudulrm -p $VARIABE_DOCKER_TOCKEN
	- docker build -t mahmudulrm/$CONTAINER_TEST_IMAGE .
	- docker push mahmudulrm/$CONTAINER_TEST_IMAGE
    - docker logout
=========================================================================================

stages:
  - Login
  - Build
  - Push
  - Logout
  

variables:
  CONTAINER_TEST_IMAGE: $CI_REGISTRY_IMAGE:test

login_job:
  stage: Login
  tags:
    - docker
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    

build_job:
  stage: Build
  tags:
    - docker
  script:
    - docker build -t $CONTAINER_TEST_IMAGE .
    
push_job:
  stage: Push
  tags:
    - docker
  script:
    - docker push $CONTAINER_TEST_IMAGE

logout_job:
  stage: Logout
  tags:
    - docker
  script:
    - docker logout $CI_REGISTRY
	
	
==
#!/bin/sh
docker run --rm -v ${PWD}/input:/input -v ${PWD}/output:/output text-vis

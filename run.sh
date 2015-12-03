#!/bin/sh
docker pull wrvhage/text-vis
docker run --rm -v ${PWD}/input:/input -v ${PWD}/output:/output wrvhage/text-vis

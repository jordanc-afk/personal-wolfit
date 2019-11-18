#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export ACTIVITY_LOG_MICRO=https://activity-logger-4.herokuapp.com
flask run --host=0.0.0.0
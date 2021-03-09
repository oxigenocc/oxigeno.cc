#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver 0.0.0.0:8000